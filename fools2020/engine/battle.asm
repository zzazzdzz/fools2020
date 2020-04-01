include "include/battle_text.asm"

FillScreenWithTile:
    ld bc, SCREEN_WIDTH * SCREEN_HEIGHT
    ld hl, wTileMap
    jp FillMemory

BeginBattle:
    ld c, 0
BeginExtendedBattle:
    push de
    push bc
    call SaveScreenTilesToBuffer2
    ld c, AUDIO_2
    ld a, MUSIC_TRAINER_BATTLE
    ld [wIsInBattle], a
    call PlayMusic
    farcall LoadBattleTransitionTile
    ld [wBattleTransitionSpiralDirection], a
    farcall BattleTransition_Spiral
    ldh a, [$d7]
    ld [wSavedTilesetType], a
    xor a
    ldh [$d7], a
    ld a, $ff
    call FillScreenWithTile
    call UpdateSprites
    call TextboxEnable_NoLoadFont
    call LoaderTextbox
    call DelayFrame
    call LoadGBPal
.retry
    ld hl, SerialStruct_StartBattle
    call CopySerialStruct
    serial_struct_ld_hl StartBattle, PlayerType
    pop bc
    pop de
    ld [hl], c
    inc hl
    ld [hl], e
    inc hl
    ld [hl], d
    push de
    push bc
    call PrepareRequest
    ld de, SERIAL_BATTLE_BUF
    call RequestToDEWithErrorHandling
    jr c, .retry
.done
    pop bc
    pop de
    ld hl, SERIAL_BATTLE_BUF
    ; load stuff here
    ld de, wBattleItemIDs
    ld bc, 16
    xor a
    call CopyDataFromSRAX
    ; read trainer class
    xor a
    call ReadFromSRAX
    ld [wTrainerClass], a
    inc hl
    ; read bp gained
    ld de, wNumCreditsGained
    xor a
    call ReadFromSRAX
    ld [de], a
    inc de
    inc hl
    xor a
    call ReadFromSRAX
    ld [de], a
    inc hl
    ; read credits gained
    ld de, wNumBPGained
    xor a
    call ReadFromSRAX
    ld [de], a
    inc de
    inc hl
    xor a
    call ReadFromSRAX
    ld [de], a
    inc hl
    ; read attacker id
    xor a
    call ReadFromSRAX
    ld [wAttackerMonID], a
    inc hl
    ; read defender id
    xor a
    call ReadFromSRAX
    ld [wDefenderMonID], a
    inc hl
    ld de, wOpponentName
.readTrainerName
    xor a
    call ReadFromSRAX
    inc hl
    ld [de], a
    inc de
    and a
    jr nz, .readTrainerName
.skipZeros
    xor a
    call ReadFromSRAX
    inc hl
    and a
    jr z, .skipZeros
.nonZero
    dec hl
    xor a
    ld [wTextBoxBufferListPtr], a
    call ReadFromSRAX
    ld e, a
    inc hl
    xor a
    call ReadFromSRAX
    ld d, a
    inc hl
    push hl
    add hl, de
    ld a, l
    ld [wTextBoxBufferListPtr + 1], a
    ld a, h
    ld [wTextBoxBufferListPtr + 2], a
    call BlackOutPals
	call GetTrainerInformation
    safe_farcall _LoadTrainerPic
    ld hl, SERIAL_BATTLE_BUF
    ld a, $7f
    call FillScreenWithTile
    xor a
	ldh [$e1], a
	coord hl, SCREEN_WIDTH/2-3, 2
    ld a, 1
    call Predef
    call Delay3
    call DisableLCD
	farcall LoadHudAndHpBarAndStatusTilePatterns
    ld hl, $9800
	ld bc, $400
    ld a, $7f
    call FillMemory
    ld a, $70
    ldh [rWX], a
    call EnableLCD
	ld b, 8
	call RunPaletteCommand
    call DelayFrame
    call LoadGBPal
    ld h, $70
.scroll
    ldh [rWX], a
    call DelayFrame
    ld a, h
    sub 4
    ld h, a
    cp 4
    jr nz, .scroll
.adjustScroll
    ld a, 7
    ldh [rWX], a
.playTrainerSFX
	xor a
    ld [wOnSGB], a
	ld [wFrequencyModifier], a
	ld a, $80
	ld [wTempoModifier], a
    ld a, $e9
    call PlaySound
    call WaitForSoundToFinish
    ld hl, ChallengedByText
    call PrintTextVWF
