import configparser
import glob

from util import const_int, lobyte, hibyte

MAP_PATH = "../maps/"

def find_map_file(idx):
    candidates = glob.glob(MAP_PATH + "%.4x_*.map" % idx)
    if len(candidates) > 1:
        raise RuntimeError("more than 1 map with specific identifier?")
    if not candidates:
        return MAP_PATH + "0000_Null.map"
    return candidates[0]

def load_map(identifier, player_data):
    fname = find_map_file(identifier)
    config = configparser.ConfigParser()
    config.read(fname)
    num_warps = len([i for i in config.sections() if i.startswith("Warp_")])
    num_signs = len([i for i in config.sections() if i.startswith("Sign_")])
    num_objs  = len([i for i in config.sections() if i.startswith("Object_")])
    compiled_warps = []
    compiled_signs = []
    compiled_objs = []
    compiled_connection_data = []
    compiled_textptrs = []
    compiled_blockdata = [0]
    compiled_ramscript = []
    for i in range(0, num_warps):
        compiled_warps += [
            const_int(config["Warp_%i" % i]["Y"]),
            const_int(config["Warp_%i" % i]["X"])
        ]
    for i in range(0, num_warps):
        compiled_warps += [
            const_int(config["Warp_%i" % i]["TargetY"]),
            const_int(config["Warp_%i" % i]["TargetX"]),
            lobyte(const_int(config["Warp_%i" % i]["ConnectedMapID"]))
        ]
    for i in range(0, num_signs):
        compiled_signs += [
            const_int(config["Sign_%i" % i]["Y"]),
            const_int(config["Sign_%i" % i]["X"])
        ]
    for i in range(0, num_signs):
        compiled_signs += [
            const_int(config["Sign_%i" % i]["TextID"])
        ]
    for i in range(0, num_objs):
        compiled_objs += [
            const_int(config["Object_%i" % i]["PictureID"]),
            const_int(config["Object_%i" % i]["Y"]) + 4,
            const_int(config["Object_%i" % i]["X"]) + 4,
            const_int(config["Object_%i" % i]["Movement"])
        ]
    for i in range(0, num_objs):
        compiled_objs += [
            const_int(config["Object_%i" % i]["MovementPattern"]),
            const_int(config["Object_%i" % i]["TextID"])
        ]
    for direction in ("North", "South", "West", "East"):
        if direction not in config["Connections"]:
            continue
        current_conn = config["Connections"][direction].split(",")
        data = [const_int(x.strip()) for x in current_conn]
        compiled_connection_data += [
            lobyte(data[0]),
            hibyte(data[0]),
            data[1],
            data[2]
        ]
    for i in range(0, len(config["TextPointers"])):
        tid = const_int(config["TextPointers"]["Text%i" % (i+1)])
        compiled_textptrs += [
            lobyte(tid),
            hibyte(tid)
        ]
    if "Blocks" in config["Sources"]:
        with open(MAP_PATH + config["Sources"]["Blocks"], "rb") as f:
            compiled_blockdata = list(f.read())
    if "ConnectionPreview" in config["Sources"]:
        with open(MAP_PATH + config["Sources"]["ConnectionPreview"], "r") as f:
            for l in f.readlines():
                compiled_ramscript += parse_ramscript_line(l)
            compiled_ramscript.append(0xff)
    map_data = [
        const_int(config["MapHeader"]["Tileset"]),
        const_int(config["MapHeader"]["Height"]),
        const_int(config["MapHeader"]["Width"]),
        const_int(config["MapHeader"]["BorderBlock"]),
        const_int(config["MapHeader"]["Palette"])
    ]
    map_data += [num_warps] + compiled_warps
    map_data += [num_signs] + compiled_signs
    map_data += [num_objs] + compiled_objs
    map_data += [
        const_int(config["MapHeader"]["MusicID"]),
        const_int(config["MapHeader"]["MusicBank"])
    ]
    map_data += compiled_connection_data + [0xff]
    map_data += compiled_blockdata + [0xff]
    map_data += compiled_textptrs + [0xff]
    map_data += compiled_ramscript
    print(len(map_data))
    return map_data

def parse_ramscript_line(l):
    l_tx = l
    l = [x.strip() for x in l.strip().replace(",","").replace("  "," ").split(" ")]
    try:
        args = [const_int(x) for x in l[1:]]
    except:
        args = []
    if l[0] == "rs_write_1":
        return [
            0x00 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff,
            args[1]
        ]
    if l[0] == "rs_write_2":
        return [
            0x20 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff,
            args[1], args[2]
        ]
    if l[0] == "rs_write_3":
        return [
            0x40 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff,
            args[1], args[2], args[3]
        ]
    if l[0] == "rs_write_term":
        return [
            0x60 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff
        ]
    if l[0] == "rs_fill_2":
        return [
            0x80 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff
        ]
    if l[0] == "rs_fill_3":
        return [
            0xa0 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff
        ]
    if l[0] == "rs_fill_len":
        return [
            0xc0 | ((args[0] >> 8) & 0x1f),
            args[0] & 0xff,
            args[1]
        ]
    if l[0] == "rs_fill_byte":
        return [
            0xe0, args[0]
        ]
    if l[0] == "rs_end":
        return [0xff]
    if l[0] == "db":
        seq = [const_int(x) for x in l_tx.replace("db ","").strip().split(",")]
        return seq
    return []

if __name__ == "__main__":
    load_map("../0101.map")