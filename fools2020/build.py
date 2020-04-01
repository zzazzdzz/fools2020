import os
import sys

try:
    import rgbbin.objfile
except:
    print("rgbbin is not installed!")
    print("please place it in python path, or put it in the build script's directory.")
    sys.exit(1)

def dump_rgbds_object_file(objname):
    with rgbbin.objfile.ObjectFile(objname) as obj:
        obj.parse_all()
        for section in obj.sections:
            filename = "bin/" + section['name'] + ".bin"
            with open(filename, "wb") as f:
                f.write(section['data'])

with open("base.sav", "rb") as fp:
    save = bytearray(fp.read())

def insert_at(offset, data):
    global save
    for i in range(0, len(data)):
        save[offset + i] = data[i]

print("compiling...")
ret = os.system("rgbasm -o bin/main.obj main.asm")
if ret != 0:
    raise RuntimeError("command not completed successfully")

print("extracting sections...")
dump_rgbds_object_file("bin/main.obj")

print("creating save data...")

with open('bin/SRA2.bin', 'rb') as f:
    sra2 = f.read()
with open('bin/SRA3.bin', 'rb') as f:
    sra3 = f.read()
with open('bin/WRAM.bin', 'rb') as f:
    wram = f.read()

sra2_sz = 0x2000
sra3_sz = 0x2000
wram_sz = 0x400

print("free space report:")
print("sra2: %4i/%4i / %.2f%%" % (len(sra2), sra2_sz, (len(sra2)/sra2_sz)*100))
print("sra3: %4i/%4i / %.2f%%" % (len(sra3), sra3_sz, (len(sra3)/sra3_sz)*100))
print("wram: %4i/%4i / %.2f%%" % (len(wram), wram_sz, (len(wram)/wram_sz)*100))

if len(sra2) > sra2_sz:
    raise RuntimeError("sram2 is overfilled")
if len(sra3) > sra3_sz:
    raise RuntimeError("sram3 is overfilled")
if len(wram) > wram_sz:
    raise RuntimeError("wram is overfilled")

insert_at(0x4000, sra2)
insert_at(0x6000, sra3)
insert_at(0x30c0, wram)

checksum = 0
for i in range(0x2598, 0x3523):
    checksum += save[i]
checksum %= 256
checksum ^= 0xff
insert_at(0x3523, [checksum])

checksum = 0x55
for i in range(0x4001, 0x6000):
    checksum ^= save[i]
    checksum += 1
    checksum %= 256
insert_at(0x4000, [checksum])

checksum = 0x55
for i in range(0x6001, 0x8000):
    checksum ^= save[i]
    checksum += 1
    checksum %= 256
insert_at(0x6000, [checksum])

print("writing save...")
with open('fools.sav', 'wb') as fp:
    fp.write(save)

print("writing bgb savestate...")

source = r'W:\bgb\red.sn3'
target = r'W:\bgb\red.sn2'

print("creating bgb state to %s" % target)

save_raw = save
with open(source, 'rb') as fp:
    save = bytearray(fp.read())
mark = b'SRAM\x00\x00\x80\x00\x00'
sram_data_at = save.index(mark) + len(mark)
insert_at(sram_data_at, save_raw[0:0x8000])
with open(target, 'wb') as fp:
    fp.write(save)
