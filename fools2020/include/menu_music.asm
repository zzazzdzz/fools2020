
Music_InventoryScreen_Pointers:
    dw $c9e0 + (Music_InventoryScreen_Ch0 - Music_InventoryScreen)
    dw $c9e0 + (Music_InventoryScreen_Ch1 - Music_InventoryScreen)
    dw $c9e0 + (Music_InventoryScreen_Ch2 - Music_InventoryScreen)
    dw $c9e0 + (Music_InventoryScreen_Ch3 - Music_InventoryScreen)

Music_InventoryScreen:

Ch1_sub_0:
	G_ 2
	B_ 2
	octave 4
	D_ 2
	F# 2
	D_ 2
	octave 3
	B_ 2
	G_ 2
	B_ 2
	octave 4
	D_ 2
	F# 2
	D_ 2
	octave 3
	A# 2
	G_ 2
	A# 2
	octave 4
	D_ 2
	F# 2
	D_ 2
	octave 3
	A# 2
	G_ 2
	A# 2
	octave 4
	D_ 2
	F# 2
	D_ 2
	octave 3
	A_ 2
	F# 2
	A_ 2
	octave 4
	C# 2
	E_ 2
	C# 2
	endchannel
Music_InventoryScreen_Ch0:
	tempo 126
	vibrato 0, 0, 0
	duty 3
	notetype 12, 8, 4
	octave 3
	A_ 5
	rest 1
	G_ 2
	F# 2
	G_ 2
	A_ 4
	octave 4
	D_ 5
	rest 1
	octave 3
	A_ 2
	octave 4
	C# 4
	octave 3
	B_ 6
	A# 2
	B_ 12
	G_ 6
	F# 2
	E_ 2
	F# 2
	G_ 4
	octave 4
	C# 6
	octave 3
	B_ 2
	A_ 6
	G# 2
	A_ 2
	B_ 2
	A_ 12
	A_ 6
	G_ 2
	F# 2
	G_ 2
	A_ 4
	octave 4
	D_ 6
	C# 2
	E_ 6
	D_ 2
	C# 2
	D_ 2
	octave 3
	B_ 12
	octave 4
	G_ 5
	rest 1
	F# 2
	E_ 4
	C# 4
	D_ 4
	E_ 4
	notetype 15, 8, 4
	D_ 16
	notetype 12, 8, 4
	rest 4
	octave 3
	B_ 2
	callchannel $c9e0 + (Ch1_sub_0 - Music_InventoryScreen)
	octave 3
	A_ 2
	F# 2
	A_ 2
	octave 4
	C# 2
	E_ 2
	C# 2
	octave 3
	G_ 2
	E_ 2
	G_ 2
	B_ 2
	octave 4
	E_ 2
	D_ 2
	C# 2
	D_ 2
	octave 3
	B_ 2
	octave 4
	C# 2
	octave 3
	A_ 2
	G_ 2
	B_ 2
	callchannel $c9e0 + (Ch1_sub_0 - Music_InventoryScreen)
	D# 2
	octave 3
	B_ 2
	octave 4
	D# 2
	F# 2
	A_ 2
	F# 2
	G_ 2
	A_ 2
	F# 2
	G_ 2
	E_ 2
	F# 2
	D_ 2
	E_ 2
	C# 2
	D_ 2
	octave 3
	B_ 2
	octave 4
	C# 2
	loopchannel 0, $c9e0 + (Music_InventoryScreen_Ch0 - Music_InventoryScreen)
Ch3_sub_0:
	G_ 4
	B_ 4
	octave 3
	D_ 4
	octave 2
	G_ 4
	B_ 4
	octave 3
	D_ 4
	octave 2
	G_ 4
	A# 4
	octave 3
	D_ 4
	octave 2
	G_ 4
	A# 4
	octave 3
	D_ 4
	octave 2
	F# 8
	A_ 2
	F# 2
	A_ 4
	G_ 4
	F# 4
	E_ 8
	F# 2
	G_ 2
	A_ 4
	G_ 4
	E_ 4
	endchannel
