import random

import util
from resources import *

class BaseItem:
    @classmethod
    def numeric_id(self):
        return NONE
    @classmethod
    def combat_stats(self, owner):
        return {}
    @classmethod
    def unique_combat_stats(self, owner):
        return {}
    @classmethod
    def on_precombat(self, owner, state, log, unique):
        pass
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        pass
    @classmethod
    def on_postdamage(self, owner, state, log, unique):
        pass
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        pass
    @classmethod
    def on_beforedamaged(self, owner, state, log, unique):
        pass
    @classmethod
    def on_afterdamaged(self, owner, state, log, unique):
        pass
    @classmethod
    def on_evaded(self, owner, state, log, unique):
        pass
    @classmethod
    def on_missed(self, owner, state, log, unique):
        pass
    @classmethod
    def on_moveused(self, owner, state, log, unique):
        pass
    @classmethod
    def on_real_afterdamaged(self, owner, state, log, unique):
        pass

class SmallDagger(BaseItem):
    @classmethod
    def numeric_id(self):
        return SMALL_DAGGER
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 5
        }

class LesserWand(BaseItem):
    @classmethod
    def numeric_id(self):
        return LESSER_WAND
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_attack": 5
        }

class Chainmail(BaseItem):
    @classmethod
    def numeric_id(self):
        return CHAINMAIL
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 5
        }

class MagicCloak(BaseItem):
    @classmethod
    def numeric_id(self):
        return MAGIC_CLOAK
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_defense": 5
        }

class WoodenShield(BaseItem):
    @classmethod
    def numeric_id(self):
        return WOODEN_SHIELD
    @classmethod
    def combat_stats(self, owner):
        return {
            "evasion": 5
        }

class SharpshooterGem(BaseItem):
    @classmethod
    def numeric_id(self):
        return SHARPSHOOTER_GEM
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 5
        }

class RingOfVitality(BaseItem):
    @classmethod
    def numeric_id(self):
        return RING_OF_VITALITY
    @classmethod
    def combat_stats(self, owner):
        return {
            "hp": 5
        }

class PointedNeedle(BaseItem):
    @classmethod
    def numeric_id(self):
        return POINTED_NEEDLE
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 3
        }

class NintendiumShard(BaseItem):
    @classmethod
    def numeric_id(self):
        return NINTENDIUM_SHARD
    @classmethod
    def combat_stats(self, owner):
        return {}

class SharpSpear(BaseItem):
    @classmethod
    def numeric_id(self):
        return SHARP_SPEAR
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 7
        }

class Longsword(BaseItem):
    @classmethod
    def numeric_id(self):
        return LONGSWORD
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 20
        }

class GreaterWand(BaseItem):
    @classmethod
    def numeric_id(self):
        return GREATER_WAND
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_attack": 20
        }

class ArmoredVest(BaseItem):
    @classmethod
    def numeric_id(self):
        return ARMORED_VEST
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 20
        }

class SorcerersCap(BaseItem):
    @classmethod
    def numeric_id(self):
        return SORCERERS_CAP
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_defense": 20
        }

class GuardianAegis(BaseItem):
    @classmethod
    def numeric_id(self):
        return GUARDIAN_AEGIS
    @classmethod
    def combat_stats(self, owner):
        return {
            "evasion": 20
        }

class PrecisionCharm(BaseItem):
    @classmethod
    def numeric_id(self):
        return PRECISION_CHARM
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 20
        }

class GiantStrength(BaseItem):
    @classmethod
    def numeric_id(self):
        return GIANT_STRENGTH
    @classmethod
    def combat_stats(self, owner):
        return {
            "hp": 20
        }

class MrBalls(BaseItem):
    @classmethod
    def numeric_id(self):
        return SMALL_DAGGER
    @classmethod
    def combat_stats(self, owner):
        return {
            "hp": 20,
            "defense": 20
        }
    @classmethod
    def unique_combat_stats(self, owner):
        return {
            "defense": 20,
            "special_defense": 20
        }

