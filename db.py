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

    def get_premium_status(self, guildId, userId):
        self.c.execute("SELECT premiumStatus FROM {} WHERE userId = {}".format(guildId, userId))
        return self.c.fetchone()[0]

    def get_economy_status(self, guildId, userId):
        self.c.execute("SELECT economyStatus FROM {} WHERE userId = {}".format(guildId, userId))
        return self.c.fetchone()[0]

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()