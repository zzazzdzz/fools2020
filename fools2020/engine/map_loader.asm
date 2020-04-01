
RetrieveAndLoadMap:
    call LoaderTextbox
    ld a, $26
    ld [wCurMap], a
    xor a
    ld [wWarpedFromWhichMap], a
.retry
    ld hl, SerialStruct_DownloadMap
    call CopySerialStruct
    ld a, [wCurrentMapNumber]
    serial_struct_ld_a DownloadMap, MapNumber
    ld a, [wCurrentMapBank]
    serial_struct_ld_a DownloadMap, MapBank
    call PrepareRequest
    call RequestWithErrorHandling
    jr c, .retry
LoadCurrentMap:
    ld a, [wCurrentMapConnection]
    and a
    call z, OnFullMapLoadBegin
    ld hl, SERIAL_SEND_BUF
    ld de, wCurMapTileset
    ld a, [hli] ; tileset
    ld [de], a
    inc de
    ld a, [hli] ; height
    ld [de], a
    inc de
    ld a, [hli] ; width
    ld [de], a
    inc de
    push hl
    ld hl, MapDataPointers
    ld bc, 10
    call CopyData
    pop hl
    ld a, [hli] ; border block
    ld [wMapBackgroundTile], a
    ld a, [hli] ; palette
    ld [wLastMap], a
    ld a, [hli] ; number of warps
    ld [wNumberOfWarps], a
    ld c, a
    ld b, 0
    and a
    jr z, .skipWarps
    ld de, wWarpEntries
.loadWarps
    ld a, [hli] ; y pos
    ld [de], a
    inc de
    ld a, [hli] ; x pos
    ld [de], a
    inc de
    ld a, 4
    ld [de], a
    inc de
    ld [de], a
    inc de
    inc b
    dec c
    jr nz, .loadWarps
    ld de, wWarpCoords
.loadWarpCoords
    ld a, [hli] ; target y pos
    ld [de], a
    inc de
    ld a, [hli] ; target x pos
    ld [de], a
    inc de
    ld a, [hli] ; target map lowbyte
    ld [de], a
    inc de
    dec b
    jr nz, .loadWarpCoords
.skipWarps
    ld a, [hli] ; number of signs
    ld [wNumSigns], a
    ld c, a
    ld b, a
    and a
    jr z, .skipSigns
    ld de, wSignCoords
.loadSignCoords
    ld a, [hli] ; y pos
    ld [de], a
    inc de
    ld a, [hli] ; x pos
    ld [de], a
    inc de
    dec c
    jr nz, .loadSignCoords
    ld de, wSignTextIDs
.loadSignTIDs
    ld a, [hli] ; textbox ID
    ld [de], a
    inc de
    dec b
    jr nz, .loadSignTIDs
.skipSigns
    call ClearSpriteData
    ld a, [hli] ; number of NPCs
	ld [wNumSprites], a
    ld c, a
    ld b, a
    and a
    jr z, .skipSprites
    ld de, wSpriteStateData1 + $10
.loadSpriteData1
    ld a, [hli] ; picture ID
    ld [de], a
    inc d
	ld a, $04
	add e
    ld e, a
    ld a, [hli]
	ld [de], a ; y pos
	inc e
	ld a, [hli]
	ld [de], a ; x pos
	inc e
    ld a, [hli] ; movement byte 1
	ld [de], a
    dec d
	ld a, $0a
	add e
	ld e, a
    dec c
    jr nz, .loadSpriteData1
    ld de, wMapSpriteData
.loadSpriteData2
    ld a, [hli] ; movement byte 2
    ld [de], a
    inc de
    ld a, [hli] ; textbox ID
    ld [de], a
    inc de
    dec b
    jr nz, .loadSpriteData2
.skipSprites
    push hl
    ld a, $19
    call Predef ; LoadTilesetHeader
    call $1206 ; LoadMapHeader.finishUp+?
    pop hl
    ld a, [hli] ; music ID
    ld [wMapMusicSoundID], a
    ld a, [hli] ; music bank
    ld [wMapMusicROMBank], a
    ld de, wMapConnectionMeta
.loadConnectionData
    ld a, [hli] ; connection data until 0xff
    ; format: <connected map ID le><connection offset><connection target X/Y>
    ld [de], a
    inc de
    inc a
    jr nz, .loadConnectionData
    ld de, wCurMapBlocks
.loadMapBlocks
    ld a, [hli] ; map block data until 0xff
    ld [de], a
    inc de
    inc a
    jr nz, .loadMapBlocks
    ld de, wCurTextIDs
.loadTextIDs
    ld a, [hli] ; text ID data until 0xff
    ld [de], a
    inc de
    inc a
    jr nz, .loadTextIDs
    ld de, wCurTextPtrs
    ld bc, StandardTextboxDelegate
.fillTextPointer
    ld a, c
    ld [de], a
    inc de
    ld a, b
    ld [de], a
    inc de
    ld a, e
    and a
    jr nz, .fillTextPointer
.finalize
    push hl ; remember the RAM script
    ld c, 10