.delayIntroText
    ld c, 80
    call DelayFrames
    ld b, 14
.scrollOut
    coord hl, 6, 2
    ld c, SCREEN_WIDTH * 6 + 8
.shiftOut
    inc hl
    ld a, [hld]
    ld [hli], a
    dec c
    jr nz, .shiftOut
    coord hl, SCREEN_WIDTH-1, 1
    ld c, 7
.patchTiles
    ld [hl], $7f
    ld a, l
    add SCREEN_WIDTH
    ld l, a
    ld a, h
    adc 0
    ld h, a
    dec c
    jr nz, .patchTiles
    call DelayFrame
    dec b
    jr nz, .scrollOut
.printSendOutText
    ld hl, SendOutText
    call PrintTextVWF
    ld a, $0f
    call BankswitchHome
    ld a, [wDefenderMonID]
    ld [wBattleMonSpecies2], a
    ld [wEnemyMonSpecies2], a
    ld [wcf91], a
	ld [wd0b5], a
    push af
	call GetMonHeader
	ld de, $9000
	safe_call LoadMonFrontSprite
	ld a, -$31
	ldh [$e1], a
	coord hl, 15, 6
    safe_call $707b
    pop af
	call PlayCry
    ld a, [wAttackerMonID]
    ld [wBattleMonSpecies], a
    ld [wBattleMonSpecies2], a
	ld [wd0b5], a
    call GetMonHeader
    safe_call $4ca7
    ld de, 0
    ld b, $80
    ld hl, wBattleItemIDs
.loadItemIcons
    ld a, b
    cp $bc
    jr nz, .notLast
    ld b, $e0
.notLast
    ld a, [hli]
    ld c, a
    push hl
    push bc
    push de
    call LoadInventoryIcon
    pop de
    pop bc
    ld hl, CoordsOfItems
    add hl, de
    add hl, de
    ld a, [hli]
    ld h, [hl]
    ld l, a
    ld a, b
    call DrawInventoryIcon
    push de
    push bc
    ld a, 3
    call PlaySound
    ld c, 6
    call DelayFrames
    pop bc
    pop de
    pop hl
    inc b
    inc b
    inc b
    inc b
    inc e
    ld a, e
    cp 16
    jr nz, .loadItemIcons
    coord hl, 0, 0
    call DrawHealthbar
    coord hl, 10, 7
    call DrawHealthbar
    ; fall through to RunBattleScript

RunBattleScript:
    pop hl
    push hl
    ld de, wCurrentBattleCommand
    ld bc, 6
    xor a
    call CopyDataFromSRAX
    ;ld b, b
    ld a, [wCurrentBattleCommand]
    cp $ff
    jr z, .end
    bit 7, a
    jr nz, BattleScriptMessage
    ld hl, BattleScriptJumptable
    ld b, 0
    ld c, a
    add hl, bc
    add hl, bc
    ld a, [hli]
    ld h, [hl]
    ld l, a
    jp hl
.end
    ld a, [wBattleWon]
    and a
    jr z, .battleLost
    ld a, MUSIC_DEFEATED_GYM_LEADER
    call PlayBattleVictoryMusic
    ld hl, VictoryText
    call PrintTextVWF
    jp ReturnFromBattleToOverworld
.battleLost
    ld c, 6
    ld hl, wd72c
    set 1, [hl]
.reduceVolume
    push bc
    ld a, 1
    ld [wAudioFadeOutControl], a
    ld a, 1
    ld [wAudioFadeOutCounter], a
    call DelayFrame
    call DelayFrame
    call DelayFrame
    pop bc
    dec c
    jr nz, .reduceVolume
    xor a
    ld [wAudioFadeOutControl], a
.defeatedText
    ld hl, DefeatedText
    call PrintTextVWF
    jp ReturnFromBattleToOverworld

BattleScriptMessage:
    pop hl
    ld a, [wCurrentBattleCommand]
    and $7f
    ld b, 0
    ld c, a
    add hl, bc
    inc hl
    push hl
    ld hl, BattleMessagePointers
    ld a, [wCurrentBattleCommand + 1]
    ld c, a
    add hl, bc
    add hl, bc
    ld a, [hli]
    ld h, [hl]
    ld l, a
    call PrintTextVWF
BattleScriptNone:
    jp RunBattleScript