class Daikatana(BaseItem):
    @classmethod
    def numeric_id(self):
        return DAIKATANA
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 40,
            "accuracy": 20
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if unique:
            if state["move_type"] == "physical":
                dmg = damage(
                    state, "physical",
                    0.1*state["defender"]["hp"]
                )
                log.announce_item_trigger()
                apply_damage(state["defender"], dmg, log)
                log.push(
                    BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_DAIKATANA_PHYSICAL,
                    util.bcd(dmg), log.item_stringbuf_id(self.numeric_id())
                )
            else:
                state["effective_accuracy"] += 50
                log.announce_item_trigger()
                log.push(
                    BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_DAIKATANA_SPECIAL,
                    log.item_stringbuf_id(self.numeric_id())
                )

class EdgeOfDuality(BaseItem):
    @classmethod
    def numeric_id(self):
        return EDGE_OF_DUALITY
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 20,
            "special_attack": 20,
            "accuracy": 10
        }
    @classmethod
    def on_postdamage(self, owner, state, log, unique):
        log.announce_item_trigger()
        phys_dmg = damage(state, "physical", state["base_damage"]/2)
        spec_dmg = damage(state, "special", state["base_damage"]/2)
        state["damage_dealt"] = phys_dmg + spec_dmg

class Rowhammer(BaseItem):
    @classmethod
    def numeric_id(self):
        return ROWHAMMER
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 40,
            "hp": 20
        }
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        log.announce_item_trigger()
        stat = random.choice(("attack", "defense", "special_attack", "special_defense"))
        perc = random.choice((0.04, 0.08, 0.16, 0.32)) * owner["base_" + stat]
        owner[stat] += perc
        log.push(
            BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_ROWHAMMER,
            log.get_stringbuf(STAT_NAMES[stat]), util.bcd(int(perc))
        )

class Glitchodia(BaseItem):
    @classmethod
    def numeric_id(self):
        return THE_GLITCHODIA
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 20,
            "special_defense": 20
        }
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        if unique:
            log.announce_item_trigger()
            slot = random.choice(
                filter_item_slots(owner, lambda x: x.numeric_id() not in (NONE, THE_GLITCHODIA))
            )
            item = random.choice(
                (ITEM_1F, ITEM_2F, ITEM_3F, ITEM_4F)
            )
            replace_item(owner, slot, item)
            log.announce_item_replace(owner, slot, item)
            if FirstFloor in owner["items"] and SecondFloor in owner["items"] and ThirdFloor in owner["items"] and FourthFloor in owner["items"]:
                log.announce_item_trigger()
                state["win"] = True
                log.push(
                    BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_WON,
                    log.item_stringbuf_id(self.numeric_id())
                )

class FirstFloor(BaseItem):
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 15,
            "special_defense": 15
        }
    @classmethod
    def numeric_id(self):
        return ITEM_1F

class SecondFloor(BaseItem):
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 15,
            "special_defense": 15
        }
    @classmethod
    def numeric_id(self):
        return ITEM_2F

class ThirdFloor(BaseItem):
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 15,
            "special_defense": 15
        }
    @classmethod
    def numeric_id(self):
        return ITEM_3F

class FourthFloor(BaseItem):
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 15,
            "special_defense": 15
        }
    @classmethod
    def numeric_id(self):
        return ITEM_4F

class EdsLuckyCheese(BaseItem):
    @classmethod
    def numeric_id(self):
        return EDS_LUCKY_CHEESE
    @classmethod
    def combat_stats(self, owner):
        return {
            "hp": 20,
            "evasion": 20
        }
    @classmethod
    def on_beforedamaged(self, owner, state, log, unique):
        if unique:
            if owner["cur_hp"] < owner["hp"] * 0.3:
                if random.random() < 0.4:
                    log.announce_item_trigger()
                    state["missed"] = True

