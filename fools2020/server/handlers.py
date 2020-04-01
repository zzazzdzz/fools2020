import random
import json

import maploader
import scriptloader
import trainerloader
import battle
import util
import resources
import items
import storage

def handle_command(data, player_data):
    if data[0] in handlers:
        return handlers[data[0]](data[1:], player_data)
    else:
        raise RuntimeError("not a valid packet ID: %.2x" % data[0])

def hello_packet_handler(data, player_data):
    if data[0] == 0x10:
        return bytearray(b"\x01")
    else:
        return bytearray(b"\x02")

def loadmap_packet_handler(data, player_data):
    return bytearray(maploader.load_map(data[1]*256 + data[0], player_data))

def script_packet_handler(data, player_data):
    return bytearray(scriptloader.load_script(data[1]*256 + data[0], player_data))

def battle_packet_handler(data, player_data):
    if data[0] == 1:
        q = storage.sql("select battle_data from last_battle where id=?", (player_data["id"],))
        return bytearray(q[0]["battle_data"])

    print(data)
    rnd_items_1 = []
    rnd_items_2 = []
    for i in range(0,8):
        rnd_items_1.append(random.choice(list(items.ITEM_CLASSES.keys())))
    for i in range(0,8):
        rnd_items_2.append(random.choice(list(items.ITEM_CLASSES.keys())))
    rnd_state = {"species": random.choice(list(resources.MON_DATA.keys())), "mon_name": "Shadow", "moves": ["SCRATCH"], "name": "X", "items": rnd_items_1}

    attacking_player = json.loads(player_data["mon"])
    defending_player = trainerloader.load_trainer(data[2]*256 + data[1])

    b = battle.battle(attacking_player, defending_player)

    r = bytearray(
        bytes(defending_player["items"]) + # attacker items
        bytes(attacking_player["items"]) + # defender items
        bytes([defending_player["class_id"]]) + # trainer class id
        bytes(util.bcd(defending_player["bp_reward"])) + # bp reward
        bytes(util.bcd(defending_player["credits_reward"])) + # credit reward
        bytes([resources.MON_DATA[attacking_player["species"]]["mon_numeric_id"]]) + # attacker species id
        bytes([resources.MON_DATA[defending_player["species"]]["mon_numeric_id"]]) + # defender species id
        bytes(util.parse_text(defending_player["name"], 21)) + # defender name
        b.log_bytes() # offset to stringbuf, battle data, stringbuf
    )
    print(r)
    
    storage.sql("""
        update last_battle set battle_data=? where id=?
    """, (r, player_data["id"]))

    return r

def gift_packet_handler(data, player_data):
    r = bytearray(
        b"\x02" +
        bytes(util.parse_text("Star For Effort")) +
        bytes(util.parse_text("Shadowek"))
    )
    print(r)
    return r

handlers = {
    0x88: hello_packet_handler,
    0x90: loadmap_packet_handler,
    0x91: script_packet_handler,
    0x92: battle_packet_handler,
    0x93: gift_packet_handler
}
