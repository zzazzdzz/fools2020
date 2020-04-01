
RunStartMenu:
    ld a, SFX_START_MENU
    call PlaySound
    ld a, 3
    ld [wAudioFadeOutCounterReloadValue], a
    ld a, $ff
    ld [wAudioFadeOutControl], a
    ld c, 55
    call DelayFrames
    call PlayInventoryMusic
    call TextboxEnable
    ld hl, StartMenuText
    call PrintTextVWF
    ld hl, StartMenuMenu
    call DisplayMenu
    ; notlikethis
    cp $ff
    jp z, QuitStartMenu
    cp $03
    jp z, QuitStartMenu
    cp $01
    jr z, StartMenu_TravelBack
    cp $02
    jr z, StartMenu_MysteryGift
    ; fall through

StartMenu_BattleReplay:
    ld hl, BattleReplayText
    call PrintTextVWF
    ld hl, YesNoSimpleMenu
    call DisplayMenu
    and a
    jp nz, QuitStartMenu
    ld c, 1
    call BeginExtendedBattle
    ld hl, BattleReplayFinishedText
    call PrintTextVWF
    jp QuitStartMenuNoMusic

StartMenu_TravelBack:
    ld hl, TravelBackText
    call PrintTextVWF
    ld hl, YesNoSimpleMenu
    call DisplayMenu
    and a
    jr nz, QuitStartMenu
    call InitFadeout
    call QuitStartMenuNoMusic
    ld a, $01
    ld [wCurrentMapNumber], a
    ld [wPreviousMapMusic], a
    ld a, $01
    ld [wCurrentMapBank], a
    ld a, $04
    ld [wCurrentWarpTargetX], a
    ld a, $04
    ld [wCurrentWarpTargetY], a
    jp RetrieveAndLoadMap

StartMenu_MysteryGift:
    ld hl, MysteryGiftText
    call PrintTextVWF
    ld hl, YesNoSimpleMenu
    call DisplayMenu
    and a
    jr nz, QuitStartMenu
.retry
    ld hl, SerialStruct_ReceiveGift
    call CopySerialStruct
    call PrepareRequest
    call RequestWithErrorHandling
    jr c, .retry
    response_ld_a_at 0
    dec a
    jr z, .noGift
    ld de, SERIAL_SEND_BUF + 1
    ld hl, wTextBoxBufferListPtr + 1
    ld [hl], e
    inc hl
    ld [hl], d
    ld hl, MysteryGift_GiftReceiveText
    call PrintTextVWF
    ld a, SFX_POKEDEX_RATING
    call PlaySound
    call WaitForSoundToFinish
    ld hl, MysteryGift_GiftPutAwayText
    call PrintTextVWF
    jp QuitStartMenu
.noGift
    ld hl, MysteryGift_NoGiftText
    call PrintTextVWF
    jp QuitStartMenu

InitFadeout:
    ld a, 4
    ld [wAudioFadeOutCounterReloadValue], a
    ld a, $ff
    ld [wAudioFadeOutControl], a
    ld [wLastMusicSoundID], a
    ld c, 50
    jp DelayFrames

QuitStartMenu:
    call InitFadeout
    call PlayMapMusic
QuitStartMenuNoMusic:
    call LoadWalkingPlayerSpriteGraphics
    jp ReturnFromTextboxToOverworld

StartMenuText:
    text "What do you want to do?"
    done

TravelBackText:
    text "You will now return to the"
    next "Town of Beginnings."
    cont "Is that OK?"
    done

BattleReplayText:
    text "This functionality allows you"
    next "to rewatch a recent battle."
    para "On the event site, open any"
    next "report, then select Replay."
    para "Do you want to rewatch your"
    next "selected battle now?"
    done

MysteryGiftText:
    text "Receive a Mystery Gift?"
    done

MysteryGift_NoGiftText:
    text "There seem to be no gifts"
    next "waiting for you right now."
    wait

MysteryGift_GiftPutAwayText:
    text "The <B>"
    tx_buf_id 0
    text "</B> was"
    next "added to your inventory."
    wait

MysteryGift_GiftReceiveText:
    text "<B>"
    tx_buf_id 0
    text "</B> was sent"
    next "over by <B>"
    tx_buf_id 1
    text "</B>!"
    done

BattleReplayFinishedText:
    text "Battle replay was finished."
    wait
    done

StartMenuMenu:
    db $0d,$04 ; w, h
    db %00100001 ; [disable screen save][draw textbox][B allowed][R allowed][L allowed][item size][item size][item size]
    db $81,$a0,$b3,$b3,$ab,$a4,$7f,$b1,$a4,$af,$ab,$a0,$b8,$4f
    db $93,$b1,$a0,$b5,$a4,$ab,$7f,$a1,$a0,$a2,$aa,$4f
    db $8c,$b8,$b2,$b3,$a4,$b1,$b8,$7f,$86,$a8,$a5,$b3,$4f
    db $90,$b4,$a8,$b3,$50