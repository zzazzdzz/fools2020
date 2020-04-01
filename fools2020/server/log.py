from resources import *
import util

class BattleLog():
    def __init__(self):
        self.log = []
        self.stringbuf = []
        self.item_to_stringbuf = {}
    
    def push(self, *args):
        self.log.append(args)

    def add_to_stringbuf(self, s):
        self.stringbuf.append(s)

    def item_stringbuf_id(self, item):
        if item not in self.item_to_stringbuf:
            self.item_to_stringbuf[item] = len(self.stringbuf)
            self.stringbuf.append(ITEM_NAMES[item])
        return self.item_to_stringbuf[item]

    def get_stringbuf(self, s):
        if not s in self.stringbuf:
            self.add_to_stringbuf(s)
        return self.stringbuf.index(s)

    def announce_item_trigger(self):
        self.log.append((BATTLE_ACTION_TRIGGER, self.cur_item))

    def announce_item_replace(self, owner, slot, item):
        self.log.append((BATTLE_ACTION_REPLACE, slot + MAX_ITEM_SLOTS - owner["string_buffer_id"] * MAX_ITEM_SLOTS, item))

    def set_current_callback_slot(self, item):
        self.cur_item = item

    def log_bytes(self):
        result = []
        for entry in self.log:
            lentry = [item for sublist in [(x,) if type(x) is not tuple else x for x in entry] for item in sublist]
            if lentry[0] == BATTLE_ACTION_MESSAGE:
                lentry[0] = BATTLE_ACTION_MESSAGE + len(lentry) - 1
            result += lentry
        result.append(0xff)
        result = [len(result) % 256, len(result) // 256] + result
        for entry in self.stringbuf:
            result += util.parse_text(entry)
        return bytes(result)

    def print(self):
        for entry in self.log:
            if entry[0] == BATTLE_ACTION_MESSAGE:
                msg_string = MESSAGES[entry[1]]
                entry = entry[2:]
                while entry:
                    tag = msg_string[msg_string.index("{")+1:msg_string.index("}")]
                    tag_str = "bepis"
                    if tag == "str_buf":
                        tag_str = self.stringbuf[entry[0]]
                        entry = entry[1:]
                    if tag == "move_name":
                        tag_str = get_move_by_numeric_id(entry[0])["display_name"]
                        entry = entry[1:]
                    if tag == "raw_int":
                        tag_str = "%s" % hex(entry[0][0] * 256 + entry[0][1]).replace("0x", "")
                        entry = entry[1:]
                    msg_string = msg_string.replace("{%s}" % tag, tag_str, 1)
                print(msg_string.replace("<B>","[").replace("</B>","]"))
            elif entry[0] == BATTLE_ACTION_TRIGGER:
                print("<item triggered, slot ID %i>" % entry[1])
            else:
                print("? %s" % repr(entry))