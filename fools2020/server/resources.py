import json

YOUNGSTER     = 0x01
BUG_CATCHER   = 0x02
LASS          = 0x03
SAILOR        = 0x04
JR_TRAINER_M  = 0x05
JR_TRAINER_F  = 0x06
POKEMANIAC    = 0x07
SUPER_NERD    = 0x08
HIKER         = 0x09
BIKER         = 0x0A
BURGLAR       = 0x0B
ENGINEER      = 0x0C
JUGGLER_X     = 0x0D
FISHER        = 0x0E
SWIMMER       = 0x0F
CUE_BALL      = 0x10
GAMBLER       = 0x11
BEAUTY        = 0x12
PSYCHIC_TR    = 0x13
ROCKER        = 0x14
JUGGLER       = 0x15
TAMER         = 0x16
BIRD_KEEPER   = 0x17
BLACKBELT     = 0x18
SONY1         = 0x19
PROF_OAK      = 0x1A
CHIEF         = 0x1B
SCIENTIST     = 0x1C
GIOVANNI      = 0x1D
ROCKET        = 0x1E
COOLTRAINER_M = 0x1F
COOLTRAINER_F = 0x20
BRUNO         = 0x21
BROCK         = 0x22
MISTY         = 0x23
LT_SURGE      = 0x24
ERIKA         = 0x25
KOGA          = 0x26
BLAINE        = 0x27
SABRINA       = 0x28
GENTLEMAN     = 0x29
SONY2         = 0x2A
SONY3         = 0x2B
LORELEI       = 0x2C
CHANNELER     = 0x2D
AGATHA        = 0x2E
LANCE         = 0x2F

EFFECTIVENESS = [
    ["NORMAL","ROCK",0.5],
    ["NORMAL","STEEL",0.5],
    ["FIRE","FIRE",0.5],
    ["FIRE","WATER",0.5],
    ["FIRE","GRASS",2],
    ["FIRE","ICE",2],
    ["FIRE","BUG",2],
    ["FIRE","ROCK",0.5],
    ["FIRE","DRAGON",0.5],
    ["FIRE","STEEL",2],
    ["WATER","FIRE",2],
    ["WATER","WATER",0.5],
    ["WATER","GRASS",0.5],
    ["WATER","GROUND",2],
    ["WATER","ROCK",2],
    ["WATER","DRAGON",0.5],
    ["ELECTRIC","WATER",2],
    ["ELECTRIC","ELECTRIC",0.5],
    ["ELECTRIC","GRASS",0.5],
    ["ELECTRIC","GROUND",0.05],
    ["ELECTRIC","FLYING",2],
    ["ELECTRIC","DRAGON",0.5],
    ["GRASS","FIRE",0.5],
    ["GRASS","WATER",2],
    ["GRASS","GRASS",0.5],
    ["GRASS","POISON",0.5],
    ["GRASS","GROUND",2],
    ["GRASS","FLYING",0.5],
    ["GRASS","BUG",0.5],
    ["GRASS","ROCK",2],
    ["GRASS","DRAGON",0.5],
    ["GRASS","STEEL",0.5],
    ["ICE","WATER",0.5],
    ["ICE","GRASS",2],
    ["ICE","ICE",0.5],
    ["ICE","GROUND",2],
    ["ICE","FLYING",2],
    ["ICE","DRAGON",2],
    ["ICE","STEEL",0.5],
    ["ICE","FIRE",0.5],
    ["FIGHTING","NORMAL",2],
    ["FIGHTING","ICE",2],
    ["FIGHTING","POISON",0.5],
    ["FIGHTING","FLYING",0.5],
    ["FIGHTING","PSYCHIC",0.5],
    ["FIGHTING","BUG",0.5],
    ["FIGHTING","ROCK",2],
    ["FIGHTING","DARK",2],
    ["FIGHTING","STEEL",2],
    ["POISON","GRASS",2],
    ["POISON","POISON",0.5],
    ["POISON","GROUND",0.5],
    ["POISON","ROCK",0.5],
    ["POISON","GHOST",0.5],
    ["POISON","STEEL",0.05],
    ["GROUND","FIRE",2],
    ["GROUND","ELECTRIC",2],
    ["GROUND","GRASS",0.5],
    ["GROUND","POISON",2],
    ["GROUND","FLYING",0.05],
    ["GROUND","BUG",0.5],
    ["GROUND","ROCK",2],
    ["GROUND","STEEL",2],
    ["FLYING","ELECTRIC",0.5],
    ["FLYING","GRASS",2],
    ["FLYING","FIGHTING",2],
    ["FLYING","BUG",2],
    ["FLYING","ROCK",0.5],
    ["FLYING","STEEL",0.5],
    ["PSYCHIC","FIGHTING",2],
    ["PSYCHIC","POISON",2],
    ["PSYCHIC","PSYCHIC",0.5],
    ["PSYCHIC","DARK",0.05],
    ["PSYCHIC","STEEL",0.5],
    ["BUG","FIRE",0.5],
    ["BUG","GRASS",2],
    ["BUG","FIGHTING",0.5],
    ["BUG","POISON",0.5],
    ["BUG","FLYING",0.5],
    ["BUG","PSYCHIC",2],
    ["BUG","GHOST",0.5],
    ["BUG","DARK",2],
    ["BUG","STEEL",0.5],
    ["ROCK","FIRE",2],
    ["ROCK","ICE",2],
    ["ROCK","FIGHTING",0.5],
    ["ROCK","GROUND",0.5],
    ["ROCK","FLYING",2],
    ["ROCK","BUG",2],
    ["ROCK","STEEL",0.5],
    ["GHOST","NORMAL",0.05],
    ["GHOST","PSYCHIC",2],
    ["GHOST","DARK",0.5],
    ["GHOST","STEEL",0.5],
    ["GHOST","GHOST",2],
    ["DRAGON","DRAGON",2],
    ["DRAGON","STEEL",0.5],
    ["DARK","FIGHTING",0.5],
    ["DARK","PSYCHIC",2],
    ["DARK","GHOST",2],
    ["DARK","DARK",0.5],
    ["DARK","STEEL",0.5],
    ["STEEL","FIRE",0.5],
    ["STEEL","WATER",0.5],
    ["STEEL","ELECTRIC",0.5],
    ["STEEL","ICE",2],
    ["STEEL","ROCK",2],
    ["STEEL","STEEL",0.5]
]

