
table = {
    'e': '0000',
    't': '0001',
    'a': '0010',
    'o': '0011',
    'i': '0100',
    'n': '0101',
    's': '0110',
    'r': '0111',
    'h': '1000',
    'l': '1001',
    'd': '1010',
    'c': '1011',
    ' ': '1100',
    'm': '11100000',
    'f': '11100001',
    'p': '11100010',
    'g': '11100011',
    'w': '11100100',
    'y': '11100101',
    'b': '11100110',
    'v': '11100111',
    'k': '11101000',
    'x': '11101001',
    'j': '11101010',
    'q': '11101011',
    'z': '11101100',
    'u': '11101101',
    '!': '11101110',
    '?': '11101111',
    '1': '11110000',
    '2': '11110001',
    '3': '11110010',
    '4': '11110011',
    '5': '11110100',
    '6': '11110101',
    '7': '11110110',
    '8': '11110111',
    '0': '11111000',
    ',': '11111001',
    '.': '11111010',
    '[RA]': '11111011',
    '[NL]': '11111100',
    '[SC]': '11111101',
    '[CL]': '11111110',
    '[ED]': '11111111',
    ':': '111110110001',
    '9': '111110110010'
}

for i in 'abcdefghijklmnopqrstuvwxyz':
    table[i.upper()] = '1101' + table[i]

s = "Please configure your server connection now. When everything is ready, press the A button."
bitstream = ""

for i in s:
    bitstream += table[i]

if len(bitstream) % 8 != 0:
    bitstream += '1111'

encoded_bytes = [int(bitstream[i:i+8],2) for i in range(0, len(bitstream), 8)]

print("normal length: %i" % len(s))
print("encoded: %.2f" % (len(bitstream)/8))

print(encoded_bytes)