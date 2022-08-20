import sqlite3

class DB():
    def __init__(self, botDb):
        self.db_name = botDb
        self.conn = sqlite3.connect(botDb)
        self.c = self.conn.cursor()

    def create_table(self, guildName):
        self.c.execute("CREATE TABLE IF NOT EXISTS {} (userId VARCHAR(255), premiumStatus VARCHAR(255), economyStatus INT)".format(guildName))

    def insert_data(self, guildName, userId, premiumStatus, economyStatus):
        self.c.execute("INSERT INTO {} VALUES ({}, {}, {})".format(guildName, userId, premiumStatus, economyStatus))
        self.conn.commit()

    def select_data(self, guildId, fields, condition):
        self.c.execute("SELECT {} FROM {} WHERE {}".format(fields, guildId, condition))
        return self.c.fetchall()

    def update_data(self, guildName, userId):
        self.c.execute("UPDATE {}".format(guildName, userId))
        self.conn.commit()

    def delete_data(self, guildId, condition):
        self.c.execute("DELETE FROM {} WHERE {}".format(guildId, condition))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()