DMG_MULT = 0.4
RATIO_FACTOR = 1.2

PHYSICAL_TYPES = [
    "NORMAL", "FIGHTING", "FLYING", "GROUND", "ROCK", "BUG", "GHOST", "POISON"
]

NFE_POKEMON = [
    "NIDORAN_M",
    "CLEFAIRY",
    "SPEAROW",
    "VOLTORB",
    "IVYSAUR",
    "EXEGGCUTE",
    "GRIMER",
    "NIDORAN_F",
    "CUBONE",
    "RHYHORN",
    "SHELLDER",
    "TENTACOOL",
    "GASTLY",
    "STARYU",
    "GROWLITHE",
    "PIDGEY",
    "SLOWPOKE",
    "KADABRA",
    "GRAVELER",
    "MACHOKE",
    "PSYDUCK",
    "DROWZEE",
    "KOFFING",
    "MANKEY",
    "SEEL",
    "DIGLETT",
    "VENONAT",
    "DODUO",
    "POLIWAG",
    "MEOWTH",
    "KRABBY",
    "VULPIX",
    "PIKACHU",
    "DRATINI",
    "DRAGONAIR",
    "KABUTO",
    "HORSEA",
    "SANDSHREW",
    "OMANYTE",
    "JIGGLYPUFF",
    "EEVEE",
    "MACHOP",
    "ZUBAT",
    "EKANS",
    "PARAS",
    "POLIWHIRL",
    "WEEDLE",
    "KAKUNA",
    "CATERPIE",
    "METAPOD",
    "MAGIKARP",
    "HAUNTER",
    "ABRA",
    "PIDGEOTTO",
    "BULBASAUR",
    "GOLDEEN",
    "PONYTA",
    "RATTATA",
    "NIDORINO",
    "NIDORINA",
    "GEODUDE",
    "MAGNEMITE",
    "CHARMANDER",
    "SQUIRTLE",
    "CHARMELEON",
    "WARTORTLE",
    "ODDISH",
    "GLOOM",
    "BELLSPROUT",
    "WEEPINBELL"
]

BATTLE_ACTION_MESSAGE = 0x80
BATTLE_ACTION_TRIGGER = 2
BATTLE_ACTION_REPLACE = 3
BATTLE_ACTION_DAMAGE = 4
BATTLE_ACTION_HEAL = 5
BATTLE_ACTION_FAINT = 6