class Leftovers(BaseItem):
    @classmethod
    def numeric_id(self):
        return LEFTOVERS
    @classmethod
    def combat_stats(self, owner):
        return {
            "hp": 20,
            "defense": 20,
            "special_defense": 20
        }
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        if unique:
            log.announce_item_trigger()
            val = int((owner["hp"] - owner["cur_hp"]) * 0.1)
            apply_damage(owner, -val, log)
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_RECOVERED,
                util.bcd(val), log.item_stringbuf_id(self.numeric_id())
            )

class VoidPointer(BaseItem):
    @classmethod
    def numeric_id(self):
        return VOID_POINTER
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 15,
            "attack": 40
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if unique and state["crit"]:
            state["base_damage"] /= 2
            state["base_damage"] *= 2.25

class BallOfSpikes(BaseItem):
    @classmethod
    def numeric_id(self):
        return BALL_OF_SPIKES
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 15,
            "defense": 40
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if unique and state["crit"]:
            state["effective_defense"] *= 0.9
            state["effective_sp_defense"] *= 0.9

class GuiltyCrown(BaseItem):
    @classmethod
    def numeric_id(self):
        return GUILTY_CROWN
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 20,
            "special_defense": 20
        }
    @classmethod
    def on_afterdamaged(self, owner, state, log, unique):
        if unique and owner["cur_hp"] <= state["damage_dealt"]:
            log.announce_item_trigger()
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_REDUCED,
                log.item_stringbuf_id(self.numeric_id())
            )
            state["damage_dealt"] = int(state["damage_dealt"] / 2)
            if "gc_triggers" not in state["permvars"]:
                state["permvars"]["gc_triggers"] = 0
            state["permvars"]["gc_triggers"] += 1
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_TRIGGER_COUNT,
                state["permvars"]["gc_triggers"]
            )
            if state["permvars"]["gc_triggers"] >= 3:
                state["win"] = True
                log.push(
                    BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_WON,
                    log.item_stringbuf_id(self.numeric_id())
                )

class ScopeLens(BaseItem):
    @classmethod
    def numeric_id(self):
        return SCOPE_LENS
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 15,
            "accuracy": 40
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if unique and state["crit"]:
            state["effective_accuracy"] = 10000
            
class RazorClaw(BaseItem):
    @classmethod
    def numeric_id(self):
        return RAZOR_CLAW
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 15,
            "special_attack": 40
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if unique and state["crit"]:
            log.announce_item_trigger()
            owner["evasion"] += 5

class AbsorptionStaff(BaseItem):
    @classmethod
    def numeric_id(self):
        return ABSORPTION_STAFF
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_attack": 40,
            "defense": 20
        }
    @classmethod
    def on_postdamage(self, owner, state, log, unique):
        if unique:
            log.announce_item_trigger()
            val = int(state["damage_dealt"] * 0.2)
            apply_damage(owner, -val, log)
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_RECOVERED,
                util.bcd(val), log.item_stringbuf_id(self.numeric_id())
            )

class ExpertBelt(BaseItem):
    @classmethod
    def numeric_id(self):
        return EXPERT_BELT
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 40,
            "special_attack": 20
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if unique:
            effect_mult = type_effectiveness(MOVE_DATA[state["move_id"]]['type'], state["defender"])
            new_effect_mult = 1
            if effect_mult > 1.1:
                new_effect_mult = 2.5
            elif effect_mult < 0.15:
                new_effect_mult = 0.1
            elif effect_mult < 0.9:
                new_effect_mult = 0.33
            state["base_damage"] /= effect_mult
            state["base_damage"] *= new_effect_mult

class HotPotato(BaseItem):
    @classmethod
    def numeric_id(self):
        return HOT_POTATO
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 10,
            "evasion": 10
        }
    @classmethod
    def on_afterdamaged(self, owner, state, log, unique):
        if unique:
            slot = random.choice(
                filter_item_slots(state["attacker"], lambda x: x.numeric_id() != NONE)
            )
            log.announce_item_trigger()
            replace_item(state["attacker"], slot, HOT_POTATO)
            log.announce_item_replace(state["attacker"], slot, HOT_POTATO)
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        state["effective_attack"] -= owner["base_attack"] * 0.05
        state["effective_sp_attack"] -= owner["base_special_attack"] * 0.05

