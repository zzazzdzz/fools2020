
SerialStruct_ClientHello:
    dw 0 ; encryption key
    dw 2 ; payload length
    dw 0 ; checksum
    ; data follows
    db $88 ; packet type = version
SerialStruct_ClientHello_Version:
    db $10 ; version ID
; expected response:
; byte[1] errorCode

SerialStruct_DownloadMap:
    dw 0 ; encryption key
    dw 3 ; payload length
    dw 0 ; checksum
    ; data follows
    db $90 ; packet type = download map
SerialStruct_DownloadMap_MapNumber:
    db 0   ; map number
SerialStruct_DownloadMap_MapBank:
    db 0   ; map bank

; expected response:
; byte[?] mapData

SerialStruct_RunScript:
    dw 0 ; encryption key
    dw 3 ; payload length
    dw 0 ; checksum
    ; data follows
    db $91 ; packet type = script
SerialStruct_RunScript_ScriptIDLo:
    db 0
SerialStruct_RunScript_ScriptIDHi:
    db 0

SerialStruct_StartBattle:
    dw 0 ; encryption key
    dw 4 ; payload length
    dw 0 ; checksum
    ; data follows
    db $92 ; packet type = battle
SerialStruct_StartBattle_PlayerType:
    db 0
SerialStruct_StartBattle_PlayerID:
    dw 0

SerialStruct_ReceiveGift:
    dw 0 ; encryption key
    dw 1 ; payload length
    dw 0 ; checksum
    ; data follows
    db $93 ; packet type = gift

; expected response
; byte[11] enemyNicknames[3]
; byte[11] ownNicknames[3]
; byte[?] battleCommands
; byte[?] battleStrings