MSG_BATTLE_USED = 1
MSG_BATTLE_FIRST = 2
MSG_BATTLE_NORMAL_DAMAGE = 3
MSG_BATTLE_SENDOUT_OWN = 4
MSG_BATTLE_CRIT = 5
MSG_BATTLE_SUPER_EFFECTIVE = 6
MSG_BATTLE_NOT_VERY_EFFECTIVE = 7
MSG_BATTLE_INEFFECTIVE = 8
MSG_BATTLE_EQUIP = 9
MSG_BATTLE_FAINTED = 10
MSG_BATTLE_ATTACK_MISSED = 11
MSG_BATTLE_ATTACK_AVOIDED = 12
MSG_BATTLE_EFFECT_DAIKATANA_PHYSICAL = 13
MSG_BATTLE_EFFECT_DAIKATANA_SPECIAL = 14
MSG_BATTLE_EFFECT_ROWHAMMER = 15
MSG_BATTLE_EFFECT_WON = 16
MSG_BATTLE_RECOVERED = 17
MSG_BATTLE_REDUCED = 18
MSG_BATTLE_TRIGGER_COUNT = 19
MSG_BATTLE_LOST_HP = 20
MSG_BATTLE_LAGGING_TAIL = 21
MSG_BATTLE_ENDURED = 22
MSG_BATTLE_FLINCHING = 23
MSG_BATTLE_B2B = 24
MSG_BATTLE_STACKS = 25
MSG_BATTLE_STAT_CHANGES = 26
MSG_BATTLE_NO_CHOICE = 27
MSG_BATTLE_TURN_LIMIT_1 = 28
MSG_BATTLE_TURN_LIMIT_2 = 29
MSG_BATTLE_TURN_LIMIT_3 = 30
MSG_BATTLE_SUDDEN_DEATH = 31

MESSAGES = {
    MSG_BATTLE_USED: "<B>{str_buf}</B> used <B>{str_buf}</B>!",
    MSG_BATTLE_FIRST: "<B>{str_buf}</B> strikes first.",
    MSG_BATTLE_NORMAL_DAMAGE: "<B>{str_buf}</B> took <B>{raw_int}</B> damage!",
    MSG_BATTLE_CRIT: "Critical hit!",
    MSG_BATTLE_SUPER_EFFECTIVE: "It's super effective!",
    MSG_BATTLE_NOT_VERY_EFFECTIVE: "Not very effective...",
    MSG_BATTLE_INEFFECTIVE: "It has little effect...",
    MSG_BATTLE_B2B: "bepis",
    MSG_BATTLE_FAINTED: "<B>{str_buf}</B> fainted!",
    MSG_BATTLE_ATTACK_MISSED: "<B>{str_buf}</B>'s attack missed!",
    MSG_BATTLE_ATTACK_AVOIDED: "<B>{str_buf}</B> avoided the attack!",
    MSG_BATTLE_EFFECT_DAIKATANA_PHYSICAL: "<B>{raw_int}</B> damage from <B>{str_buf}</B>!",
    MSG_BATTLE_EFFECT_DAIKATANA_SPECIAL: "Accuracy boosted by <B>{str_buf}</B>!",
    MSG_BATTLE_EFFECT_ROWHAMMER: "<B>{str_buf}</B> increased by <B>{raw_int}</B>!",
    MSG_BATTLE_EFFECT_WON: "The battle was won due to\neffects of <B>{str_buf}</B>!",
    MSG_BATTLE_RECOVERED: "Recovered <B>{raw_int}</B> HP with <B>{str_buf}</B>!",
    MSG_BATTLE_REDUCED: "Damage reduced by <B>{str_buf}</B>!",
    MSG_BATTLE_TRIGGER_COUNT: "Trigger count is <B>{raw_int}</B>.",
    MSG_BATTLE_LOST_HP: "<B>{str_buf}</B> lost some of its HP!",
    MSG_BATTLE_LAGGING_TAIL: "<B>{str_buf}</B> is lagging behind!",
    MSG_BATTLE_ENDURED: "Attack was barely endured!",
    MSG_BATTLE_FLINCHING: "<B>{str_buf}</B> flinched!",
    MSG_BATTLE_B2B: "Back-to-Back counter is <B>{raw_int}</B>.",
    MSG_BATTLE_STACKS: "Currently at <B>{raw_int}</B> stacks.",
    MSG_BATTLE_STAT_CHANGES: "Stat changes were eliminated!"
}

def get_move_by_numeric_id(numeric_id):
    for m in MOVE_DATA.values():
        if m["move_numeric_id"] == numeric_id:
            return m
    return None

with open('mons.json', 'r') as fp:
    MON_DATA = json.load(fp)
with open('moves.json' ,'r') as fp:
    MOVE_DATA = json.load(fp)