class LifeOrb(BaseItem):
    @classmethod
    def numeric_id(self):
        return LIFE_ORB
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 20,
            "special_attack": 20
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        state["base_damage"] *= 1.3
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        log.announce_item_trigger()
        val = int(owner["hp"] * 0.1)
        apply_damage(owner, val, log)
        log.push(
            BATTLE_ACTION_MESSAGE, MSG_BATTLE_LOST_HP,
            owner["string_buffer_id"]
        )
    
class LaggingTail(BaseItem):
    @classmethod
    def numeric_id(self):
        return LAGGING_TAIL
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 60,
            "special_defense": 40,
            "evasion": 20
        }
    @classmethod
    def on_precombat(self, owner, state, log, unique):
        if self in state["attacker"]["items"] and self in state["defender"]["items"]:
            return
        if state["attacker_side"]:
            state["attacker_turn"] = False
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_LAGGING_TAIL,
                state["attacker"]["string_buffer_id"]
            )
        else:
            state["attacker_turn"] = True
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_LAGGING_TAIL,
                state["defender"]["string_buffer_id"]
            )

class FocusSash(BaseItem):
    @classmethod
    def numeric_id(self):
        return FOCUS_SASH
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 20,
            "special_defense": 20
        }
    @classmethod
    def on_afterdamaged(self, owner, state, log, unique):
        chance = 0.1
        if owner["cur_hp"] >= owner["hp"]: chance = 0.85
        if random.random() < chance and state["damage_dealt"] >= owner["cur_hp"]:
            log.announce_item_trigger()
            state["damage_dealt"] = int(owner["cur_hp"] - 1)
            log.push(BATTLE_ACTION_MESSAGE, MSG_BATTLE_ENDURED)

class Brightpowder(BaseItem):
    @classmethod
    def numeric_id(self):
        return BRIGHTPOWDER
    @classmethod
    def combat_stats(self, owner):
        return {
            "evasion": 20,
            "hp": 20
        }
    @classmethod
    def unique_combat_stats(self, owner):
        return {
            "evasion": 40
        }

class KingsRock(BaseItem):
    @classmethod
    def numeric_id(self):
        return KINGS_ROCK
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 20,
            "special_defense": 20,
            "hp": 20
        }
    @classmethod
    def on_postdamage(self, owner, state, log, unique):
        if random.random() < 0.2:
            log.announce_item_trigger()
            state["defender"]["flinching"] = True

class RockOfThrow(BaseItem):
    @classmethod
    def numeric_id(self):
        return ROCK_OF_THROW
    @classmethod
    def combat_stats(self, owner):
        return {
            "evasion": 40,
            "hp": 20
        }
    @classmethod
    def on_evaded(self, owner, state, log, unique):
        if unique:
            log.announce_item_trigger()
            val = damage(state, "special", state["attacker"]["hp"] * 0.1)
            apply_damage(state["attacker"], val, log)
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_NORMAL_DAMAGE,
                state["attacker"]["string_buffer_id"], util.bcd(val)
            )

class StealthPebbles(BaseItem):
    @classmethod
    def numeric_id(self):
        return STEALTH_PEBBLES
    @classmethod
    def combat_stats(self, owner):
        return {
            "hp": 20,
            "special_defense": 40
        }
    @classmethod
    def on_precombat(self, owner, state, log, unique):
        if unique:
            log.announce_item_trigger()
            enemy = state["attacker"]
            if owner["string_buffer_id"] == enemy["string_buffer_id"]:
                enemy = state["defender"]
            val = int(enemy["hp"] * 0.15)
            apply_damage(enemy, val, log)
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_LOST_HP,
                enemy["string_buffer_id"]
            )

