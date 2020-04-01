SECTION "SRA2", ROM0[$A000]

_SRA2Checksum:
    ds 1

_SRA2Ident:
    db 2

include "engine/utils.asm"
include "engine/text.asm"
include "engine/menu.asm"
include "engine/map_loader.asm"
include "engine/dma_hijacking.asm"
include "engine/ram_script.asm"
include "engine/scripting.asm"
include "engine/battle.asm"
include "engine/start_menu.asm"

include "engine/emulator_tests.asm"
include "engine/serial.asm"

_Start:
    ld a, $c0
    ld [wSpritePlayerStateData1YPixels], a
    ld a, $ff
    ld [wAudioFadeOutControl], a
    ld a, 3
    ld [wAudioFadeOutCounterReloadValue], a
    call TextboxEnable
    ld c, 30
    call DelayFrames
    call PlayInventoryMusic
    call CheckEmulationAccuracy
    call c, InaccurateEmulator
    call CheckROM
    call nz, WrongROM
    ld hl, IntroText
    call PrintTextVWF
    ld hl, ConnectionSimpleMenu
    coord de, 2, 2
    call DisplayMenu
    ld hl, ConnectionBeginText
    call PrintTextVWF
.clientHelloLoop
    ld hl, SerialStruct_ClientHello
    call CopySerialStruct
    call PrepareRequest
    call Request
    jr c, .nope
    response_ld_a_at 0
    dec a
    jr z, .success
    dec a
    jr nz, .nope
.outdated
    ld hl, OutdatedVersionText
    call PrintTextVWF
.forever
    jr .forever
.success
    ld a, SFX_TURN_ON_PC
    call PlaySound
    ld hl, ConnectionSuccessText
    call PrintTextVWF
    ld hl, $c490
    ld bc, $0078
    ld a, $10
    call FillMemory
    ld hl, wAudioFadeOutCounter
    ld a, 8
    ld [hld], a
    ld [hld], a
    ld a, $ff
    ld [hl], a
    ld c, 80
    call DelayFrames
    ld a, $01
    ld [wCurrentMapNumber], a
    ld a, $01
    ld [wCurrentMapBank], a
    ld a, $04 ; issotm triggered
    ld [wCurrentWarpTargetX], a
    ld a, $04
    ld [wCurrentWarpTargetY], a
    jp RetrieveAndLoadMap
.nope
    call ConnectionError
    jr .clientHelloLoop

InaccurateEmulator:
    ld hl, InaccurateEmulatorText
    call PrintTextVWF
.forever
    jr .forever
    ret

WrongROM:
    ld hl, WrongROMText
    call PrintTextVWF
.forever
    jr .forever
    ret

InaccurateEmulatorText:
    text "You are using an inaccurate"
    next "or unsupported emulator."
    para "For more information visit:"
    next "zzazzdzz.github.io/emu."
    done

WrongROMText:
    text "You are using a modified or"
    next "invalid ROM image."
    para "This save file is compatible"
    next "with Pokémon Red EN only."
    para "Particularly, Pokémon Blue"
    next "cannot be used with this save."
    para "Consult the event site for"
    next "any further information."
    done

IntroText:
    text "Welcome to Fools2020:"
    next "Tactical Showdown!"
    para "In order to play, you'll need"
    next "to connect to a game server."
    para "Please connect the link cable"
    next "and press A to begin."
    done

ConnectionBeginText:
    text "Great! Let me check your"
    next "connection real quick..."
    done

OutdatedVersionText:
    text "Oops! It looks like you're"
    next "using an outdated version"
    cont "of the save."
    para "Please redownload your save"
    next "file from the event site."
    done

ConnectionSuccessText:
    text "The connection was"
    next "successfully estabilished!"
    para "We will now transfer you to"
    next "the overworld. Good luck!"
    wait