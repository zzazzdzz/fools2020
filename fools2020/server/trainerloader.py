import glob
import configparser

import resources
import items

TRAINER_PATH = "../trainers/"

def find_trainer_file(idx):
    candidates = glob.glob(TRAINER_PATH + "%.4x*.txt" % idx)
    if len(candidates) > 1:
        raise RuntimeError("more than 1 trainer with specific identifier?")
    if not candidates:
        return TRAINER_PATH + "0000.txt"
    return candidates[0]

def load_trainer(identifier):
    print(identifier)
    fname = find_trainer_file(identifier)
    config = configparser.ConfigParser()
    config.read(fname)
    obj = {
        "species": config["Trainer"]["MonSpecies"],
        "mon_name": resources.MON_DATA[config["Trainer"]["MonSpecies"]]["display_name"],
        "name": config["Trainer"]["Name"],
        "class_id": eval("resources.%s" % config["Trainer"]["Class"]),
        "bp_reward": int(config["Trainer"]["RewardBP"]),
        "credits_reward": int(config["Trainer"]["RewardCredits"]),
        "tactics": dict(config["Tactics"]),
    }
    l_moves = []
    if config["Moveset"]["Move1"] != ".":
        l_moves.append(config["Moveset"]["Move1"])
    if config["Moveset"]["Move2"] != ".":
        l_moves.append(config["Moveset"]["Move2"])
    if config["Moveset"]["Move3"] != ".":
        l_moves.append(config["Moveset"]["Move3"])
    if config["Moveset"]["Move4"] != ".":
        l_moves.append(config["Moveset"]["Move4"])
    l_items = []
    for i in range(1, 9):
        l_items.append(eval("items.%s" % config["Inventory"]["Slot%i" % i]))
    obj["moves"] = l_moves
    obj["items"] = l_items
    return obj