DAMAGING_EFFECTS = [
    "EFFECT_ALWAYS_HIT",
    "EFFECT_ATTACK_DOWN_HIT",
    "EFFECT_BIDE",
    "EFFECT_BURN_HIT",
    "EFFECT_CONFUSE_HIT",
    "EFFECT_DEFENSE_DOWN_HIT",
    "EFFECT_DOUBLE_HIT",
    "EFFECT_DREAM_EATER",
    "EFFECT_EARTHQUAKE",
    "EFFECT_FLINCH_HIT",
    "EFFECT_FLY",
    "EFFECT_FREEZE_HIT",
    "EFFECT_GUST",
    "EFFECT_HYPER_BEAM",
    "EFFECT_JUMP_KICK",
    "EFFECT_LEECH_HIT",
    "EFFECT_LEVEL_DAMAGE",
    "EFFECT_MULTI_HIT",
    "EFFECT_NORMAL_HIT",
    "EFFECT_OHKO",
    "EFFECT_PARALYZE_HIT",
    "EFFECT_PAY_DAY",
    "EFFECT_POISON_HIT",
    "EFFECT_POISON_MULTI_HIT",
    "EFFECT_PRIORITY_HIT",
    "EFFECT_PSYWAVE",
    "EFFECT_RAGE",
    "EFFECT_RAMPAGE",
    "EFFECT_RAZOR_WIND",
    "EFFECT_RECOIL_HIT",
    "EFFECT_SKULL_BASH",
    "EFFECT_SKY_ATTACK",
    "EFFECT_SOLARBEAM",
    "EFFECT_SP_DEF_DOWN_HIT",
    "EFFECT_SPEED_DOWN_HIT",
    "EFFECT_STATIC_DAMAGE",
    "EFFECT_STOMP",
    "EFFECT_SUPER_FANG",
    "EFFECT_THUNDER",
    "EFFECT_TRAP_TARGET",
    "EFFECT_TRI_ATTACK"
]

NONE = 0
SMALL_DAGGER = 1
LESSER_WAND = 2
CHAINMAIL = 3
MAGIC_CLOAK = 4
WOODEN_SHIELD = 5
SHARPSHOOTER_GEM = 6
RING_OF_VITALITY = 7
POINTED_NEEDLE = 8
NINTENDIUM_SHARD = 9
SHARP_SPEAR = 10
LONGSWORD = 11
GREATER_WAND = 12
ARMORED_VEST = 13
SORCERERS_CAP = 14
GUARDIAN_AEGIS = 15
PRECISION_CHARM = 16
GIANT_STRENGTH = 17
MR_BALLS = 18
DAIKATANA = 19
EDGE_OF_DUALITY = 20
ROWHAMMER = 21
THE_GLITCHODIA = 22
EDS_LUCKY_CHEESE = 23
LEFTOVERS = 24
REVERSAL_EMBLEM = 25
VOID_POINTER = 26
BALL_OF_SPIKES = 27
ROD_OF_SUPREMACY = 28
GUILTY_CROWN = 29
SCOPE_LENS = 30
RAZOR_CLAW = 31
ABSORPTION_STAFF = 32
EXPERT_BELT = 33
HOT_POTATO = 34
CHOICE_BAND = 35
LIFE_ORB = 36
LAGGING_TAIL = 37
FOCUS_SASH = 38
BRIGHTPOWDER = 39
KINGS_ROCK = 40
EVIOLITE = 41
ROCK_OF_THROW = 42
STEALTH_PEBBLES = 43
WUMBOTIZER = 44
SCRABBLE_BOARD = 45
ROD_OF_ELEMENTS = 46
ULTIMATE_BEPIS = 47
DELICIOUS_CURRY = 48
THE_FLAG = 49
RADICAL_TRAIN = 50
BPD_8000V2 = 51
STAR_FOR_EFFORT = 52
DECEARING_EGG = 53
ITEM_1F = 54
ITEM_2F = 55
ITEM_3F = 56
ITEM_4F = 57

MAX_ITEM_SLOTS = 8

