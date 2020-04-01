SECTION "XXX", ROM0[$B800]

X_Header:
    hdr_tileset         0
    hdr_dimensions      6, 6
    hdr_palette         $00
    hdr_music           MUSIC_CREDITS, AUDIO_3
    hdr_connection      NORTH, $0101, 0, 11
    hdr_connection      SOUTH, $0101, 0, 0
    hdr_connection      WEST,  $0101, 0, 11
    hdr_connection      EAST,  $0101, 0, 0
    
X_Objects:
    hdr_border          $0F
    hdr_warp_count      1
    hdr_warp            5, 1, 4, 7, $0169
    hdr_sign_count      2
    hdr_signpost        7, 4, $02
    hdr_signpost        4, 4, $03
    hdr_object_count    1
    hdr_object          SPRITE_LASS, 7, 2, STAY, NONE, $01

X_RAMScript:
    hdr_textptrs        $fea0,$fea1,$fea2
    rs_end

X_Blocks:
    db $0F,$0F,$02,$03,$0F,$0F
    db $0F,$0F,$01,$01,$0F,$0F
    db $0A,$0A,$0A,$0A,$0A,$0A
    db $0A,$0A,$0A,$0A,$0A,$0A
    db $0F,$0F,$0F,$0F,$0F,$0F
    db $0F,$0F,$0F,$0F,$0F,$0F

X_X:
	ret
























































