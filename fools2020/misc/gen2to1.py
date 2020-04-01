
with open('dueltheme1.asm', 'r') as fp:
    lines = [i for i in fp.readlines()]

intensity = 0
octave = 0

labels = {}
it = 0
for i in lines:
    i = i.strip()
    if i:
        if i[0] == '.' or i[-1] == ':':
            labels[i.replace(":","")] = it
    it += 1

ret = [-1]
callid = [1]

line = labels['Music_TCGDuelTheme1_Ch3'] - 1

# print(labels)

result = []

while 1:
    # print("%i," % line, end='')
    r = lines[line].strip().split(" ")
    if not r[0]:
        line += 1
        continue
    if r[0] == 'notetype0':
        result.append(" notetype %s, $a, 11" % r[1])
        line += 1
    elif r[0] == 'notetype1':
        intensity = (intensity % 16) + int(r[1])*16
        # result.append(" intensity %i" % intensity)
        line += 1
    elif r[0] == 'notetype2':
        intensity = (intensity // 16) + int(r[1])
        # result.append(" intensity %i" % intensity)
        line += 1
    elif r[0] == 'octave':
        #if len(r) > 2 and r[2] == ';r' and octave != int(r[1]):
        #    raise RuntimeError("inconsistent octave %i - %i != %i" % (line, int(r[1]), octave))
        octave = int(r[1])
        result.append(" octave %i" % octave)
        line += 1
    elif r[0] == 'inc_octave':
        octave += 1
        result.append(" octave %i ;i" % octave)
        line += 1
    elif r[0] == 'dec_octave':
        octave -= 1
        result.append(" octave %i ;d" % octave)
        line += 1
    elif r[0] == 'note':
        if "__" in r[1]:
            r[1] = "rest"
        result.append(" %s %s" % (r[1].replace(",",""), r[2]))
        line += 1
    elif r[0] == 'callchannel':
        ret.append(line+1)
        callid.append(line+1)
        result.append("; lbl %s" % r[1])
        line = labels[r[1]]
    elif r[0] == 'loopchannel':
        # line = labels[r[1]]
        result.append(" " + " ".join(r) + "_%i" % callid[-1])
        line += 1
    elif r[0] == 'endchannel':
        line = ret.pop()
        callid.pop()
        if line == -1:
            # print("finish")
            result.append(" endchannel")
            break
    elif r[0][-1] == ':':
        line += 1
    elif r[0][0] == '.':
        result.append(" ".join(r) + "_%i" % callid[-1])
        line += 1
    elif r[0] == 'dutycycle':
        result.append(" duty %s" % r[1])
        line += 1
    elif r[0] == 'vibrato':
        line += 1
    elif r[0] == 'rept':
        result.append(" ".join(r))
        line += 1
    elif r[0] == 'endr':
        result.append(" ".join(r))
        line += 1
    else:
        print("?????? %s" % r[0])
        result.append(" ".join(r))
        line += 1

print("\n".join(result))