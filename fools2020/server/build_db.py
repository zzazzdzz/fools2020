# coding: utf-8
# create databases for use in fools2020

import json

mon_names = [
    "RHYDON","KANGASKHAN","NIDORAN_M","CLEFAIRY","SPEAROW","VOLTORB","NIDOKING","SLOWBRO","IVYSAUR","EXEGGUTOR","LICKITUNG","EXEGGCUTE","GRIMER","GENGAR","NIDORAN_F","NIDOQUEEN","CUBONE","RHYHORN","LAPRAS","ARCANINE","MEW","GYARADOS","SHELLDER","TENTACOOL","GASTLY","SCYTHER","STARYU","BLASTOISE","PINSIR","TANGELA","MISSINGNO.","MISSINGNO.","GROWLITHE","ONIX","FEAROW","PIDGEY","SLOWPOKE","KADABRA","GRAVELER","CHANSEY","MACHOKE","MR__MIME","HITMONLEE","HITMONCHAN","ARBOK","PARASECT","PSYDUCK","DROWZEE","GOLEM","MISSINGNO.","MAGMAR","MISSINGNO.","ELECTABUZZ","MAGNETON","KOFFING","MISSINGNO.","MANKEY","SEEL","DIGLETT","TAUROS","MISSINGNO.","MISSINGNO.","MISSINGNO.","FARFETCH_D","VENONAT","DRAGONITE","MISSINGNO.","MISSINGNO.","MISSINGNO.","DODUO","POLIWAG","JYNX","MOLTRES","ARTICUNO","ZAPDOS","DITTO","MEOWTH","KRABBY","MISSINGNO.","MISSINGNO.","MISSINGNO.","VULPIX","NINETALES","PIKACHU","RAICHU","MISSINGNO.","MISSINGNO.","DRATINI","DRAGONAIR","KABUTO","KABUTOPS","HORSEA","SEADRA","MISSINGNO.","MISSINGNO.","SANDSHREW","SANDSLASH","OMANYTE","OMASTAR","JIGGLYPUFF","WIGGLYTUFF","EEVEE","FLAREON","JOLTEON","VAPOREON","MACHOP","ZUBAT","EKANS","PARAS","POLIWHIRL","POLIWRATH","WEEDLE","KAKUNA","BEEDRILL","MISSINGNO.","DODRIO","PRIMEAPE","DUGTRIO","VENOMOTH","DEWGONG","MISSINGNO.","MISSINGNO.","CATERPIE","METAPOD","BUTTERFREE","MACHAMP","MISSINGNO.","GOLDUCK","HYPNO","GOLBAT","MEWTWO","SNORLAX","MAGIKARP","MISSINGNO.","MISSINGNO.","MUK","MISSINGNO.","KINGLER","CLOYSTER","MISSINGNO.","ELECTRODE","CLEFABLE","WEEZING","PERSIAN","MAROWAK","MISSINGNO.","HAUNTER","ABRA","ALAKAZAM","PIDGEOTTO","PIDGEOT","STARMIE","BULBASAUR","VENUSAUR","TENTACRUEL","MISSINGNO.","GOLDEEN","SEAKING","MISSINGNO.","MISSINGNO.","MISSINGNO.","MISSINGNO.","PONYTA","RAPIDASH","RATTATA","RATICATE","NIDORINO","NIDORINA","GEODUDE","PORYGON","AERODACTYL","MISSINGNO.","MAGNEMITE","MISSINGNO.","MISSINGNO.","CHARMANDER","SQUIRTLE","CHARMELEON","WARTORTLE","CHARIZARD","MISSINGNO.","MISSINGNO.","MISSINGNO.","MISSINGNO.","ODDISH","GLOOM","VILEPLUME","BELLSPROUT","WEEPINBELL","VICTREEBEL"
]

