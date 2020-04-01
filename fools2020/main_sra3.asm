SECTION "SRA3", ROM0[$A000]

_SRA3Checksum:
    ds 1

_SRA3Ident:
    db 3

include "include/menu_music.asm"
include "include/serial_structs.asm"

CharacterSet:

include "include/charset.asm"

InventoryGraphics:

include "include/item_graphics.asm"