BattleScriptDamage:
    pop hl
    inc hl
    inc hl
    inc hl
    push hl
	xor a
	ld [wFrequencyModifier], a
	ld [wTempoModifier], a
    ld a, SFX_DAMAGE
    call PlaySound
    ld a, [wCurrentBattleCommand + 1]
    ldh [$f3], a
    push af
    call BlinkAttackedMon
    pop af
    coord hl, 2, 0
    and a
    jr nz, .defender
    coord hl, 12, 7
.defender
    ld a, [wCurrentBattleCommand + 2]
    call AnimateHealthbar
    jp RunBattleScript

BattleScriptHeal:
    pop hl
    inc hl
    inc hl
    inc hl
    push hl
    ld a, [wCurrentBattleCommand + 1]
    coord hl, 2, 0
    and a
    jr nz, .defender
    coord hl, 12, 7
.defender
    ld a, [wCurrentBattleCommand + 2]
    call AnimateHealthbar
    jp RunBattleScript

BattleScriptTrigger:
    pop hl
    inc hl
    inc hl
    push hl
    ld a, [wCurrentBattleCommand + 1]
    ;ld b, b
    call BlinkItem
    call BlinkItem
    call BlinkItem
    jp RunBattleScript

BattleScriptFaint:
    pop hl
    inc hl
    inc hl
    push hl
    call PlayFaintSFX
    xor a
    ld [wInHandlePlayerMonFainted], a
    ld a, [wCurrentBattleCommand + 1]
    and a
    jr nz, .defender
    call RemoveFaintedPlayerMon
    xor a
    ld [wBattleWon], a
    jp RunBattleScript
.defender
    ; faint
    coord hl, 12, 5
	coord de, 12, 6
	call SlideDownFaintedMonPic
	coord hl, 0, 0
	lb bc, 5, 11
	call ClearScreenArea
    ld a, 1
    ld [wBattleWon], a
    ; jump back
    jp RunBattleScript

BattleScriptReplace:
    pop hl
    inc hl
    inc hl
    inc hl
    push hl
    ld a, [wCurrentBattleCommand + 1]
    ld hl, CoordsOfItems
    ld b, 0
    ld c, a
    add hl, bc
    add hl, bc
    ld a, [hli]
    ld h, [hl]
    ld l, a
    ld a, [hl]
    push hl
    push af
    call ClearItem
    ld a, SFX_DOUBLESLAP
    call PlaySound
    ld c, 10
    call DelayFrames
    pop af
    ld b, a
    push af
    ld a, [wCurrentBattleCommand + 2]
    ld c, a
    call LoadInventoryIcon
    pop af
    pop hl
    call DrawInventoryIcon
    ld c, 10
    call DelayFrames
    jp RunBattleScript

PlayFaintSFX:
	xor a
	ld [wFrequencyModifier], a
	ld [wTempoModifier], a
	ld a, SFX_FAINT_FALL
	call PlaySoundWaitForCurrent
.sfxwait
	ld a, [wChannelSoundIDs + 4]
	cp SFX_FAINT_FALL
	jr z, .sfxwait
	ld a, SFX_FAINT_THUD
	jp PlaySound

BlinkAttackedMon:
	ld c, 4
.loop
	push bc
	farcall AnimationHideMonPic
	ld c, 3
	call DelayFrames
	farcall AnimationShowMonPic
	ld c, 3
	call DelayFrames
	pop bc
	dec c
	jr nz, .loop
    ret

BlinkItem:
    push af
    ld c, a
    xor a
	ld [wFrequencyModifier], a
	ld a, $80
	ld [wTempoModifier], a
    ld a, $e9
    call PlaySound
    ld b, 0
    ld hl, CoordsOfItems
    add hl, bc
    add hl, bc
    ld a, [hli]
    ld h, [hl]
    ld l, a
    ld d, [hl]
    push hl
    call ClearItem
    pop hl
    ld c, 5
    call DelayFrames
    ld a, d
    call DrawInventoryIcon
    ld c, 5
    call DelayFrames
    pop af
    ret

ClearItem:
    ld a, $7f
    ld [hli], a
    ld [hli], a
    push bc
    ld bc, SCREEN_WIDTH - 2
    add hl, bc
    pop bc
    ld [hli], a
    ld [hl], a
    ret

GetCurrentHealthbarState:
    push hl
    push bc
    ld bc, $0007
.getStateLoop
    ld a, [hli]
    sub $63
    add b
    ld b, a
    dec c
    jr nz, .getStateLoop
    ld a, b
    pop bc
    pop hl
    ret

UpdateHealthbarState:
    push bc
    push hl
