import sqlite3

class DB():
    def __init__(self, botDb):
        self.db_name = botDb
        self.conn = sqlite3.connect(botDb)
        self.c = self.conn.cursor()

    def create_table(self, guild_name):
        self.c.execute("CREATE TABLE IF NOT EXISTS {} (id TEXT, data TEXT)".format(guild_name))

    def insert_data(self, guild_id, data):
        self.c.execute("INSERT INTO {} VALUES ({})".format(guild_id, data))
        self.conn.commit()

    def select_data(self, guild_id, fields, condition):
        self.c.execute("SELECT {} FROM {} WHERE {}".format(fields, guild_id, condition))
        return self.c.fetchall()

    def update_data(self, guild_id, fields, condition):
        self.c.execute("UPDATE {} SET {} WHERE {}".format(guild_id, fields, condition))
        self.conn.commit()

    def delete_data(self, guild_id, condition):
        self.c.execute("DELETE FROM {} WHERE {}".format(guild_id, condition))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()