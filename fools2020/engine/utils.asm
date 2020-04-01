
TextboxEnable:
    call SaveScreenTilesToBuffer1
    call SaveScreenTilesToBuffer2
    call LoadFontTilePatterns
TextboxEnable_NoLoadFont:
    ld b, $9c
    ld hl, CopyScreenTileBufferToVRAM
    call SafeCallHL
    ld c, 3
    call DelayFrames
    xor a
    ldh [$b0], a
    inc a
    ldh [$ba], a
    ret

PlayMusicFromRAM:
    ld bc, $0008
    ld de, $C006
    call CopyData
    xor a
    ld bc, $0004
    ld hl, $C016
    call FillMemory
    ld a, $01
    ld bc, $0004
    ld hl, $C0B6
    call FillMemory
    ld a, $e0
    ld bc, $0004
    ld hl, $C026
    jp FillMemory

BlackOutPals:
    ld a, %11111111
WriteAToPals:
	ld [rBGP], a
    ld [rOBP0], a
    ld [rOBP1], a
    ret

AnimateLoadingTile:
    ld a, [wIgnoreInputCounter]
    swap a
    and 3
    add $69
    ld [$c4f2], a
    ret

PlayInventoryMusic:
    ld de, $c9e0
    ld bc, 512
    ld hl, Music_InventoryScreen
    ld a, 3
    call CopyDataFromSRAX
    ld de, $c9d0
    ld bc, 8
    ld hl, Music_InventoryScreen_Pointers
    ld a, 3
    call CopyDataFromSRAX
    ld hl, $c9d0
    jr PlayMusicFromRAM

CompareBCToDE:
    ld a, b
    cp d
    jr nz, .nope
    ld a, c
    cp e
.nope
    ret

CheckROM:
    ld hl, $0000
    ld bc, $3fff
    ld de, $0000
.loop
    ld a, [hl]
    xor d
    ld d, a
    ldi a, [hl]
    add e
    ld e, a
    dec bc
    ld a, c
    or b
    jr nz, .loop
    ld bc, $4DE1
    jp CompareBCToDE

ConnectionError:
    ld a, SFX_DENIED
    call PlaySound
    call WaitForSoundToFinish
    ld hl, ConnectionErrorText
    call PrintTextVWF
    ld hl, ConnectionSimpleMenu
    jp DisplayMenu

ConnectionSimpleMenu:
    db $05,$01 ; w, h
    db %00000001 ; [disable screen save][draw textbox][B allowed][R allowed][L allowed][item size][item size][item size]
    db $92,$b3,$a0,$b1,$b3,$50

YesNoSimpleMenu:
    db $03,$02 ; w, h
    db %00100001 ; [disable screen save][draw textbox][B allowed][R allowed][L allowed][item size][item size][item size]
    db $98,$a4,$b2,$4f,$8d,$ae,$50

ConnectionErrorText:
    text "Oopsie woopsie! Couldn't"
    next "connect to the server."
    para "Check your connection,"
    next "then press A to retry."
    done

PlaceStringSimple:
    push bc
    push hl
    ld bc, 20
.nextChar
    ld a, [de]
    inc de
    cp $50
    jr z, .finished
    cp $4f
    jr z, .nextLine
    ld [hli], a
    jr .nextChar
.nextLine
    pop hl
    add hl, bc
    push hl
    jr .nextChar
.finished
    pop hl
    pop bc
    ret

SaveScreenTilesToBuffer2_SaveAll:
    push af
    push bc
    push de
    push hl
    call SaveScreenTilesToBuffer2
    pop hl
    pop de
    pop bc
    pop af
    ret

LoaderTextbox:
    coord hl, 17, 15
    ld bc, $0101
    call TextBoxBorder
    jp UpdateSprites

ClearSpriteData:
    push hl
    ld hl, wSpriteStateData1 + $10
	ld de, wSpriteStateData2 + $10
	xor a
	ld c, $f0
.clearSpriteData
	ld [hli], a
	ld [de], a
	inc e
	dec c
	jr nz, .clearSpriteData
    ld hl, wSpriteStateData1 + $12
	ld de, $0010
	ld c, $0f
.disableAllSprites
	ld [hl], $ff
	add hl, de
	dec c
	jr nz,.disableAllSprites
    pop hl
    ret

; a -> high vram address (aka starting tile id)
; hl -> target
DrawInventoryIcon:
    ld [hli], a
    inc a
    ld [hli], a
    inc a
    push bc
    ld bc, SCREEN_WIDTH - 2
    add hl, bc
    pop bc
    ld [hli], a
    inc a
    ld [hl], a
    ret

; c -> item ID to load, b -> high vram address
LoadInventoryIcon:
    ld a, b
    and $f0
    swap a
    add $80
    ld d, a
    ld a, b
    and $0f
    swap a
    ld e, a
    ld b, 0
    ld hl, InventoryGraphics
    ld a, 64
    call AddNTimes
    push de
    ld a, 3
    ld de, $cfd0
    push de
    ld bc, 64
    call CopyDataFromSRAX
    pop de
    pop hl
    ld c, 64
    ; fall through to CopyDataDuringHblank
    
; copy c bytes from de to hl during hblank periods
CopyDataDuringHblank:
.waitHblank
    ldh a, [rSTAT]
    and %00000011
    jr nz, .waitHblank
    ld a, [de]
    ld [hli], a
    inc de
    ld a, [de]
    ld [hli], a
    inc de
    dec c
    dec c
    jr z, .done
.waitNoHblank
    ldh a, [rSTAT]
    and %00000011
    jr z, .waitNoHblank
    jr .waitHblank
.done
    ret