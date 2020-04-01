
DMAHijackingApply:
    di
    ld de, DMAHijackingRoutine
    ld hl, $ff80
    ld [hl], $cd
    inc l
    ld [hl], e
    inc l
    ld [hl], d
    inc l
    ld [hl], $e2
    ei
    ; fall through to DMAHijackingEnable

DMAHijackingEnable:
    ld a, 1
    ld [wDMAHijackingEnabled], a
    ret
DMAHijackingDisable:
    xor a
    ld [wDMAHijackingEnabled], a
    ret

DMAHijackingProc:
    ld hl, wJoyIgnore
    set 3, [hl]
    ld a, [wIsInBattle]
    and a
    jr z, .skipMusicChanges
    ld hl, wChannelDuties
    ld a, $80
    ld [hli], a
    ld [hl], a
.skipMusicChanges
    call DMAHijackingCheckBeforeMapConnection
    call DMAHijackingCheckBeforeMapWarp
    call DMAHijackingCheckAfterMapConnection
    ret

DMAHijackingCheckBeforeMapWarp:
    ld a, [wWarpedFromWhichMap]
    and a
    ret z
    xor a
    ld [wOnSGB], a
    ret

DMAHijackingCheckAfterMapConnection:
    ld a, [wCurMap]
    cp 4
    ret nz
    xor a
    ld [wAudioFadeOutControl], a
    call DMAHijackingDisable
    call LoadConnectionOrWarpTarget
    call TextboxEnable
    jp RetrieveAndLoadMap

DMAHijackingCheckBeforeMapConnection:
    ld a, [wWalkCounter]
    and a
    ret z
    ld a, [wWarpedFromWhichMap]
    and a
    ret nz
	ld a, [wSpriteStateData1 + 3] ; delta Y
	ld b, a
	ld a, [wSpriteStateData1 + 5] ; delta X
	ld c, a
    add b
    ret z
    ld a, [wYCoord] ; coord Y
    ld d, a
    ld a, [wXCoord] ; coord X
    ld e, a
    ld a, [wCurMapHeight]
    add a
    dec a
    ld h, a
    ld a, [wCurMapWidth]
    add a
    dec a
    ld l, a
; -----------
; N dY=FF cY=00
; S dY=01 cY=wCurMapHeight*2-1
; W dX=FF cX=00
; E dY=01 cX=wCurMapWidth*2-1
; -----------
    xor a
    cp d
    jr nz, .skipNorth
    dec a
    cp b
    jr nz, .skipNorth
    ld a, 1
    jr .found
.skipNorth
    ld a, 1
    cp b
    jr nz, .skipSouth
    ld a, h
    cp d
    jr nz, .skipSouth
    ld a, 2
    jr .found
.skipSouth
    xor a
    cp e
    jr nz, .skipWest
    dec a
    cp c
    jr nz, .skipWest
    ld a, 3
    jr .found
.skipWest
    ld a, 1
    cp c
    jr nz, .skipEast
    ld a, l
    cp e
    jr nz, .skipEast
    ld a, 4
    jr .found
.skipEast
    xor a
.found
    ld [wCurrentMapConnection], a
    and a
    ld a, [wOrigOnSGB]
    jr z, .restoreSGBFlag
    xor a
.restoreSGBFlag
    ld [wOnSGB], a
    ret
