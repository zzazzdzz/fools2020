import random
import json
from copy import deepcopy

import items
import log
import util
from resources import *

def create_basic_state(mon_id):
    return {
        "mon_id": mon_id,
        "hp": int(MON_DATA[mon_id]["base_stats"][0] * 2),
        "cur_hp": int(MON_DATA[mon_id]["base_stats"][0] * 2),
        "attack": MON_DATA[mon_id]["base_stats"][1],
        "defense": MON_DATA[mon_id]["base_stats"][2],
        "special_attack": MON_DATA[mon_id]["base_stats"][4],
        "special_defense": MON_DATA[mon_id]["base_stats"][5],
        "speed": MON_DATA[mon_id]["base_stats"][3],
        "base_hp": int(MON_DATA[mon_id]["base_stats"][0] * 2),
        "base_attack": MON_DATA[mon_id]["base_stats"][1],
        "base_defense": MON_DATA[mon_id]["base_stats"][2],
        "base_special_attack": MON_DATA[mon_id]["base_stats"][4],
        "base_special_defense": MON_DATA[mon_id]["base_stats"][5],
        "base_speed": MON_DATA[mon_id]["base_stats"][3],
        "types": MON_DATA[mon_id]["types"],
        "status": None,
        "species": MON_DATA[mon_id]["display_name"],
        "name": MON_DATA[mon_id]["display_name"],
        "crit_chance": 5,
        "accuracy": 100,
        "evasion": 100,
        "last_attack_power": 0,
        "items": [items.NONE] * 8,
        "flinching": False,
        "secondary_effect_mult": 1
    }

def create_action_state(attacker, defender):
    return {
        "damage_dealt": 0,
        "attacker": attacker,
        "defender": defender,
        "effective_attack": attacker["attack"],
        "effective_defense": defender["defense"],
        "effective_sp_attack": attacker["special_attack"],
        "effective_sp_defense": defender["special_defense"],
        "effective_accuracy": attacker["accuracy"],
        "effective_evasion": defender["evasion"],
        "effective_crit": attacker["crit_chance"],
        "win": False,
        "missed": False,
        "unavoidable_encounter": True
    }

def effect_normal_hit(move_id, battle_log, action_array):
    # todo
    pass

def effect_paralyze_hit(move_id, battle_log, action_array):
    # todo
    pass

def effect_burn_hit(move_id, battle_log, action_array):
    # todo
    pass

def effect_freeze_hit(move_id, battle_log, action_array):
    # todo
    pass

EFFECT_HANDLERS = {
    "EFFECT_NORMAL_HIT": effect_normal_hit
}

def use_move(move_id, battle_log, action_array):
    attacker = action_array["attacker"]
    defender = action_array["defender"]
    action_array["missed"] = False
    action_array["move_id"] = move_id
    items.predamaged(defender, action_array, battle_log)
    items.moveused(attacker, action_array, battle_log)
    if action_array["missed"]:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_ATTACK_AVOIDED, defender["string_buffer_id"]
        )
        items.evaded(defender, action_array, battle_log)
        items.missed(attacker, action_array, battle_log)
        action_array["damage_dealt"] = 0
        return
    # move accuracy checks
    if random.randrange(0, 100) > MOVE_DATA[move_id]['accuracy']:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_ATTACK_MISSED, attacker["string_buffer_id"]
        )
        items.evaded(defender, action_array, battle_log)
        items.missed(attacker, action_array, battle_log)
        action_array["damage_dealt"] = 0
        return
    # evasion checks
    effective_evasion = min(max(action_array['effective_evasion'] - action_array['effective_accuracy'], 0), 60)
    if random.randrange(0, 100) < effective_evasion:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_ATTACK_AVOIDED, defender["string_buffer_id"]
        )
        items.evaded(defender, action_array, battle_log)
        items.missed(attacker, action_array, battle_log)
        action_array["damage_dealt"] = 0
        return
    action_array["base_damage_start"] = MOVE_DATA[move_id]['power']
    effect_mult = type_effectiveness(MOVE_DATA[move_id]['type'], defender)
    # Possible effectiveness multipliers are 0.5, 2 and 0.05.
    # This means all multipliers above 1 are super effective,
    # below 1 are not very effective, and <= 0.1 - ineffective.
    # However, to avoid float precision issues, the comparison
    # thresholds are set a bit higher or lower.
    if effect_mult > 1.1:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_SUPER_EFFECTIVE
        )
    elif effect_mult < 0.15:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_INEFFECTIVE
        )
    elif effect_mult < 0.9:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_NOT_VERY_EFFECTIVE
        )
    action_array["effect_mult"] = effect_mult
    base_damage = action_array["base_damage_start"]
    if MOVE_DATA[move_id]['type'] in attacker['types']:
        base_damage *= 1.5 # stab
    base_damage *= effect_mult
    base_damage *= random.randrange(90, 105) / 100
    action_array["crit"] = False
    if random.randrange(0, 100) < action_array["effective_crit"]:
        base_damage *= 2
        action_array["crit"] = True
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_CRIT
        )
    action_array["base_damage"] = base_damage
    if MOVE_DATA[move_id]['type'] in PHYSICAL_TYPES:
        move_type = "physical"
    else:
        move_type = "special"
    action_array["move_type"] = move_type
    items.predamage(attacker, action_array, battle_log)
    action_array["damage_dealt"] = damage(action_array, move_type, action_array["base_damage"])
    items.postdamage(attacker, action_array, battle_log)
    items.afterdamaged(defender, action_array, battle_log)
    return

