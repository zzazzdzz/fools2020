import sqlite3
import threading

import util

TAG = "DBConnection"

db = sqlite3.connect("db.sqlite3", check_same_thread=False)
db.row_factory = sqlite3.Row

db_lock = threading.Lock()

def sql(query, params=(), log_errors=True):
    ret = []
    with db_lock:
        cur = db.cursor()
        for i in cur.execute(query, params):
            ret.append(dict(i))
        db.commit()
    return ret

def sql_readonly(query, params=(), log_errors=True):
    ret = []
    cur = db.cursor()
    for i in cur.execute(query, params):
        ret.append(dict(i))
    return ret

def get_player_data(x):
    result = sql("SELECT * FROM users WHERE sessid=?", (x,))
    if not result:
        return None
    return result[0]