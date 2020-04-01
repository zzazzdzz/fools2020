safe_call: MACRO
    ld a, LOW(\1)
    ld [wSafeCallAddressLow], a
    ld a, HIGH(\1)
    ld [wSafeCallAddressHigh], a
    call SafeCall
ENDM

safe_call_hl: MACRO
    ld hl, \1
    call SafeCallHL
ENDM

coord: MACRO
    IF _NARG >= 4
        ld \1, \4 + SCREEN_WIDTH * \3 + \2
    ELSE
        ld \1, wTileMap + SCREEN_WIDTH * \3 + \2
    ENDC
ENDM

lb: MACRO ; r, hi, lo
	ld \1, (\2) << 8 + ((\3) & $ff)
ENDM

dw_coord: MACRO
    dw wTileMap + SCREEN_WIDTH * \2 + \1
ENDM

farcall: MACRO
    ld b, b_\1
    ld hl, \1
    call Bankswitch
ENDM

safe_farcall: MACRO
    ld b, b_\1
    ld hl, \1
    safe_call Bankswitch
ENDM

text   EQUS "db " ; Start writing text.
next   EQUS "db $F2," ; Move a line down.
para   EQUS "db $F3," ; Start a new paragraph.
cont   EQUS "db $F1," ; Scroll to the next line.
done   EQUS "db $0"  ; End a text box.
wait   EQUS "db $F4,0"

tx_buf: MACRO
    db $f7
    db \1
    dw \2
ENDM

tx_buf_id: MACRO
    db $f8
    db \1
ENDM

tx_buf_id_indirect: MACRO
    db $f9
    db \1
ENDM

tx_num: MACRO
    db $fa
    dw \1
ENDM

tx_wait: MACRO
    db $fb
    db \1
ENDM

tx_cls: MACRO
    db $fc
ENDM

serial_struct_ld_a: MACRO
    IF _NARG < 3
        ld [SERIAL_SEND_BUF + (SerialStruct_\1_\2 - SerialStruct_\1)], a
    ELSE
        ld [\1 + (SerialStruct_\2_\3 - SerialStruct_\2)], a
    ENDC
ENDM

serial_struct_ld_hl: MACRO
    IF _NARG < 3
        ld hl, SERIAL_SEND_BUF + (SerialStruct_\1_\2 - SerialStruct_\1)
    ELSE
        ld hl, \1 + (SerialStruct_\2_\3 - SerialStruct_\2)
    ENDC
ENDM

response_ld_a: MACRO
    IF _NARG < 3
        ld a, [SERIAL_SEND_BUF + (SerialStruct_\1_\2 - SerialStruct_\1) - 6]
    ELSE
        ld a, [\1 + (SerialStruct_\2_\3 - SerialStruct_\2) - 6]
    ENDC
ENDM

response_ld_hl: MACRO
    IF _NARG < 3
        ld hl, SERIAL_SEND_BUF + (SerialStruct_\1_\2 - SerialStruct_\1) - 6
    ELSE
        ld hl, \1 + (SerialStruct_\2_\3 - SerialStruct_\2) - 6
    ENDC
ENDM

response_ld_a_at: MACRO
    ld a, [SERIAL_SEND_BUF + \1]
ENDM

data_offset equs "6 + "