def battle(attacking_player, defending_player):
    attacker = create_basic_state(attacking_player["species"])
    defender = create_basic_state(defending_player["species"])
    attacker["string_buffer_id"] = 0
    defender["string_buffer_id"] = 1
    attacker["moves"] = deepcopy(attacking_player["moves"])
    defender["moves"] = deepcopy(defending_player["moves"])

    defender["items"] = deepcopy(defending_player["items"])
    attacker["items"] = deepcopy(attacking_player["items"])

    battle_log = log.BattleLog()
    battle_log.add_to_stringbuf(attacking_player["mon_name"])
    battle_log.add_to_stringbuf(defending_player["mon_name"])

    turns_passed = 0

    items.load_item_classes(attacker)
    items.apply_combat_stats(attacker)
    items.load_item_classes(defender)
    items.apply_combat_stats(defender)
    attacker["cur_hp"] = attacker["hp"]
    defender["cur_hp"] = defender["hp"]

    permvars = {}
    precombat_state = {
        "attacker_turn": False, "win": False,
        "permvars": permvars,
        "attacker": attacker, "defender": defender,
        "unavoidable_encounter": False
    }

    if attacker['speed'] > defender['speed']:
        precombat_state["attacker_turn"] = True
    elif attacker['speed'] == defender['speed']:
        precombat_state["attacker_turn"] = random.random() > 0.5

    precombat_state["attacker_side"] = True
    items.precombat(attacker, precombat_state, battle_log)
    precombat_state["attacker_side"] = False
    items.precombat(defender, precombat_state, battle_log)

    if precombat_state["win"]:
        battle_log.push(BATTLE_ACTION_FAINT, defender["string_buffer_id"])

    if not precombat_state["attacker_turn"]:
        attacker, defender = defender, attacker

    if not precombat_state["win"]:
        battle_log.push(
            BATTLE_ACTION_MESSAGE,
            MSG_BATTLE_FIRST, attacker["string_buffer_id"]
        )

    while not precombat_state["win"]:
        print("****** %s %i/%i | %s %i/%i" % (attacker["name"], attacker["cur_hp"], attacker["hp"], defender["name"], defender["cur_hp"], defender["hp"]))
        print("%s: sp atk %i / sp def %i / atk %i / def %i " % (attacker["name"], attacker['special_attack'], attacker['special_defense'], attacker['attack'], attacker['defense']))
        print("%s: sp atk %i / sp def %i / atk %i / def %i " % (defender["name"], defender['special_attack'], defender['special_defense'], defender['attack'], defender['defense']))
        #print("%s items: %s" % (attacker["name"], attacker["items"]))
        #print("%s items: %s" % (defender["name"], defender["items"]))
        
        action_array = create_action_state(attacker, defender)
        action_array["permvars"] = permvars

        if attacker["flinching"]:
            battle_log.push(
                BATTLE_ACTION_MESSAGE,
                MSG_BATTLE_FLINCHING, attacker["string_buffer_id"]
            )
            attacker["flinching"] = False
        else:
            move_id = random.choice(attacker["moves"])
            battle_log.push(
                BATTLE_ACTION_MESSAGE,
                MSG_BATTLE_USED, attacker["string_buffer_id"],
                battle_log.get_stringbuf(MOVE_DATA[move_id]['display_name'])
            )
            use_move(move_id, battle_log, action_array)
            if action_array["damage_dealt"] > 0:
                apply_damage(defender, action_array["damage_dealt"], battle_log)
                battle_log.push(
                    BATTLE_ACTION_MESSAGE,
                    MSG_BATTLE_NORMAL_DAMAGE, defender["string_buffer_id"], util.bcd(action_array["damage_dealt"])
                )
                items.realafterdamaged(defender, action_array, battle_log)
            if MOVE_DATA[move_id]['effect'] in EFFECT_HANDLERS:
                EFFECT_HANDLERS[MOVE_DATA[move_id]['effect']](move_id, battle_log, action_array)

        if defender["cur_hp"] == 0:
            battle_log.push(BATTLE_ACTION_FAINT, defender["string_buffer_id"])
            battle_log.push(
                BATTLE_ACTION_MESSAGE,
                MSG_BATTLE_FAINTED, defender["string_buffer_id"]
            )
            break

        items.endstep(attacker, action_array, battle_log)
        if action_array["win"]:
            battle_log.push(BATTLE_ACTION_FAINT, defender["string_buffer_id"])
            break

        turns_passed += 1
        if turns_passed == 10:
            battle_log.push(BATTLE_ACTION_MESSAGE, MSG_BATTLE_TURN_LIMIT_1)
        if turns_passed == 11:
            battle_log.push(BATTLE_ACTION_MESSAGE, MSG_BATTLE_TURN_LIMIT_2)
        if turns_passed == 12:
            battle_log.push(BATTLE_ACTION_MESSAGE, MSG_BATTLE_TURN_LIMIT_3)
        if turns_passed == 13:
            battle_log.push(BATTLE_ACTION_MESSAGE, MSG_BATTLE_SUDDEN_DEATH)
            atk_score = attacker["cur_hp"]
            def_score = defender["cur_hp"]
            atk_score *= defender["hp"]
            def_score *= attacker["hp"]
            if atk_score > def_score:
                apply_damage(defender, 99999, battle_log)
                battle_log.push(BATTLE_ACTION_FAINT, defender["string_buffer_id"])
            else:
                apply_damage(attacker, 99999, battle_log)
                battle_log.push(BATTLE_ACTION_FAINT, attacker["string_buffer_id"])
            break

        attacker, defender = defender, attacker

    return battle_log


'''
print(damage({"effective_attack": 100, "effective_defense": 50}, "physical", 100))
print(damage({"effective_attack": 100, "effective_defense": 100}, "physical", 100))
print(damage({"effective_attack": 100, "effective_defense": 150}, "physical", 100))
print(damage({"effective_attack": 100, "effective_defense": 200}, "physical", 100))
print(damage({"effective_attack": 100, "effective_defense": 250}, "physical", 100))
print(damage({"effective_attack": 100, "effective_defense": 300}, "physical", 100))
'''

if __name__ == "__main__":
    attacking_player = {"species": "CHARMANDER", "mon_name": "Bepis", "moves": ["SCRATCH"], "name": "X", "items": [items.ROWHAMMER, items.NONE, items.NONE, items.NONE, items.NONE, items.NONE, items.NONE, items.NONE]}
    defending_player = {"species": "SQUIRTLE", "mon_name": "Bagina", "moves": ["TACKLE"], "name": "Who Cares", "items": [items.NONE, items.NONE, items.NONE, items.NONE, items.NONE, items.NONE, items.NONE, items.NONE]}
    b = battle(attacking_player, defending_player)
    print(b.log_bytes())
    b.print()