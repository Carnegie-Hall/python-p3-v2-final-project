import sqlite3
import ipdb


CONN = sqlite3.connect("db/boba_store.db")
CURSOR = CONN.cursor()

# ipdb.set_trace()