.subFull
    sub 8
    jr c, .subParts
    ld [hl], $6b
    inc hl
    jr .subFull
.subParts
    add 8 + $63
    ld [hl], a
    pop hl
    pop bc
    ret

AnimateHealthbar:
    ld b, a
    call GetCurrentHealthbarState
    ld c, a
.animation
    ld a, c
    cp b
    jr z, .finish
    jr c, .less
.more
    dec c
    jr .cont
.less
    inc c
.cont
    ld a, c
    call UpdateHealthbarState
    call DelayFrame
    jr .animation
.finish
    ret

BattleScriptJumptable:
    dw BattleScriptNone
    dw BattleScriptMessage
    dw BattleScriptTrigger
    dw BattleScriptReplace
    dw BattleScriptDamage
    dw BattleScriptHeal
    dw BattleScriptFaint

ChallengedByText:
    text "You are challenged by"
    next "<B>"
    tx_buf 0, wOpponentName
    text "</B>!"
    done

SendOutText:
    text "<B>"
    tx_buf_id 1
    text "</B> was sent out."
    next "Go, <B>"
    tx_buf_id 0
    text "</B>!"
    done

DefeatedText:
    text "You lost against"
    next "<B>"
    tx_buf 0, wOpponentName
    text "</B>!"
    tx_wait 120
    tx_cls
    text "You gave out <B>"
    tx_num wNumCreditsGained
    text "</B> credits"
    next "and <B>"
    tx_num wNumBPGained
    text "</B> BP to the winner."
    tx_wait 120
    tx_cls
    text "You walked away, overwhelmed"
    next "by your defeat."
    tx_wait 120
    done

VictoryText:
    text "You won the battle against"
    next "<B>"
    tx_buf 0, wOpponentName
    text "</B>!"
    tx_wait 120
    tx_cls
    text "You received <B>"
    tx_num wNumCreditsGained
    text "</B> credits"
    next "and <B>"
    tx_num wNumBPGained
    text "</B> BP for winning."
    tx_wait 120
    done

CoordsOfItems:
    dw_coord 0, 1
    dw_coord 2, 1
    dw_coord 4, 1
    dw_coord 6, 1
    dw_coord 8, 1
    dw_coord 0, 3
    dw_coord 2, 3
    dw_coord 4, 3
    dw_coord 10, 8
    dw_coord 12, 8
    dw_coord 14, 8
    dw_coord 16, 8
    dw_coord 18, 8
    dw_coord 10, 10
    dw_coord 12, 10
    dw_coord 14, 10

DrawHealthbar:
    ld [hl], $71
    inc hl
    ld [hl], $62
    inc hl
    ld a, $6b
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    ld [hli], a
    inc a
    ld [hl], a
    ret

ReturnFromBattleToOverworld:
    ld a, 25
    ld [wAudioFadeOutCounterReloadValue], a
    ld a, $ff
    ld [wAudioFadeOutControl], a
    ld c, 80
    call DelayFrames
    ld a, [wOrigOnSGB]
    ld [wOnSGB], a
    ld hl, wd72c
    res 1, [hl]
    ld a, [wSavedTilesetType]
    ldh [$d7], a
    xor a
    call WriteAToPals
    ld [wFontLoaded], a
    ld [wIsInBattle], a
    call DisableLCD
    ; lcd disabled
    ld a, $98
	ld [wMapViewVRAMPointer + 1],a
	xor a
	ld [wMapViewVRAMPointer], a
    ldh [$af], a
    ldh [$ae], a
    ldh [$42], a
    ldh [$43], a
    call LoadMapViewAndCopyToVRAM
    call OnFullMapLoadFinish_NoDisableLCD
    ; lcd enabled now
    call LoadWalkingPlayerSpriteGraphics
    call UpdateSprites
	ld b, 9
	call RunPaletteCommand
    call DelayFrame
    call LoadGBPal
    call GBFadeInFromWhite
	call PlayMapMusic
    pop de
    ret

LoadMapViewAndCopyToVRAM:
    call LoadCurrentMapView
	coord hl, 0, 0
	ld de, $9800
	ld b, 18
.vramCopyLoop
	ld c, 20
.vramCopyInnerLoop
	ld a, [hli]
	ld [de], a
	inc e
	dec c
	jr nz, .vramCopyInnerLoop
	ld a, 32 - 20
	add e
	ld e, a
	jr nc, .noCarry
	inc d
.noCarry
	dec b
	jr nz, .vramCopyLoop
    ret