ITEM_NAMES = {
    NONE: "Bepis",
    SMALL_DAGGER: "Small Dagger",
    LESSER_WAND: "Lesser Wand",
    CHAINMAIL: "Chainmail",
    MAGIC_CLOAK: "Magic Cloak",
    WOODEN_SHIELD: "Wooden Shield",
    SHARPSHOOTER_GEM: "Sharpshooter Gem",
    RING_OF_VITALITY: "Ring of Vitality",
    POINTED_NEEDLE: "Pointed Needle",
    NINTENDIUM_SHARD: "Nintendium Shard",
    SHARP_SPEAR: "Sharp Spear",
    LONGSWORD: "Longsword",
    GREATER_WAND: "Greater Wand",
    ARMORED_VEST: "Armored Vest",
    SORCERERS_CAP: "Sorcerer's Cap",
    GUARDIAN_AEGIS: "Guardian Aegis",
    PRECISION_CHARM: "Precision Charm",
    GIANT_STRENGTH: "Giant Strength",
    MR_BALLS: "Mr. Balls",
    DAIKATANA: "Daikatana",
    EDGE_OF_DUALITY: "Edge of Duality",
    ROWHAMMER: "Rowhammer",
    THE_GLITCHODIA: "The Glitchodia",
    EDS_LUCKY_CHEESE: "Ed's Lucky Cheese",
    LEFTOVERS: "Leftovers",
    REVERSAL_EMBLEM: "Reversal Emblem",
    VOID_POINTER: "Void Pointer",
    BALL_OF_SPIKES: "Ball of Spikes",
    ROD_OF_SUPREMACY: "Rod of Supremacy",
    GUILTY_CROWN: "Guilty Crown",
    SCOPE_LENS: "Scope Lens",
    RAZOR_CLAW: "Razor Claw",
    ABSORPTION_STAFF: "Absorption Staff",
    EXPERT_BELT: "Expert Belt",
    HOT_POTATO: "Hot Potato",
    CHOICE_BAND: "Choice Band",
    LIFE_ORB: "Life Orb",
    LAGGING_TAIL: "Lagging Tail",
    FOCUS_SASH: "Focus Sash",
    BRIGHTPOWDER: "Brightpowder",
    KINGS_ROCK: "King's Rock",
    EVIOLITE: "Eviolite",
    ROCK_OF_THROW: "Rock of Throw",
    STEALTH_PEBBLES: "Stealth Pebbles",
    WUMBOTIZER: "Wumbotizer",
    SCRABBLE_BOARD: "Scrabble Board",
    ROD_OF_ELEMENTS: "Rod of Elements",
    ULTIMATE_BEPIS: "Ultimate Bepis",
    DELICIOUS_CURRY: "Delicious Curry",
    THE_FLAG: "The Flag",
    RADICAL_TRAIN: "Radical Train",
    BPD_8000V2: "BPD-8000v2",
    STAR_FOR_EFFORT: "Star for Effort",
    DECEARING_EGG: "Decearing Egg"
}

STAT_NAMES = {
    "hp": "Health",
    "attack": "Attack",
    "defense": "Defense",
    "special_attack": "Sp.Atk.",
    "special_defense": "Sp.Def."
}

def damage(state, dmg_type, amount):
    if dmg_type == "physical":
        amount *= state["effective_attack"]**RATIO_FACTOR / state["effective_defense"]**RATIO_FACTOR
    elif dmg_type == "special":
        amount *= state["effective_sp_attack"]**RATIO_FACTOR / state["effective_sp_defense"]**RATIO_FACTOR
    elif dmg_type != "true":
        raise NotImplementedError("unknown damage type %s" % dmg_type)
    amount *= DMG_MULT
    return int(amount)

def type_effectiveness(move_type, defender):
    mult = 1.0
    for i in EFFECTIVENESS:
        if move_type == i[0] and i[1] in defender["types"]:
            mult *= i[2]
    return mult

def calc_damage_state(defender):
    # 7*8 hp tiles available
    MAX_TILES = 7*8
    frac = defender["cur_hp"] / defender["hp"]
    num_tiles = int(MAX_TILES * frac)
    if defender["cur_hp"] <= 0:
        num_tiles = 0
    if defender["cur_hp"] > 0 and num_tiles == 0:
        num_tiles = 1
    return num_tiles

def apply_damage(defender, dmg, log):
    dmg = int(dmg)
    if dmg == 0:
        return
    defender["cur_hp"] -= dmg
    if defender["cur_hp"] < 0: defender["cur_hp"] = 0
    if defender["cur_hp"] > defender["hp"]: defender["cur_hp"] = defender["hp"]
    if dmg < 0:
        log.push(BATTLE_ACTION_HEAL, defender["string_buffer_id"], calc_damage_state(defender))
    else:
        log.push(BATTLE_ACTION_DAMAGE, defender["string_buffer_id"], calc_damage_state(defender))

def filter_item_slots(participant, f):
    idx = 0
    result = []
    for i in participant["items"]:
        if f(i): result.append(idx)
        idx += 1
    return result