class Wumbotizer(BaseItem):
    @classmethod
    def numeric_id(self):
        return WUMBOTIZER
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 20,
            "special_attack": 20
        }
    @classmethod
    def on_moveused(self, owner, state, log, unique):
        if "b2b_stacks" not in state["permvars"]:
            state["permvars"]["b2b_stacks"] = 0
        if unique:
            log.announce_item_trigger()
            if state["permvars"]["b2b_stacks"] > 1:
                state["effective_attack"] += owner["base_attack"] * 0.3
                state["effective_sp_attack"] += owner["base_special_attack"] * 0.3
            if state["permvars"]["b2b_stacks"] > 3:
                state["effective_attack"] += owner["base_attack"] * 0.3
                state["effective_sp_attack"] += owner["base_special_attack"] * 0.3
    @classmethod
    def on_postdamage(self, owner, state, log, unique):
        if unique:
            if MOVE_DATA[state["move_id"]]["effect"] in DAMAGING_EFFECTS:
                state["permvars"]["b2b_stacks"] += 1
            else:
                state["permvars"]["b2b_stacks"] = 0
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_B2B,
                util.bcd(state["permvars"]["b2b_stacks"])
            )

class ScrabbleBoard(BaseItem):
    @classmethod
    def numeric_id(self):
        return SCRABBLE_BOARD
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_attack": 20,
            "special_defense": 20
        }
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        letters = len(set(MOVE_DATA[state["move_id"]]["display_name"].replace(" ","")))
        state["base_damage"] *= 1 + 0.02 * letters

class RodOfElements(BaseItem):
    @classmethod
    def numeric_id(self):
        return ROD_OF_ELEMENTS
    @classmethod
    def combat_stats(self, owner):
        return {
            "special_attack": 20,
            "evasion": 40
        }
    @classmethod
    def on_moveused(self, owner, state, log, unique):
        if "elemental_stacks" not in state["permvars"]:
            state["permvars"]["elemental_stacks"] = []
        if unique:
            cur_type = MOVE_DATA[state["move_id"]]["type"]
            prev_stacks = len(state["permvars"]["elemental_stacks"])
            if cur_type not in state["permvars"]["elemental_stacks"]:
                state["permvars"]["elemental_stacks"].append(cur_type)
            cur_stacks = len(state["permvars"]["elemental_stacks"])
            if cur_stacks > prev_stacks:
                log.announce_item_trigger()
                log.push(
                    BATTLE_ACTION_MESSAGE, MSG_BATTLE_STACKS,
                    util.bcd(cur_stacks)
                )
            state["effective_attack"] += owner["base_attack"] * 0.1 * cur_stacks
            state["effective_sp_attack"] += owner["base_special_attack"] * 0.1 * cur_stacks
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        if unique and len(state["permvars"]["elemental_stacks"]) >= 7:
            log.announce_item_trigger()
            state["win"] = True
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_WON,
                log.item_stringbuf_id(self.numeric_id())
            )

class Eviolite(BaseItem):
    @classmethod
    def numeric_id(self):
        return EVIOLITE
    @classmethod
    def combat_stats(self, owner):
        return {
            "defense": 40,
            "special_defense": 40
        }
    @classmethod
    def on_beforedamaged(self, owner, state, log, unique):
        if owner["mon_id"] in NFE_POKEMON:
            state["effective_defense"] *= 1.5
            state["effective_sp_defense"] *= 1.5

