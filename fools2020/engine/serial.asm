; 0..1 : key
; 2..3 : length
; 4..5 : checksum
; 6..  : data

KeyGenerateByte:
    push bc
    ld a, [wSerialKeyVarA]
    ld b, a
    ld a, [wSerialKeyVarB]
    ld c, a
    xor b
    rlc a
    ld [wSerialKeyVarA], a
    ld a, b
    add a
    xor c
    ld [wSerialKeyVarB], a
    pop bc
    ret

CopySerialStruct:
    ld a, 3
    ld bc, 256
    ld de, SERIAL_SEND_BUF
    jp CopyDataFromSRAX

PrepareRequest:
    ; 0..1 : key
    ; 2..3 : length
    ; 4..5 : checksum
    ; 6..  : data
    ld hl, SERIAL_SEND_BUF
    push hl
    ldh a, [$d3]
    ld [hli], a
    ld [wSerialKeyVarA], a
    ld e, a
    ldh a, [$d4]
    ld [hli], a
    ld [wSerialKeyVarB], a
    ld d, a
    ld a, [hli]
    ld c, a
    ld a, [hli]
    ld b, a
    inc hl
    inc hl
    push hl
    push hl
    push bc
    call CalcChecksum
    pop bc
    pop hl
    dec hl
    ld a, d
    ld [hld], a
    ld [hl], e
    pop hl
.crypt
    call KeyGenerateByte
    xor [hl]
    ld [hli], a
    dec bc
    ld a, c
    or b
    jr nz, .crypt
    pop hl
    ret

; Fletcher's checksum mod 255 from length bc block of data, return in de
CalcChecksum:
    ld de, 0
.loop
    call ReadFromSRA0
    inc hl
    add d
    adc 0
    inc a
    jr z, .wasFF_1
    dec a
.wasFF_1
    ld d, a
    add e
    adc 0
    inc a
    jr z, .wasFF_2
    dec a
.wasFF_2
    ld e, a
    dec bc
    ld a, c
    or b
    jr nz, .loop
    ret

RecvExact:
    ld a, $81
    ldh [$01], a
    ldh [$02], a
.sending
    ; shifting out. animate the loading tile now
    call AnimateLoadingTile
    ; also a good opportunity to generate keybyte
    call KeyGenerateByte
    ld e, a
    ; part of the subroutine is located in WRAM, so it can write to SRA0
    jp RecvExactWRAMDelegate

ExchangeSingle:
    ldh [$01], a
    ld a, $81
    ldh [$02], a
    ; shifting out. animate the loading tile now
    call AnimateLoadingTile
.wait
    ldh a, [$02]
    bit 7, a
    jr nz, .wait
    ldh a, [$01]
    ret

Handshake:
    ld c, 64
.retry
    call DelayFrame
    dec c
    jr z, .error
    ld a, $6d
    call ExchangeSingle
    cp $3a
    jr nz, .retry
    ld a, $a4
    call ExchangeSingle
    cp $f1
    jr nz, .retry
    ld a, $d1
    call ExchangeSingle
    cp $65
    jr nz, .retry
    and a
    ret
.error
    scf
    ret

Request:
    ld de, SERIAL_SEND_BUF
    ; fall through to Request
RequestToDE:
    push de
    push hl
    ld hl, $9690
    ld de, SaveProgressTiles
    ld bc, $0104
    call CopyVideoDataDouble

    ld a, 5 ; vblank and timer, no serial
    ldh [$ff], a

    call Handshake
    jr c, .out

    pop hl

    ; 0..1 : key
    ; 2..3 : length
    ; 4..5 : checksum
    ; 6..  : data
    
    ld a, [hli]
    call ExchangeSingle
    ld a, [hli]
    call ExchangeSingle
    ld a, [hli]
    ld c, a
    call ExchangeSingle
    ld a, [hli]
    ld b, a
    call ExchangeSingle
    ld a, [hli]
    call ExchangeSingle
    ld a, [hli]
    call ExchangeSingle

.sendRequest
    ld a, [hli]
    call ExchangeSingle
    cp $cc
    jr nz, .out2
    dec bc
    ld a, c
    or b
    jr nz, .sendRequest

.waitComplete
    ld a, $cc
    call ExchangeSingle
    cp $cc
    jr z, .waitComplete
    cp $cf
    jr nz, .out2

.getLength
    ; 0..1 : key
    ; 2..3 : length
    ; 4..5 : checksum
    ; 6..  : data
    call ExchangeSingle
    ld [wSerialKeyVarA], a
    call ExchangeSingle
    ld [wSerialKeyVarB], a
    call ExchangeSingle
    ld c, a
    call ExchangeSingle
    ld b, a
    call ExchangeSingle
    ld e, a
    call ExchangeSingle
    ld d, a

    pop hl
    push de
    push hl
    push bc
    call RecvExact
    pop bc
    pop hl
    call CalcChecksum
    pop bc
    call CompareBCToDE
    jr nz, .out3
    and a
    ret
.out
    pop hl
.out2
    pop de
.out3
    scf
    ret

RequestWithErrorHandling:
    ld de, SERIAL_SEND_BUF
RequestToDEWithErrorHandling:
    call RequestToDE
    jr c, .nope
    ret
.nope
    call ConnectionError
    scf
    ret

SaveProgressTiles:
    db %00000000, %00011000, %01000000, %11100010
    db %11100010, %01000000, %00011000, %00000000
    db %00000000, %00011000, %00000000, %01000010
    db %01000010, %00011000, %00111100, %00011000
    db %00000000, %00011000, %00000010, %01000111
    db %01000111, %00000010, %00011000, %00000000
    db %00011000, %00111100, %00011000, %01000010
    db %01000010, %00000000, %00011000, %00000000