move_names = [
    "POUND","KARATE CHOP","DOUBLESLAP","COMET PUNCH","MEGA PUNCH","PAY DAY","FIRE PUNCH","ICE PUNCH","THUNDERPUNCH","SCRATCH","VICEGRIP","GUILLOTINE","RAZOR WIND","SWORDS DANCE","CUT","GUST","WING ATTACK","WHIRLWIND","FLY","BIND","SLAM","VINE WHIP","STOMP","DOUBLE KICK","MEGA KICK","JUMP KICK","ROLLING KICK","SAND-ATTACK","HEADBUTT","HORN ATTACK","FURY ATTACK","HORN DRILL","TACKLE","BODY SLAM","WRAP","TAKE DOWN","THRASH","DOUBLE-EDGE","TAIL WHIP","POISON STING","TWINEEDLE","PIN MISSILE","LEER","BITE","GROWL","ROAR","SING","SUPERSONIC","SONICBOOM","DISABLE","ACID","EMBER","FLAMETHROWER","MIST","WATER GUN","HYDRO PUMP","SURF","ICE BEAM","BLIZZARD","PSYBEAM","BUBBLEBEAM","AURORA BEAM","HYPER BEAM","PECK","DRILL PECK","SUBMISSION","LOW KICK","COUNTER","SEISMIC TOSS","STRENGTH","ABSORB","MEGA DRAIN","LEECH SEED","GROWTH","RAZOR LEAF","SOLARBEAM","POISONPOWDER","STUN SPORE","SLEEP POWDER","PETAL DANCE","STRING SHOT","DRAGON RAGE","FIRE SPIN","THUNDERSHOCK","THUNDERBOLT","THUNDER WAVE","THUNDER","ROCK THROW","EARTHQUAKE","FISSURE","DIG","TOXIC","CONFUSION","PSYCHIC","HYPNOSIS","MEDITATE","AGILITY","QUICK ATTACK","RAGE","TELEPORT","NIGHT SHADE","MIMIC","SCREECH","DOUBLE TEAM","RECOVER","HARDEN","MINIMIZE","SMOKESCREEN","CONFUSE RAY","WITHDRAW","DEFENSE CURL","BARRIER","LIGHT SCREEN","HAZE","REFLECT","FOCUS ENERGY","BIDE","METRONOME","MIRROR MOVE","SELFDESTRUCT","EGG BOMB","LICK","SMOG","SLUDGE","BONE CLUB","FIRE BLAST","WATERFALL","CLAMP","SWIFT","SKULL BASH","SPIKE CANNON","CONSTRICT","AMNESIA","KINESIS","SOFTBOILED","HI JUMP KICK","GLARE","DREAM EATER","POISON GAS","BARRAGE","LEECH LIFE","LOVELY KISS","SKY ATTACK","TRANSFORM","BUBBLE","DIZZY PUNCH","SPORE","FLASH","PSYWAVE","SPLASH","ACID ARMOR","CRABHAMMER","EXPLOSION","FURY SWIPES","BONEMERANG","REST","ROCK SLIDE","HYPER FANG","SHARPEN","CONVERSION","TRI ATTACK","SUPER FANG","SLASH","SUBSTITUTE"
]

crys_moves_db = ["SKETCH","TRIPLE_KICK","THIEF","SPIDER_WEB","MIND_READER","NIGHTMARE","FLAME_WHEEL","SNORE","CURSE","FLAIL","CONVERSION2","AEROBLAST","COTTON_SPORE","REVERSAL","SPITE","POWDER_SNOW","PROTECT","MACH_PUNCH","SCARY_FACE","FAINT_ATTACK","SWEET_KISS","BELLY_DRUM","SLUDGE_BOMB","MUD_SLAP","OCTAZOOKA","SPIKES","ZAP_CANNON","FORESIGHT","DESTINY_BOND","PERISH_SONG","ICY_WIND","DETECT","BONE_RUSH","LOCK_ON","OUTRAGE","SANDSTORM","GIGA_DRAIN","ENDURE","CHARM","ROLLOUT","FALSE_SWIPE","SWAGGER","MILK_DRINK","SPARK","FURY_CUTTER","STEEL_WING","MEAN_LOOK","ATTRACT","SLEEP_TALK","HEAL_BELL","RETURN","PRESENT","FRUSTRATION","SAFEGUARD","PAIN_SPLIT","SACRED_FIRE","MAGNITUDE","DYNAMICPUNCH","MEGAHORN","DRAGONBREATH","BATON_PASS","ENCORE","PURSUIT","RAPID_SPIN","SWEET_SCENT","IRON_TAIL","METAL_CLAW","VITAL_THROW","MORNING_SUN","SYNTHESIS","MOONLIGHT","HIDDEN_POWER","CROSS_CHOP","TWISTER","RAIN_DANCE","SUNNY_DAY","CRUNCH","MIRROR_COAT","PSYCH_UP","EXTREMESPEED","ANCIENTPOWER","SHADOW_BALL","FUTURE_SIGHT","ROCK_SMASH","WHIRLPOOL","BEAT_UP"]

move_names_db = [x.replace(" ","_").replace("-","_") for x in move_names]
move_names_db_map = {}

for i in range(0, len(move_names_db)):
    move_names_db_map[move_names_db[i]] = move_names[i]

alt_names = {
    "NIDORAN_M": "NIDORAN♂",
    "NIDORAN_F": "NIDORAN♀",
    "MR__MIME": "MR. MIME",
    "FARFETCH_D": "FARFETCH'D"
}