class UltimateBepis(BaseItem):
    @classmethod
    def numeric_id(self):
        return ULTIMATE_BEPIS
    @classmethod
    def combat_stats(self, owner):
        return {
            "attack": 20,
            "hp": 20
        }
    @classmethod
    def on_moveused(self, owner, state, log, unique):
        if "bepis_stacks1" not in state["permvars"]:
            state["permvars"]["bepis_stacks1"] = 0
            state["permvars"]["bepis_stacks2"] = 0
            state["permvars"]["bepis_stacks3"] = 0
            state["permvars"]["bepis_stacks4"] = 0
            state["permvars"]["bepis_stacks_all"] = 0
        if unique:
            state["effective_sp_attack"] += owner["base_special_attack"] * 0.08 * state["permvars"]["bepis_stacks1"]
            state["effective_defense"] += owner["base_defense"] * 0.08 * state["permvars"]["bepis_stacks2"]
            state["effective_crit"] += 6 * state["permvars"]["bepis_stacks3"]
            state["effective_evasion"] += 4 * state["permvars"]["bepis_stacks4"]
            state["effective_accuracy"] += 4 * state["permvars"]["bepis_stacks4"]
    @classmethod
    def on_postdamage(self, owner, state, log, unique):
        if "bepis_stacks1" not in state["permvars"]:
            state["permvars"]["bepis_stacks1"] = 0
            state["permvars"]["bepis_stacks2"] = 0
            state["permvars"]["bepis_stacks3"] = 0
            state["permvars"]["bepis_stacks4"] = 0
            state["permvars"]["bepis_stacks_all"] = 0
        if unique:
            log.announce_item_trigger()
            if MOVE_DATA[state["move_id"]]["effect"] in DAMAGING_EFFECTS:
                state["permvars"]["bepis_stacks2"] += 1
                state["permvars"]["bepis_stacks_all"] += 1
            else:
                state["permvars"]["bepis_stacks1"] += 1
                state["permvars"]["bepis_stacks_all"] += 1
    @classmethod
    def on_predamage(self, owner, state, log, unique):
        if "bepis_stacks1" not in state["permvars"]:
            state["permvars"]["bepis_stacks1"] = 0
            state["permvars"]["bepis_stacks2"] = 0
            state["permvars"]["bepis_stacks3"] = 0
            state["permvars"]["bepis_stacks4"] = 0
            state["permvars"]["bepis_stacks_all"] = 0
        if unique and state["crit"]:
            log.announce_item_trigger()
            state["permvars"]["bepis_stacks3"] += 1
            state["permvars"]["bepis_stacks_all"] += 1
    @classmethod
    def on_evaded(self, owner, state, log, unique):
        if "bepis_stacks1" not in state["permvars"]:
            state["permvars"]["bepis_stacks1"] = 0
            state["permvars"]["bepis_stacks2"] = 0
            state["permvars"]["bepis_stacks3"] = 0
            state["permvars"]["bepis_stacks4"] = 0
            state["permvars"]["bepis_stacks_all"] = 0
        if unique:
            log.announce_item_trigger()
            state["permvars"]["bepis_stacks4"] += 1
            state["permvars"]["bepis_stacks_all"] += 1
    @classmethod
    def on_endstep(self, owner, state, log, unique):
        if "bepis_stacks_all" not in state["permvars"]:
            state["permvars"]["bepis_stacks_all"] = 0
        if unique:
            if state["permvars"]["bepis_stacks_all"] > 4:
                log.announce_item_trigger()
                log.push(
                    BATTLE_ACTION_MESSAGE, MSG_BATTLE_STAT_CHANGES
                )
                state["permvars"]["bepis_stacks1"] = 0
                state["permvars"]["bepis_stacks2"] = 0
                state["permvars"]["bepis_stacks3"] = 0
                state["permvars"]["bepis_stacks4"] = 0
                state["permvars"]["bepis_stacks_all"] = 0

class DeliciousCurry(BaseItem):
    @classmethod
    def numeric_id(self):
        return DELICIOUS_CURRY
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 40,
            "special_attack": 20
        }
    @classmethod
    def on_precombat(self, owner, state, log, unique):
        owner["secondary_effect_mult"] = 2