.probabilisticSpriteLoading
    push bc
    ld b, b_InitMapSprites
    ld hl, InitMapSprites
    call Bankswitch
    call AnimateLoadingTile
    pop bc
    dec c
    jr nz, .probabilisticSpriteLoading
    ld a, $ff
    call SetMapConnectionBytes
    safe_call_hl LoadTileBlockMap
    pop hl
    ; now we can run the RAM script from earlier
    call RunRAMScript
    xor a
    ld [wFontLoaded], a
    ld [wGrassRate], a
    ld a, $3c
    ld [wSpritePlayerStateData1YPixels], a
    ld a, 4
    ld [wSpriteSetID], a
    call SetMapConnectionBytes
    call PrepareXYPositions
    call TransitionMapMusic
    ld a, [wCurrentMapConnection]
    and a
    call z, OnFullMapLoadFinish
    ld b, b_UsedCut
    ld hl, $6fec
    call Bankswitch ; UsedCut+?
    ld a, $90
    ldh [$b0], a
    ld hl, .returnAddr
    push hl
    call $29f8
.returnAddr
    call LoadGBPal
    call DMAHijackingApply
    ld sp, $dfff
    ld a, $3c
    ld [$c104], a
    jp OverworldLoop

OnFullMapLoadBegin:
    jp BlackOutPals

OnFullMapLoadFinish:
    call DisableLCD
OnFullMapLoadFinish_NoDisableLCD:
    call LoadTilesetTilePatternData
    ld b, b_InitMapSprites
    ld hl, InitMapSprites
    call Bankswitch
    jp EnableLCD

MapDataPointers:
    dw wCurMapBlocks          ; map blocks
    dw wCurTextPtrs           ; text pointers
    dw CheckStartMenu         ; map script
    dw wCurObjectPtrs         ; object data
    db $00, $ff               ; no connections

; yep, this one comes from fools2018!
PrepareXYPositions:
    ld hl, wOverworldMap
    ld a, [wCurrentWarpTargetX]
    srl a
    ld c, a
    ld b, 0
    add hl, bc
    inc hl
    ld a, [wCurrentWarpTargetY]
    srl a
    inc a
    ld d, a
    ld a, [wCurMapWidth]
    add 6
    ld c, a
.yLoop
    add hl, bc
    dec d
    jr nz, .yLoop
.yLoopEnd
    ld de, wCurrentTileBlockMapViewPointer
    ld a, l
    ld [de], a
    inc de
    ld a, h
    ld [de], a
    inc de
    ld a, [wCurrentWarpTargetY]
    ld [de], a
    ld b, a
    inc de
    ld a, [wCurrentWarpTargetX]
    ld [de], a
    ld c, a
    inc de
    ld a, b
    and 1
    ld [de], a
    inc de
    ld a, c
    and 1
    ld [de], a
    ret

SetMapConnectionBytes:
	ld [wMapConn1Ptr], a
	ld [wMapConn2Ptr], a
	ld [wMapConn3Ptr], a
	ld [wMapConn4Ptr], a
    ret

LoadConnectionOrWarpTarget:
    ld a, [wWarpedFromWhichMap]
    and a
    jr nz, .enteringWarp
    ; entering map connection
    ld a, [wCurrentMapConnection]
    dec a
    push af
    ld hl, wMapConnectionMeta
    ld bc, 4 ; size of map connection struct
    call AddNTimes
    ld a, [hli]
    ld [wCurrentMapNumber], a
    ld a, [hli]
    ld [wCurrentMapBank], a
    pop af
    and 2 ; is west/east connection?
    jr nz, .westEast
.northSouth
    ld a, [wXCoord]
    add [hl]
    inc hl
    ld [wCurrentWarpTargetX], a
    ld a, [hl]
    ld [wCurrentWarpTargetY], a
    ret
.westEast
    ld a, [wYCoord]
    add [hl]
    inc hl
    ld [wCurrentWarpTargetY], a
    ld a, [hl]
    ld [wCurrentWarpTargetX], a
    ret
.enteringWarp
    ld hl, wWarpCoords
    ld bc, 3 ; size of map warp struct
    ld a, [wWarpedFromWhichWarp]
    call AddNTimes
    ld a, [hli]
    ld [wCurrentWarpTargetY], a
    ld a, [hli]
    ld [wCurrentWarpTargetX], a
    ld a, [hl]
    ld [wCurrentMapNumber], a
    ret

TransitionMapMusic:
    ld de, wPreviousMapMusic
    ld hl, wMapMusicSoundID
    ld a, [de]
    cp [hl]
    ret z ; no changes
    ld a, [hl]
    ld [de], a

PlayMapMusic:
    ld a, [wMapMusicSoundID]
    cp $01
    jr z, .playUnusedTheme
    jp PlayDefaultMusicCommon
.playUnusedTheme
    ld a, MUSIC_VERMILION
    ld c, AUDIO_1
    call PlayMusic
    xor a
    ld hl, $c006
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hl], $13
    inc hl
    ld [hl], $69
    inc hl
    ld [hli], a
    ld [hl], a
    ret
