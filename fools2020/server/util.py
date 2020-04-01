import hashlib
import binascii
import os

import consts

def get_raw_post(environ):
    data_len = int(environ.get('CONTENT_LENGTH', 0))
    data = environ['wsgi.input'].read(data_len)
    return data

def gen_keybytes(key, sz):
    varA = key % 256
    varB = key // 256
    result = []
    for i in range(0, sz):
        origA = varA
        origB = varB
        newA = origB ^ origA
        newA = ((newA << 1) | (newA >> 7)) % 256
        newB = ((origA + origA) % 256) ^ origB
        varA = newA
        varB = newB
        result.append(varB)
    return result

def gen_checksum(data):
    checksum_l = 0
    checksum_h = 0
    for i in data:
        checksum_h += i
        checksum_h %= 255
        checksum_l += checksum_h
        checksum_l %= 255
    return checksum_h * 256 + checksum_l

def const_int(x):
    if type(x) is int:
        return x
    if not x:
        return 0
    if x.startswith("$"):
        return int("%s" % x[1:], 16)
    if x.startswith("0x"):
        return int("%s" % x[2:], 16)
    if x in consts.CONSTS:
        return consts.CONSTS[x]
    return int(x)

def lobyte(x):
    return x & 0xff

def hibyte(x):
    return (x >> 8) & 0xff
    
CHARMAP_FILE = "../include/charmap.asm"
charmap = {}

with open(CHARMAP_FILE, "r") as f:
    for i in f.readlines():
        if i.startswith("charmap"):
            d = [x.strip() for x in i[8:].split(", ")]
            charmap[d[0][1:-1].replace("\\", "")] = const_int(d[1])

def parse_textbox(txt):
    out = []
    line_no = 0
    c = ""
    for line in txt:
        if line == "":
            out.append(0xf3)
            line_no = -1
        if line_no == 1:
            out.append(0xf2)
        if line_no > 1:
            out.append(0xf1)
        for char in line:
            c += char
            if c in charmap:
                out.append(charmap[c])
                c = ""
        line_no += 1
    if c:
        raise RuntimeError("undefined character: %s" % c[0])
    out.append(0)
    return out

def parse_text(txt, pad=0):
    out = []
    c = ""
    for char in txt:
        c += char
        if c in charmap:
            out.append(charmap[c])
            c = ""
    if c:
        raise RuntimeError("undefined character: %s" % c[0])
    out.append(0)
    if pad:
        while len(out) < pad:
            out.append(0)
        if len(out) > pad:
            raise RuntimeError("text exceeds padding of %i" % pad)
    return out

def bcd(x):
    x16 = int(str(x), 16)
    x16l = x16 % 256
    x16h = x16 // 256
    return (x16h, x16l)

# yep this hashing is shit :/
def password_hash(x):
    return hashlib.sha256(bytes(x, 'utf-8') + b"ew90v9mwc0mei0wfojief-d0wfjiwefew").hexdigest()

def new_session_key():
    return binascii.hexlify(os.urandom(64)).decode('ascii')