class TheFlag(BaseItem):
    @classmethod
    def numeric_id(self):
        return THE_FLAG
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 20,
            "special_attack": 20,
            "attack": 20
        }
    @classmethod
    def on_precombat(self, owner, state, log, unique):
        if not state["unavoidable_encounter"]:
            log.announce_item_trigger()
            state["win"] = True
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_WON,
                log.item_stringbuf_id(self.numeric_id())
            )

class RadicalTrain(BaseItem):
    @classmethod
    def numeric_id(self):
        return RADICAL_TRAIN
    @classmethod
    def combat_stats(self, owner):
        return {
            "crit_chance": 20
        }
    @classmethod
    def on_precombat(self, owner, state, log, unique):
        log.announce_item_trigger()
        stat = random.choice(("attack", "defense", "special_attack", "special_defense"))
        perc = 0.6 * owner["base_" + stat]
        owner[stat] += perc
        log.push(
            BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_ROWHAMMER,
            log.get_stringbuf(STAT_NAMES[stat]), util.bcd(int(perc))
        )

class DecearingEgg(BaseItem):
    @classmethod
    def numeric_id(self):
        return DECEARING_EGG
    @classmethod
    def combat_stats(self, owner):
        return {
            "accuracy": 40,
            "defense": 20
        }
    @classmethod
    def on_real_afterdamaged(self, owner, state, log, unique):
        if state["move_type"] == "physical" and MOVE_DATA[state["move_id"]]["effect"] in DAMAGING_EFFECTS:
            dmg = damage(
                state, "special",
                max(0.05*state["attacker"]["cur_hp"], 0.01*state["attacker"]["hp"])
            )
            log.announce_item_trigger()
            apply_damage(state["attacker"], dmg, log)
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_EFFECT_DAIKATANA_PHYSICAL,
                util.bcd(dmg), log.item_stringbuf_id(self.numeric_id())
            )
        if state["move_type"] == "special" and MOVE_DATA[state["move_id"]]["effect"] in DAMAGING_EFFECTS:
            dmg = int(max(0.05*(state["defender"]["hp"]-state["defender"]["cur_hp"]), 0.01*state["defender"]["hp"]))
            log.announce_item_trigger()
            apply_damage(state["defender"], -dmg, log)
            log.push(
                BATTLE_ACTION_MESSAGE, MSG_BATTLE_RECOVERED,
                util.bcd(dmg), log.item_stringbuf_id(self.numeric_id())
            )

ITEM_CLASSES = {
    NONE: BaseItem,
    SMALL_DAGGER: SmallDagger,
    LESSER_WAND: LesserWand,
    CHAINMAIL: Chainmail,
    MAGIC_CLOAK: MagicCloak,
    WOODEN_SHIELD: WoodenShield,
    SHARPSHOOTER_GEM: SharpshooterGem,
    RING_OF_VITALITY: RingOfVitality,
    POINTED_NEEDLE: PointedNeedle,
    NINTENDIUM_SHARD: NintendiumShard,
    SHARP_SPEAR: SharpSpear,
    LONGSWORD: Longsword,
    GREATER_WAND: GreaterWand,
    ARMORED_VEST: ArmoredVest,
    SORCERERS_CAP: SorcerersCap,
    GUARDIAN_AEGIS: GuardianAegis,
    PRECISION_CHARM: PrecisionCharm,
    GIANT_STRENGTH: GiantStrength,
    MR_BALLS: MrBalls,
    DAIKATANA: Daikatana,
    EDGE_OF_DUALITY: EdgeOfDuality,
    ROWHAMMER: Rowhammer,
    THE_GLITCHODIA: Glitchodia,
    ITEM_1F: FirstFloor,
    ITEM_2F: SecondFloor,
    ITEM_3F: ThirdFloor,
    ITEM_4F: FourthFloor,
    EDS_LUCKY_CHEESE: EdsLuckyCheese,
    LEFTOVERS: Leftovers,
    VOID_POINTER: VoidPointer,
    BALL_OF_SPIKES: BallOfSpikes,
    GUILTY_CROWN: GuiltyCrown,
    SCOPE_LENS: ScopeLens,
    RAZOR_CLAW: RazorClaw,
    ABSORPTION_STAFF: AbsorptionStaff,
    EXPERT_BELT: ExpertBelt,
    HOT_POTATO: HotPotato,
    LIFE_ORB: LifeOrb,
    LAGGING_TAIL: LaggingTail,
    FOCUS_SASH: FocusSash,
    BRIGHTPOWDER: Brightpowder,
    KINGS_ROCK: KingsRock,
    ROCK_OF_THROW: RockOfThrow,
    STEALTH_PEBBLES: StealthPebbles,
    WUMBOTIZER: Wumbotizer,
    SCRABBLE_BOARD: ScrabbleBoard,
    ROD_OF_ELEMENTS: RodOfElements,
    EVIOLITE: Eviolite,
    ULTIMATE_BEPIS: UltimateBepis,
    DELICIOUS_CURRY: DeliciousCurry,
    THE_FLAG: TheFlag,
    RADICAL_TRAIN: RadicalTrain,
    DECEARING_EGG: DecearingEgg
}