alt_names_2 = {
    "NIDORANM": "NIDORAN_M",
    "NIDORANF": "NIDORAN_F",
    "FARFETCHD": "FARFETCH_D",
    "MRMIME": "MR__MIME"
}

base_path = r"D:\Pokered\pokecrystal-master\data\pokemon\base_stats\\"

mons = {}

for i in mon_names:
    if i == "MISSINGNO.": continue
    dname = i
    if i in alt_names: dname = alt_names[i]
    with open(base_path + i.lower() + ".asm", 'r') as fp:
        data = fp.read()
    data = data.split("\n")
    stat_tbl = [int(x) for x in data[2].replace(" ","").replace("db","").replace("\t","").split(",")]
    type_tbl = data[5].split(";")[0].replace(" ","").replace("db","").replace("\t","").split(",")
    move_tbl = [x for x in data[19].split(";")[0].replace(" ","").replace("tmhm","").replace("\t","").split(",") if x != '']
    if type_tbl[0] == type_tbl[1]:
        type_tbl = [type_tbl[0]]
    mons[i] = {
        "mon_id": i,
        "display_name": dname,
        "base_stats": stat_tbl,
        "types": type_tbl,
        "attacks": [],
        "move_compat": [],
        "mon_numeric_id": mon_names.index(i)+1
    }
    for move_name in move_tbl:
        if move_name not in crys_moves_db:
            if move_name == "PSYCHIC_M":
                move_name = "PSYCHIC"
            if move_name not in move_names_db:
                raise NotImplementedError(move_name)
            mons[i]['move_compat'].append(move_name)

with open(r'D:\Pokered\pokecrystal-master\data\pokemon\evos_attacks.asm', 'r') as fp:
    nn = None
    for i in fp.readlines():
        if "EvosAttacks:" in i:
            nn = i.strip().replace("EvosAttacks:","").upper()
            if nn in alt_names_2:
                nn = alt_names_2[nn]
            if nn == 'CHIKORITA':
                break
        else:
            parsed = i.strip().split(";")[0].replace(" ","").replace("db","").replace("\t","").split(",")
            try:
                lvl = int(parsed[0])
                move_name = parsed[1]
            except:
                continue
            if move_name not in mons[nn]['move_compat']:
                if move_name not in crys_moves_db:
                    if move_name == "PSYCHIC_M":
                        move_name = "PSYCHIC"
                    if move_name not in move_names_db:
                        raise NotImplementedError(move_name)
                    if lvl == 1:
                        mons[nn]['attacks'].append(move_name)
                        if move_name not in mons[nn]['move_compat']:
                            mons[nn]['move_compat'].append(move_name)
                    else:
                        if move_name not in mons[nn]['move_compat']:
                            mons[nn]['move_compat'].append(move_name)

with open(r'D:\Pokered\pokecrystal-master\data\pokemon\egg_moves.asm', 'r') as fp:
    nn = None
    for i in fp.readlines():
        if "EggMoves:" in i:
            nn = i.strip().replace("EggMoves:","").upper()
            if nn in alt_names_2:
                nn = alt_names_2[nn]
            if nn == 'CHIKORITA':
                break
        else:
            parsed = i.strip().split(";")[0].replace(" ","").replace("db","").replace("\t","").split(",")
            move_name = parsed[0]
            if move_name == "PSYCHIC_M":
                move_name = "PSYCHIC"
            if move_name in move_names_db:
                if move_name not in mons[nn]['move_compat']:
                    mons[nn]['move_compat'].append(move_name)

moves = {}

with open(r'D:\Pokered\pokecrystal-master\data\moves\moves.asm', 'r') as fp:
    for i in fp.readlines():
        if 'move' in i:
            parsed = i.strip().split(";")[0].replace(" ","").replace("move","").replace("\t","").split(",")
            if len(parsed) > 5:
                move_name = parsed[0]
                move_data = parsed[1:]
                move_data[1] = int(move_data[1])
                move_data[3] = int(move_data[3])
                move_data[4] = int(move_data[4])
                move_data[5] = int(move_data[5])
                if move_name == 'PSYCHIC_M':
                    move_name = 'PSYCHIC'
                if move_name in move_names_db:
                    moves[move_name] = {
                        'display_name': move_names_db_map[move_name],
                        'move_id': move_name,
                        'effect': move_data[0],
                        'power': move_data[1],
                        'type': move_data[2],
                        'accuracy': move_data[3],
                        'effect_chance': move_data[5],
                        'move_numeric_id': move_names.index(move_names_db_map[move_name])+1
                    }
                    
with open('mons.json', 'w') as fp:
    fp.write(json.dumps(mons))
with open('moves.json', 'w') as fp:
    fp.write(json.dumps(moves))