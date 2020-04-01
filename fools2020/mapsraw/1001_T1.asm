SECTION "XXX", ROM0[$B800]

X_Header:
    hdr_tileset         0
    hdr_dimensions      14, 14
    hdr_palette         $03
    hdr_music           $ff, $02
    hdr_connection      NORTH, $0000, 0, 0
    hdr_connection      SOUTH, $0000, 0, 0
    hdr_connection      WEST,  $0000, 0, 0
    hdr_connection      EAST,  $0000, 0, 0
    
X_Objects:
    hdr_border          $00
    hdr_warp_count      0
    hdr_sign_count      0
    hdr_object_count    3
    hdr_object          SPRITE_RED, 19, 7, STAY, NONE, $01
    hdr_object          SPRITE_RED, 7, 17, STAY, NONE, $02
    hdr_object          SPRITE_RED, 11, 11, STAY, NONE, $03

X_RAMScript:
    hdr_textptrs        $0000
    rs_end

X_Blocks:
    db $0F,$0F,$0F,$0A,$01,$0A,$0A,$0F,$0F,$0F,$0F,$0F,$0F,$0F
    db $0F,$0F,$6D,$0A,$01,$0A,$0F,$0F,$0F,$0F,$0F,$0F,$0F,$0F
    db $0F,$0A,$0A,$0A,$01,$0A,$0F,$0F,$74,$0F,$0F,$0F,$0F,$0F
    db $0F,$0F,$74,$0A,$01,$01,$01,$01,$01,$0A,$02,$03,$0F,$0F
    db $0F,$0F,$0F,$0A,$01,$0A,$0C,$0E,$01,$01,$01,$01,$0F,$0F
    db $0F,$0F,$0F,$0A,$01,$0A,$10,$12,$0A,$01,$0A,$0A,$0A,$0A
    db $0F,$0F,$6D,$74,$01,$74,$0A,$0A,$0A,$01,$0A,$74,$0A,$74
    db $0F,$0F,$0A,$74,$01,$01,$01,$01,$01,$01,$01,$01,$01,$01
    db $0F,$0A,$0A,$0A,$02,$03,$01,$74,$01,$02,$03,$0A,$74,$0A
    db $0F,$0A,$01,$01,$01,$01,$01,$74,$01,$01,$01,$0A,$0F,$0F
    db $01,$01,$01,$0A,$0A,$6F,$0A,$0A,$01,$0A,$74,$6E,$0F,$0F
    db $0A,$0A,$0A,$0A,$0F,$0F,$6F,$0A,$01,$0A,$0F,$0F,$0F,$0F
    db $0A,$0F,$0A,$0F,$0F,$0F,$0F,$0F,$01,$0A,$0F,$0F,$0F,$0F
    db $0F,$0F,$0F,$0F,$0F,$0F,$0F,$0F,$01,$0A,$0F,$0F,$0F,$0F

X_X:
	ret












