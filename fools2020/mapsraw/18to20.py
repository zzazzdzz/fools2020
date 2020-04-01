import sys
import configparser

MAP_PATH = "../maps/"

def hint(x):
    if x.startswith("$"):
        return int("%s" % x[1:], 16)
    if x.startswith("0x"):
        return int("%s" % x[2:], 16)
    return int(x)

tileset_consts = {
    "OVERWORLD": 0,
    "REDS_HOUSE_1": 1,
    "MART": 2,
    "FOREST": 3,
    "REDS_HOUSE_2": 4,
    "DOJO": 5,
    "POKECENTER": 6,
    "GYM": 7,
    "HOUSE": 8,
    "FOREST_GATE": 9,
    "MUSEUM": 10,
    "UNDERGROUND": 11,
    "GATE": 12,
    "SHIP": 13,
    "SHIP_PORT": 14,
    "CEMETERY": 15,
    "INTERIOR": 16,
    "CAVERN": 17,
    "LOBBY": 18,
    "MANSION": 19,
    "LAB": 20,
    "CLUB": 21,
    "FACILITY": 22,
    "PLATEAU": 23
}
tileset_consts = {tileset_consts[x]: x for x in tileset_consts.keys()}

pal_consts = {
    "PAL_ROUTE": 0x00,
    "PAL_PALLET": 0x01,
    "PAL_VIRIDIAN": 0x02,
    "PAL_PEWTER": 0x03,
    "PAL_CERULEAN": 0x04,
    "PAL_LAVENDER": 0x05,
    "PAL_VERMILION": 0x06,
    "PAL_CELADON": 0x07,
    "PAL_FUCHSIA": 0x08,
    "PAL_CINNABAR": 0x09,
    "PAL_INDIGO": 0x0A,
    "PAL_SAFFRON": 0x0B
}
pal_consts = {pal_consts[x]: x for x in pal_consts.keys()}

print("18to20 -- fools2018 to fools2020 map converter")

fname = sys.argv[1]

identifier = "0x%s" % fname.split(".")[0].split("_")[0]
config = configparser.ConfigParser()
config["MapHeader"] = {}
config["MapHeader"]["Identifier"] = identifier
config["Connections"] = {}

curwarp = 0
cursign = 0
curobj = 0

blocks = []

with open(fname, "r") as fp:
    for i in fp.readlines():
        if "hdr_tileset" in i:
            config["MapHeader"]["Tileset"] = tileset_consts[hint(i.split("  ")[-1].strip())]
        if "hdr_dimensions" in i:
            w, h = [hint(x.strip()) for x in i.split("  ")[-1].strip().split(",")]
            config["MapHeader"]["Width"] = str(w)
            config["MapHeader"]["Height"] = str(h)
        if "hdr_palette" in i:
            config["MapHeader"]["Palette"] = str(pal_consts[hint(i.split("  ")[-1].strip())])
        if "hdr_music" in i:
            musicid, musicbank = [x.strip() for x in i.split("  ")[-1].strip().split(",")]
            config["MapHeader"]["MusicID"] = str(musicid)
            config["MapHeader"]["MusicBank"] = str(musicbank)
        if "hdr_connection      NORTH, " in i:
            i = i.replace("hdr_connection      NORTH, ","").strip()
            config["Connections"]["North"] = i.replace("$", "0x")
        if "hdr_connection      SOUTH, " in i:
            i = i.replace("hdr_connection      SOUTH, ","").strip()
            config["Connections"]["South"] = i.replace("$", "0x")
        if "hdr_connection      WEST,  " in i:
            i = i.replace("hdr_connection      WEST,  ","").strip()
            config["Connections"]["West"] = i.replace("$", "0x")
        if "hdr_connection      EAST,  " in i:
            i = i.replace("hdr_connection      EAST,  ","").strip()
            config["Connections"]["East"] = i.replace("$", "0x")
        if "hdr_border" in i:
            config["MapHeader"]["BorderBlock"] = str(hint(i.split("  ")[-1]))
        if "hdr_textptrs" in i:
            config["TextPointers"] = {}
            numptrs = 1
            d = i.split("  ")[-1].strip().split(",")
            for xx in d:
                config["TextPointers"]["Text%i" % numptrs] = xx.replace("$", "0x")
                numptrs += 1
        if "hdr_warp " in i:
            wx, wy, tx, ty, tm = [x.strip().replace("$","0x") for x in i.split("  ")[-1].strip().split(",")]
            config["Warp_%i" % curwarp] = {}
            config["Warp_%i" % curwarp]["X"] = wx
            config["Warp_%i" % curwarp]["Y"] = wy
            config["Warp_%i" % curwarp]["TargetX"] = tx
            config["Warp_%i" % curwarp]["TargetY"] = ty
            config["Warp_%i" % curwarp]["ConnectedMapID"] = tm
            curwarp += 1
        if "hdr_signpost " in i:
            wx, wy, ti = [x.strip().replace("$","0x") for x in i.split("  ")[-1].strip().split(",")]
            config["Sign_%i" % cursign] = {}
            config["Sign_%i" % cursign]["X"] = wx
            config["Sign_%i" % cursign]["Y"] = wy
            config["Sign_%i" % cursign]["TextID"] = ti
            cursign += 1
        if "hdr_object " in i:
            pid, wx, wy, mov1, mov2, ti = [x.strip().replace("$","0x") for x in i.split("  ")[-1].strip().split(",")]
            config["Object_%i" % curobj] = {}
            config["Object_%i" % curobj]["PictureID"] = pid
            config["Object_%i" % curobj]["X"] = wx
            config["Object_%i" % curobj]["Y"] = wy
            config["Object_%i" % curobj]["Movement"] = mov1
            config["Object_%i" % curobj]["MovementPattern"] = mov2
            config["Object_%i" % curobj]["TextID"] = ti
            curobj += 1
        if "db " in i:
            row = i.strip().replace("db ","").split(",")
            for x in row:
                blocks.append(hint(x))

config["Sources"] = {}
config["Sources"]["Blocks"] = fname.replace(".asm",".blk")
config["Sources"]["ConnectionPreview"] = fname.replace(".asm",".rs")

with open(MAP_PATH + fname.replace(".asm",".blk"), 'wb') as f:
    f.write(bytes(blocks))

with open(MAP_PATH + fname.replace(".asm",".map"), 'w') as configfile:
    configfile.write("; automatically created with 18to20\n\n")
    config.write(configfile)
