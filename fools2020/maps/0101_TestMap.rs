    rs_write_1 $c70c, $03
    rs_write_2 $c717, $02, $01
    rs_write_term  $c723
    db $01,$0a,$0a,$0a,$ff
    rs_fill_byte $0a
    rs_fill_len $c72d, 6
    rs_fill_3 $c739
