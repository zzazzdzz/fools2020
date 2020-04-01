SECTION "WRAM", ROM0[$DA80]

_EntryPoint:
    call VerifySaveFile
    ld a, [wOnSGB]
    ld [wOrigOnSGB], a
    jp _Start

wTextEngineVarsStart:
wTextEngineCurrentGlyph:
    ds 9
wTextEngineWorkingBlocks:
wTextEngineWorkingBlock1:
    ds 8
wTextEngineWorkingBlock2:
    ds 8
wTextEngineBoldFace:
    ds 1
wTextEngineCurrentXPosition:
    ds 1
wTextEngineCurrentCharIndex:
    ds 1
wTextEngineCurrentTilemapIndex:
    ds 1
wTextEngineVarsEnd:

wSerialKeyVarA:
    ds 1
wSerialKeyVarB:
    ds 1

wMenuCurrentSettings:
    ds 1
wMenuNumOptions:
    ds 1
wCurrentMapBank:
    ds 1
wCurrentMapNumber:
    ds 1
wCurrentMapWarp:
    ds 1
wCurrentWarpTargetX:
    ds 1
wCurrentWarpTargetY:
    ds 1
wOrigOnSGB:
    ds 1
wCurrentMapConnection:
    ds 1
wDMAHijackingEnabled:
    ds 1
wPreviousMapMusic:
    ds 1
wRAMScriptFillByte:
    ds 1
wTextBoxBank:
    ds 1
wTextBoxBufferPtr:
    ds 3
wTextBoxBufferListPtr:
    ds 3
wScriptVar:
    ds 1
wAttackerMonID:
    ds 1
wDefenderMonID:
    ds 1
wBattleWon:
    ds 1

wNumCreditsGained:
    ds 2
wNumBPGained:
    ds 2

wOpponentName:
    ds 21

wBattleItemIDs:
wOwnItemIDs:
    ds 8
wEnemyItemIDs:
    ds 8

wCurrentBattleCommand:
    ds 6

wTxNumBuf:
    ds 5

VerifySaveFile:
    call SwitchToSRA3
    call .calc
    call SwitchToSRA2
    ; fall through to .calc
.calc
    call CalcSRAMChecksum
    ld a, [$a000]
    cp d
    jr nz, .wrong
    ret
.wrong
    call LoadFontTilePatterns
    xor a
    ldh [$b0], a
    inc a
    ldh [$ba], a
    ld hl, SaveDataCorruptedText
    call PrintText
.forever
    jr .forever

SaveDataCorruptedText:
    db $00,$93,$a7,$a4,$7f,$b2,$a0,$b5,$a4,$7f,$a3,$a0,$b3,$a0,$4f
    db $a8,$b2,$7f,$a2,$ae,$b1,$b1,$b4,$af,$b3,$a4,$a3,$e8,$51

    db $8f,$ab,$a4,$a0,$b2,$a4,$7f,$b1,$a4,$a3,$ae,$b6,$ad,$ab,$ae,$a0,$a3,$4f
    db $b3,$a7,$a4,$7f,$b2,$a0,$b5,$a4,$7f,$a5,$a8,$ab,$a4,$e8,$57

CalcSRAMChecksum:
    ld hl, $a001
    ld bc, $1fff
    ld d, $55
.loop
    ld a, [hli]
    xor d
    inc a
    ld d, a
    dec bc
    ld a, b
    or c
    jr nz, .loop
    ret

SwitchToSRA2:
    ld a, 2
SwitchToSRAX:
    ld [wCurrentSRAMBank], a
SwitchToSRAX_NoPreserve:
    ld [$4000], a
    ld a, $0a
    ld [$0000], a
    ret
SwitchToSRA3:
    ld a, 3
    jr SwitchToSRAX

wCurrentSRAMBank:
    ds 1

SafeCall:
    db $cd ; call
wSafeCallAddressLow:
    ds 1
wSafeCallAddressHigh:
    ds 1
RestoreAndReturn:
    ld a, [wCurrentSRAMBank]
    jr SwitchToSRAX
SafeCallHL:
    call .jp_hl
    jr RestoreAndReturn
.jp_hl
    jp hl

CopyDataFromSRAX:
    call SwitchToSRAX_NoPreserve
    call CopyData
    jr RestoreAndReturn

ReadFromSRA0:
    xor a
ReadFromSRAX:
    call SwitchToSRAX_NoPreserve
    ld a, [hl]
    push af
    call RestoreAndReturn
    pop af
    ret

RecvExactWRAMDelegate:
    xor a
    call SwitchToSRAX_NoPreserve
    ;ld a, [hl] ; stop on $ff in target buffer - protects against overflows
    ;inc a
    ;ret z
.wait
    ldh a, [$02]
    bit 7, a
    jr nz, .wait
.received
    ldh a, [$01]
    xor e
    ld [hli], a
    ld a, 2
    call SwitchToSRAX_NoPreserve
    dec bc
    ld a, c
    or b
    jp nz, RecvExact
    ret

StandardTextboxDelegate:
    db 8 ; TX_ASM
    call SwitchToSRA2
    call RunNPCScript
    jp TextScriptEnd

DetermineCurrentSRABank:
    ld a, [_SRA2Ident]
    cp 2
    ret z
    cp 3
    ret z
    xor a
    ret

CheckStartMenu:
    ldh a, [$f8]
    and $08
    ret z
    call SwitchToSRA2
    jp RunStartMenu

DMAHijackingRoutine:
    add sp, 12
    pop de
    ld hl, wDMAHijackingReturnAddress
    ld [hl], e
    inc hl
    ld [hl], d
    ld hl, DMAHijackingReturn
    push hl
    add sp, -12
    ld a, $c3
    ld c, $46
    ret

DMAHijackingReturn:
    push af
    push bc
    push de
    push hl
    ld a, [wDMAHijackingEnabled]
    and a
    jr z, .disabled
    call DetermineCurrentSRABank
    push af
    ld a, 2
    call SwitchToSRAX_NoPreserve
    call DMAHijackingProc
    pop af
    call SwitchToSRAX_NoPreserve
.disabled
    pop hl
    pop de
    pop bc
    pop af
    db $c3 ; jp
wDMAHijackingReturnAddress:
    ds 2