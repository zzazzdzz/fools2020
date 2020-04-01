
RunNPCScript:
    ld hl, wCurTextIDs
    ldh a, [$8c]
    dec a
    add a
    ld c, a
    ld b, 0
    add hl, bc
    ld a, [hli]
    ld h, [hl]
    ld l, a
RunNPCScriptHL:
    push hl
.retry
    ld hl, SerialStruct_RunScript
    call CopySerialStruct
    pop de
    serial_struct_ld_hl RunScript, ScriptIDLo
    ld [hl], e
    inc hl
    ld [hl], d
    push de
    call PrepareRequest
    ld de, SERIAL_SCRIPT_BUF
    call RequestToDEWithErrorHandling
    jr c, .retry
.done
    pop de
    ld hl, SERIAL_SCRIPT_BUF
    ; fall through to InterpretNPCScript

InterpretNPCScript:
    call ReadFromSRA0
    inc hl
    push hl
    ld hl, NPCScriptJumptable - 2
    add a
    ld c, a
    ld b, 0
    add hl, bc
    ld a, [hli]
    ld h, [hl]
    ld l, a
    jp hl

NPCScriptJumptable:
    dw NPCScript_TextBox
    dw NPCScript_YesNo
    dw NPCScript_IfTrue
    dw NPCScript_End
    dw NPCScript_Callscript
    dw NPCScript_Waitbutton
    dw NPCScript_Beginbattle
    dw NPCScript_Closetext
    dw NPCScript_Delay
    dw NPCScript_Opentext

NPCScript_TextBox:
    pop hl
    call ReadFromSRA0
    ld d, a
    inc hl
    call ReadFromSRA0
    inc hl
    push hl
    ld h, a
    ld l, d
    xor a
    call PrintTextVWF_Banked
    pop hl
    jr InterpretNPCScript

NPCScript_YesNo:
    ld hl, YesNoSimpleMenu
    call DisplayMenu
    and a
    ld a, 1
    jr z, .true
    xor a
.true
    ld [wScriptVar], a
    pop hl
    jr InterpretNPCScript

NPCScript_IfTrue:
    pop hl
    ld a, [wScriptVar]
    and a
    jr z, .skip
    call ReadFromSRA0
    ld d, a
    inc hl
    call ReadFromSRA0
    ld h, a
    ld l, d
    jr InterpretNPCScript
.skip
    inc hl
    inc hl
    jr InterpretNPCScript

NPCScript_Waitbutton:
    pop hl
    call WaitButtonPress
    jr InterpretNPCScript

NPCScript_Beginbattle:
    pop hl
    call ReadFromSRA0
    ld e, a
    inc hl
    call ReadFromSRA0
    ld d, a
    inc hl
    push hl
    call BeginBattle
    pop hl
    jr InterpretNPCScript

NPCScript_Closetext:
    call ReturnFromTextboxToOverworld
    pop hl
    jp InterpretNPCScript

ReturnFromTextboxToOverworld:
    ld a, $90
    ldh [$b0], a
    call DelayFrame
    call LoadGBPal
    xor a
    ldh [$ba], a
    call SwitchToMapRomBank
    ldh a, [$f8]
    ld h, a
    ld l, 0
    push hl
    jp $2a22

NPCScript_Delay:
    pop hl
    call ReadFromSRA0
    inc hl
    ld c, a
    call DelayFrames
    jp InterpretNPCScript

NPCScript_Opentext:
    call TextboxEnable
    pop hl
    jp InterpretNPCScript

NPCScript_Callscript:
    pop hl
    call ReadFromSRA0
    ld d, a
    inc hl
    call ReadFromSRA0
    ld h, a
    ld l, d
    jp RunNPCScriptHL

NPCScript_End:
    pop hl
    ret