Music_InventoryScreen_Ch2:
	vibrato 0, 0, 0
	notetype 12, $a, 1
	octave 2
	D_ 12
	D_ 12
	F# 12
	B_ 4
	A_ 4
	F# 4
	E_ 12
	G_ 12
	D_ 12
	A_ 4
	G_ 4
	E_ 4
	D_ 12
	D_ 12
	F# 12
	B_ 4
	A_ 4
	F# 4
	E_ 12
	A_ 12
	D_ 12
	octave 3
	C_ 4
	octave 2
	B_ 4
	A_ 4
	callchannel $c9e0 + (Ch3_sub_0 - Music_InventoryScreen)
	callchannel $c9e0 + (Ch3_sub_0 - Music_InventoryScreen)
	loopchannel 0, $c9e0 + (Music_InventoryScreen_Ch2 - Music_InventoryScreen)
Ch2_sub_0:
	G_ 2
	B_ 2
	octave 3
	D_ 2
	F# 2
	D_ 2
	octave 2
	B_ 2
	G_ 2
	B_ 2
	octave 3
	D_ 2
	F# 2
	D_ 2
	octave 2
	A# 2
	G_ 2
	A# 2
	octave 3
	D_ 2
	F# 2
	D_ 2
	octave 2
	A# 2
	G_ 2
	A# 2
	octave 3
	D_ 2
	F# 2
	D_ 2
	octave 2
	A_ 2
	F# 2
	A_ 2
	octave 3
	C# 2
	E_ 2
	C# 2
	endchannel
Ch2_sub_1:
	F# 2
	A_ 2
	octave 3
	D_ 2
	octave 2
	A_ 2
	octave 3
	D_ 2
	octave 2
	A_ 2
Music_InventoryScreen_Ch3:
	endchannel
Ch2_sub_2:
	C# 2
	octave 2
	A# 2
	octave 3
	C# 2
	octave 2
	A# 2
	F# 2
	B_ 2
	octave 3
	D# 2
	octave 2
	B_ 2
	octave 3
	D# 2
	octave 2
	B_ 2
	E_ 2
	G_ 2
	B_ 2
	G_ 2
	B_ 2
	G_ 2
	E_ 2
	A_ 2
	octave 3
	C# 2
	octave 2
	A_ 2
	octave 3
	C# 2
	octave 2
	endchannel
Music_InventoryScreen_Ch1:
	vibrato 0, 0, 0
	duty 3
	notetype 12, 5, 4
	octave 2
	callchannel $c9e0 + (Ch2_sub_1 - Music_InventoryScreen)
	callchannel $c9e0 + (Ch2_sub_1 - Music_InventoryScreen)
	F# 2
	A# 2
	octave 3
	callchannel $c9e0 + (Ch2_sub_2 - Music_InventoryScreen)
	A_ 2
	callchannel $c9e0 + (Ch2_sub_1 - Music_InventoryScreen)
	octave 3
	D_ 2
	octave 2
	A_ 2
	octave 3
	C# 2
	octave 2
	A_ 2
	octave 3
	C# 2
	octave 2
	A_ 2
	callchannel $c9e0 + (Ch2_sub_1 - Music_InventoryScreen)
	callchannel $c9e0 + (Ch2_sub_1 - Music_InventoryScreen)
	F# 2
	A_ 2
	octave 3
	callchannel $c9e0 + (Ch2_sub_2 - Music_InventoryScreen)
	G_ 2
	callchannel $c9e0 + (Ch2_sub_1 - Music_InventoryScreen)
	F# 2
	A_ 2
	octave 3
	C_ 2
	octave 2
	A_ 2
	octave 3
	C_ 2
	octave 2
	A_ 2
	B_ 2
	callchannel $c9e0 + (Ch2_sub_0 - Music_InventoryScreen)
	octave 2
	A_ 2
	F# 2
	A_ 2
	octave 3
	C# 2
	E_ 2
	C# 2
	octave 2
	G_ 2
	E_ 2
	G_ 2
	B_ 2
	octave 3
	E_ 2
	D_ 2
	C# 2
	D_ 2
	octave 2
	B_ 2
	octave 3
	C# 2
	octave 2
	A_ 2
	G_ 2
	B_ 2
	callchannel $c9e0 + (Ch2_sub_0 - Music_InventoryScreen)
	D# 2
	octave 2
	B_ 2
	octave 3
	D# 2
	F# 2
	A_ 2
	F# 2
	G_ 2
	A_ 2
	F# 2
	G_ 2
	E_ 2
	F# 2
	D_ 2
	E_ 2
	C# 2
	D_ 2
	octave 2
	B_ 2
	octave 3
	C# 2
	loopchannel 0, $c9e0 + (Music_InventoryScreen_Ch1 - Music_InventoryScreen)