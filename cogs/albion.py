import discord
import requests
import json
import difflib
from discord.ext import commands


class PriceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_url = 'https://www.albion-online-data.com/api/v2/stats/prices/'

    def item_match(self, item_name):

        itemNames = []
        itemIDs = []
        jDists = []

        response = requests.get("https://raw.githubusercontent.com/broderickhyman/ao-bin-dumps/master/formatted/items.json")
        data = response.json()

        for (i, indivData) in enumerate(data):

            try:
                w1 = item_name.lower()
                w2 = indivData["UniqueName"].lower()

                jDist = 1 - difflib.SequenceMatcher(None, w1, w2).ratio()
                jDists.append([jDist, i])

            except:
                jDists.append([1, i])

            try:
                w1 = item_name.lower()

                localDists = []
                for name in indivData["LocalizedNames"]:
                    w2 = indivData["LocalizedNames"][name].lower()

                    localDist = 1 - \
                        difflib.SequenceMatcher(None, w1, w2).ratio()
                    localDists.append(localDist)

                jDist = min(localDists)
                jDists.append([jDist, i])

            except:
                jDists.append([1, i])

        jDists = sorted(jDists)

        itemNames = [data[jDist[1]]["LocalizedNames"]["ES-ES"]
                    for jDist in jDists[:4]]
        itemIDs = [data[jDist[1]]["UniqueName"] for jDist in jDists[:4]]
        return itemIDs

    def get_price(self, item_name):
        item_names = self.item_match(item_name)
        item_name = item_names[0]
        print(item_name)
        response = requests.get(f'{self.api_url}{item_name}')
        if response.status_code == 200:
            data = response.json()
            itemData = data[1]
            price = itemData['sell_price_min']
            
            return price
        else:
            return None

    @commands.command()
    async def price(self, ctx, *, item_name: str):
        price = self.get_price(item_name)
        if price:
            await ctx.send(f'El precio de venta mínimo de {item_name} es {price}.')
        else:
            await ctx.send('No se pudo obtener el precio del item.')


async def setup(bot):
    await bot.add_cog(PriceCog(bot))
