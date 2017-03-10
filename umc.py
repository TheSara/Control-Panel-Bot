import requests
import json
import discord

bot = commands.Bot(command_prefix='u!', description="Server Control for a Discord guild named UnraveledMC." pm_help=False)
token = ''
xas = '' #Server Access
xat = '' #Server Token

class UnraveledMC():

    def __init__(self, bot):
        self.bot = bot

    def send_request():
        try:
            r = requests.get(
                url = "https//panel.unraveledmc.com:5656/server",
                headers = {
                "X-Access-Server":xas,
                "X-Access-Token":xat,
                },
            )
            print('Response HTTP Status Code   : {status_code}'.format(status_code=r.status_code))
            print('Response HTTP Response Body : {content}'.format(content=r.content))
        except requests.exceptions.RequestException as e:
            print('HTTP Request failed')

        @commands.command(pass_context=True)
        async def serverstatus(self, ctx):
            """Checks the status of the server."""
            r = requests.get(
                url = "https//panel.unraveledmc.com:5656/server",
                headers = {
                "X-Access-Server":xas,
                "X-Access-Token":xat,
                },
                )
            if ass = json.load(r.content):
                if r.status_code == 200:
                    await self.bot.say("Connection Sucessful, 200 OK")
                    if d['status'] == "0":
                        await self.bot.say("Server Status: ***ONLINE***\n")
                elif r.status_code =! 200:
                    if len(d['message']) => 1:
                    await self.bot.say("Couldn't complete request. Message provided: " + d['message'] + " Provided status code `" + r.status_code + "`")
            else:
                await self.bot.say("Unable to load JSON data.")

        @commands.command(pass_context=True)
        async def servercontrol(self, ctx, status: str):
            """Change the status of the server, as in killing it, starting it, stopping it, etc."""
            r = requests.get(
                url = "https//panel.unraveledmc.com:5656/server/power/{}".format(status),
                headers = {
                "X-Access-Server":xas,
                "X-Access-Token":xat,
                },
                )
            if status is "on" or "off" or "start" or "kill":
                if r.content == None:
                    await self.bot.say("204 No content, sent command `" + status + "` to the server.")
            else:
                await self.bot.say("Wrong parameter. The only parameters are `on`, `off`, `start`, and `kill`.")

        @commands.command(pass_context=True)
        async def serverlogs(self, ctx, lines: int):
            """Aquire the lines of logs you want to get from the server."""
        logs = str(lines)
            r = requests.get(
                url = "https//panel.unraveledmc.com:5656/server/log/{}".format(lines),
                headers = {
                "X-Access-Server":xas,
                "X-Access-Token":xat,
                },
                )
            if lines =< 250:
                await self.bot.say(r.content)
            else:
                await self.bot.say("Restricted to less than 250 lines. Try something smaller. If there's an error saying that there's a bad request, please notify a bot developer for more info.")

        @commands.command(pass_context=True)
        async def listplayers(self, ctx):
            """List players in UnraveledMC."""
            stuff = [p["name"] for p in requests.get("https://scales.bakunet.me:8443/server", headers={"X-Access-Server":xas, "X-Access-Token":xat}).json()["query"]["players"]]
            return #unfinished
            

bot.run(token)
