import glob
import random

from util import const_int, lobyte, hibyte, parse_textbox
from copy import deepcopy

SCRIPT_PATH = "../scripts/"
SCRIPT_BASE = 0xa5a0

commands = {
    "textbox": (0x01, 2),
    "showtext": (0x01, 2),
    "yesno": (0x02,),
    "iftrue": (0x03, 2),
    "end": (0x04,),
    "callscript": (0x05, 2),
    "waitbutton": (0x06,),
    "startbattle": (0x07, 2),
    "closetext": (0x08,),
    "delay": (0x09, 1),
    "opentext": (0x0a,),
}

def find_script_file(idx):
    candidates = glob.glob(SCRIPT_PATH + "%.4x*.txt" % idx)
    if len(candidates) > 1:
        raise RuntimeError("more than 1 map with specific identifier?")
    if not candidates:
        return SCRIPT_PATH + "0000.txt"
    return candidates[0]

SAMPLE_PLAYER = {
    "inventory": {"ULTIMATE_BEPIS": 1},
    "events": ["TEST_EVENT"],
    "fun": 123
}

def load_script(identifier, player_data=SAMPLE_PLAYER):
    fname = find_script_file(identifier)
    out = []
    symbols = {"SCRIPT_ID": identifier}
    current_offset = 0
    mode = "script"
    cur_txt = []
    filtered_lines = []
    ignore = False
    depth = 0
    with open(fname, "r") as fp:
        lines = [x.replace("%SCRIPT_ID%", "%.4X" % identifier) for x in fp.readlines()]
        for l in lines:
            args = l.strip().split(" ")
            if args[-1].endswith("{"):
                depth += 1
                if args[0] == "cond":
                    inv = False
                    if args[1].startswith("!"):
                        args[1] = args[1][1:]
                        inv = True
                    if args[1] == "event":
                        ignore = args[2] in player_data["events"]
                    if args[1] == "item":
                        ignore = args[2] in player_data["inventory"]
                    if args[1] == "fun":
                        ignore = int(args[2]) < player_data["fun"] < int(args[3])
                    if args[1] == "random":
                        ignore = random.random() < (float(args[2])/100)
                    if not inv:
                        ignore = not ignore
                    mode = "cond"
                    continue
            elif args[0].endswith("}"):
                depth -= 1
                if depth == 0 and mode in ("cond", "effects"):
                    ignore = False
                    mode = "script"
                    continue
            if not ignore:
                filtered_lines.append(l)
        lines = filtered_lines
        for l in lines:
            args = l.strip().split(" ")
            if mode == "script":
                if args[0].endswith(":"):
                    symbols[args[0].replace(":","")] = SCRIPT_BASE + current_offset
                elif args[-1].endswith("{"):
                    mode = args[0]
                    cur_txt = []
                    symbols[args[1]] = SCRIPT_BASE + current_offset
                elif args[-1].endswith("{"):
                    continue
                elif args[0] == "":
                    continue
                else:
                    if args[0] not in commands:
                        raise RuntimeError("undefined script cmd %s" % args[0])
                    current_offset += sum(commands[args[0]][1:]) + 1
            elif mode == "effects":
                if args[0] == "setevent":
                    player_data["events"].append(args[1])
                if args[0] == "clearevent":
                    if args[1] in player_data["events"]:
                        player_data["events"].remove(args[1])
                if args[0] == "giveitem":
                    if args[1] not in player_data["inventory"]:
                        player_data["inventory"][args[1]] = 0
                    player_data["inventory"][args[1]] += 1
                if args[0] == "takeitem":
                    if args[1] in player_data["inventory"]:
                        player_data["inventory"][args[1]] -= 1
                        if player_data["inventory"][args[1]] <= 0:
                            del player_data["inventory"][args[1]]
                if args[0] == "newfun":
                    player_data["fun"] = random.randrange(0, 255)
                if args[0].endswith("}"):
                    mode = "script"
            elif mode == "textbox":
                if args[0].endswith("}"):
                    mode = "script"
                    current_offset += len(parse_textbox(cur_txt))
                else:
                    cur_txt.append(l.strip())
            else:
                raise RuntimeError("unknown scripting mode %s" % mode)
        for l in lines:
            args = l.strip().split(" ")
            # print(args, mode)
            if mode == "script":
                if args[0].endswith(":") or args[0] == "":
                    continue
                elif args[-1].endswith("{"):
                    mode = args[0]
                    cur_txt = []
                else:
                    if args[0] not in commands:
                        raise RuntimeError("undefined script cmd %s" % args[0])
                    cmd = commands[args[0]]
                    out.append(cmd[0])
                    for i in range(1, len(args)):
                        if i >= len(cmd):
                            raise RuntimeError("extra argument in '%s'" % l)
                        if args[i] in symbols:
                            args[i] = symbols[args[i]]
                        if cmd[i] == 1:
                            out.append(lobyte(const_int(args[i])))
                        elif cmd[i] == 2:
                            out.append(lobyte(const_int(args[i])))
                            out.append(hibyte(const_int(args[i])))
                        else:
                            raise RuntimeError("unsupported size %i" % cmd[i])
            elif mode == "effects":
                if args[0].endswith("}"):
                    mode = "script"
            elif mode == "textbox":
                if args[0].endswith("}"):
                    mode = "script"
                    out += parse_textbox(cur_txt)
                else:
                    cur_txt.append(l.strip())
            else:
                raise RuntimeError("unknown scripting mode %s" % mode)
    print(out)
    return out

if __name__ == "__main__":
    print(load_script(0xFEA1))