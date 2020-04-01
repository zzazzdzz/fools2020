SECTION "XXX", ROM0[$B800]

X_Header:
    hdr_tileset         8
    hdr_dimensions      4, 4
    hdr_palette         $00
    hdr_music           MUSIC_CELADON, AUDIO_1
    hdr_connection      NORTH, $0000, 0, 0
    hdr_connection      SOUTH, $0000, 0, 0
    hdr_connection      WEST,  $0000, 0, 0
    hdr_connection      EAST,  $0000, 0, 0
    
X_Objects:
    hdr_border          $0A
    hdr_warp_count      2
    hdr_warp            4, 7, 5, 2, $0101
    hdr_warp            5, 7, 5, 2, $0101
    hdr_sign_count      0
    hdr_object_count    1
    hdr_object          SPRITE_DAISY, 5, 3, STAY, NONE, $01

X_RAMScript:
    hdr_textptrs        $fe11
    rs_end

X_Blocks:
    db $0E,$0E,$0E,$0E
    db $0F,$01,$02,$0F
    db $0F,$0C,$0D,$0F
    db $0F,$0F,$0B,$0F

X_X:
	ret






















