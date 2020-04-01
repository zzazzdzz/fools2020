
MSG_BATTLE_PLACEHOLDER:
    text "bepis"
    tx_wait 69
    done

MSG_BATTLE_USED:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> used"
    next "<B>"
    tx_buf_id_indirect 3
    text "</B>!"
    tx_wait 30
    done

MSG_BATTLE_FIRST:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> gets the"
    next "chance to strike first!"
    tx_wait 60
    done

MSG_BATTLE_NORMAL_DAMAGE:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> took <B>"
    tx_num wCurrentBattleCommand + 3
    text "</B> damage!"
    tx_wait 60
    done

MSG_BATTLE_CRIT:
    text "Critical hit!"
    tx_wait 30
    done

MSG_BATTLE_SUPER_EFFECTIVE:
    text "It's super effective!"
    tx_wait 30
    done

MSG_BATTLE_NOT_VERY_EFFECTIVE:
    text "Not very effective..."
    tx_wait 30
    done

MSG_BATTLE_INEFFECTIVE:
    text "It has little effect..."
    tx_wait 30
    done

MSG_BATTLE_FAINTED:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> fainted!"
    tx_wait 60
    done

MSG_BATTLE_ATTACK_MISSED:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B>'s attack missed!"
    tx_wait 60
    done

MSG_BATTLE_ATTACK_AVOIDED:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> avoided the attack!"
    tx_wait 60
    done

MSG_BATTLE_EFFECT_DAIKATANA_PHYSICAL:
    text "Took additional <B>"
    tx_num wCurrentBattleCommand + 2
    text "</B> damage"
    next "from <B>"
    tx_buf_id_indirect 4
    text "</B>! "
    tx_wait 60
    done

MSG_BATTLE_EFFECT_DAIKATANA_SPECIAL:
    text "Accuracy boosted due to"
    next "effects of <B>"
    tx_buf_id_indirect 2
    text "</B>!"
    tx_wait 60
    done

MSG_BATTLE_EFFECT_ROWHAMMER:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> was increased"
    next "by <B>"
    tx_num wCurrentBattleCommand + 3
    text "</B>!"
    tx_wait 60
    done

MSG_BATTLE_EFFECT_WON:
    text "Battle was won due to"
    next "effects of <B>"
    tx_buf_id_indirect 2
    text "</B>!"
    tx_wait 60
    done

MSG_BATTLE_RECOVERED:
    text "Recovered <B>"
    tx_num wCurrentBattleCommand + 2
    text "</B> HP"
    next "with <B>"
    tx_buf_id_indirect 4
    text "</B>!"
    tx_wait 60
    done

MSG_BATTLE_REDUCED:
    text "The damage was reduced"
    next "by <B>"
    tx_buf_id_indirect 2
    text "</B>!"
    tx_wait 60
    done

MSG_BATTLE_TRIGGER_COUNT:
    text "Trigger count for this"
    next "effect is <B>"
    tx_num wCurrentBattleCommand + 2
    text "</B>."
    tx_wait 60
    done

MSG_BATTLE_LOST_HP:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> lost some"
    next "of its HP!"
    tx_wait 60
    done

MSG_BATTLE_LAGGING_TAIL:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> is lagging"
    next "behind!"
    tx_wait 60
    done

MSG_BATTLE_ENDURED:
    text "The attack was barely"
    next "endured!"
    tx_wait 60
    done

MSG_BATTLE_FLINCHING:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B> flinched"
    next "and couldn't move!"
    tx_wait 60
    done

MSG_BATTLE_B2B:
    text "Back-To-Back counter is"
    next "currently <B>"
    tx_num wCurrentBattleCommand + 2
    text "</B>."
    tx_wait 60
    done

MSG_BATTLE_STACKS:
    text "This effect is currently"
    next "at <B>"
    tx_num wCurrentBattleCommand + 2
    text "</B> stacks."
    tx_wait 60
    done

MSG_BATTLE_STAT_CHANGES:
    text "All stat changes from this"
    next "item were eliminated."
    tx_wait 60
    done

MSG_BATTLE_NO_CHOICE:
    text "<B>"
    tx_buf_id_indirect 2
    text "</B>'s effect"
    next "has no valid targets."
    done

MSG_BATTLE_TURN_LIMIT_1:
    text "Something's stirring..."
    tx_wait 100
    done

MSG_BATTLE_TURN_LIMIT_2:
    text "Something's approaching..."
    tx_wait 100
    done

MSG_BATTLE_TURN_LIMIT_3:
    text "It's getting closer!"
    tx_wait 100
    done

MSG_BATTLE_SUDDEN_DEATH:
    text "It's right nearby!"
    next "It's gusting hard!"
    tx_wait 60
    done

BattleMessagePointers:
    dw MSG_BATTLE_PLACEHOLDER
    dw MSG_BATTLE_USED
    dw MSG_BATTLE_FIRST
    dw MSG_BATTLE_NORMAL_DAMAGE
    dw MSG_BATTLE_PLACEHOLDER
    dw MSG_BATTLE_CRIT
    dw MSG_BATTLE_SUPER_EFFECTIVE
    dw MSG_BATTLE_NOT_VERY_EFFECTIVE
    dw MSG_BATTLE_INEFFECTIVE
    dw MSG_BATTLE_PLACEHOLDER
    dw MSG_BATTLE_FAINTED
    dw MSG_BATTLE_ATTACK_MISSED
    dw MSG_BATTLE_ATTACK_AVOIDED
    dw MSG_BATTLE_EFFECT_DAIKATANA_PHYSICAL
    dw MSG_BATTLE_EFFECT_DAIKATANA_SPECIAL
    dw MSG_BATTLE_EFFECT_ROWHAMMER
    dw MSG_BATTLE_EFFECT_WON
    dw MSG_BATTLE_RECOVERED
    dw MSG_BATTLE_REDUCED
    dw MSG_BATTLE_TRIGGER_COUNT
    dw MSG_BATTLE_LOST_HP
    dw MSG_BATTLE_LAGGING_TAIL
    dw MSG_BATTLE_ENDURED
    dw MSG_BATTLE_FLINCHING
    dw MSG_BATTLE_B2B
    dw MSG_BATTLE_STACKS
    dw MSG_BATTLE_STAT_CHANGES
    dw MSG_BATTLE_NO_CHOICE
    dw MSG_BATTLE_TURN_LIMIT_1
    dw MSG_BATTLE_TURN_LIMIT_2
    dw MSG_BATTLE_TURN_LIMIT_3
    dw MSG_BATTLE_SUDDEN_DEATH
    dw MSG_BATTLE_PLACEHOLDER
    dw MSG_BATTLE_PLACEHOLDER
    dw MSG_BATTLE_PLACEHOLDER
    dw MSG_BATTLE_PLACEHOLDER