def load_item_classes(participant):
    for i in range(0, len(participant["items"])):
        participant["items"][i] = ITEM_CLASSES[participant["items"][i]]

def apply_combat_stats(participant):
    applied_items = []
    for i in participant["items"]:
        apply_item_combat_stats(participant, i)
        if i.numeric_id() not in applied_items:
            apply_item_unique_combat_stats(participant, i)
        applied_items.append(i.numeric_id())

def apply_item_combat_stats(participant, item):
    stats = item.combat_stats(participant)
    for s, v in stats.items():
        if s in ("accuracy", "evasion", "crit_chance"):
            participant[s] += v
        else:
            participant[s] += participant["base_" + s] * (v/100)

def apply_item_unique_combat_stats(participant, item):
    stats = item.unique_combat_stats(participant)
    for s, v in stats.items():
        if s in ("accuracy", "evasion", "crit_chance"):
            participant[s] += v
        else:
            participant[s] += participant["base_" + s] * (v/100)

def remove_item_combat_stats(participant, item):
    stats = item.combat_stats(participant)
    for s, v in stats.items():
        if s in ("accuracy", "evasion", "crit_chance"):
            participant[s] -= v
        else:
            participant[s] -= participant["base_" + s] * (v/100)

def remove_item_unique_combat_stats(participant, item):
    stats = item.unique_combat_stats(participant)
    for s, v in stats.items():
        if s in ("accuracy", "evasion", "crit_chance"):
            participant[s] -= v
        else:
            participant[s] -= participant["base_" + s] * (v/100)

def replace_item(participant, slot, item):
    item = ITEM_CLASSES[item]
    orig_item = participant["items"][slot]
    remove_item_combat_stats(participant, orig_item)
    participant["items"][slot] = BaseItem
    if orig_item not in participant["items"]:
        remove_item_unique_combat_stats(participant, orig_item)
    if item not in participant["items"]:
        apply_item_unique_combat_stats(participant, item)
    apply_item_combat_stats(participant, item)
    participant["items"][slot] = item

# so much for 'don't repeat yourself' lol im too lazy and deadline is coming

def precombat(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_precombat(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def predamage(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_predamage(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def predamaged(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_beforedamaged(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def postdamage(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_postdamage(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def endstep(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_endstep(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def afterdamaged(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_afterdamaged(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def evaded(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_evaded(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def missed(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_missed(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def moveused(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_moveused(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break

def realafterdamaged(participant, state, log):
    applied_items = []
    ctr = 0
    for i in participant["items"]:
        log.set_current_callback_slot(ctr + MAX_ITEM_SLOTS - participant["string_buffer_id"] * MAX_ITEM_SLOTS)
        i.on_real_afterdamaged(participant, state, log, i.numeric_id() not in applied_items)
        applied_items.append(i.numeric_id())
        ctr += 1
        if state["win"]: break
