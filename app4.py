import sqlite3

conn = sqlite3.connect("pokemon.db")
c = conn.cursor()


c.execute("ALTER TABLE pokemon ADD COLUMN count INTEGER DEFAULT 0")

conn.commit()

conn.close()
