import discord

from discord.ext import commands
from utils.config import Config
from utils import pufferpanel

config = Config()

desc = "Server control bot for {}".format(config.name)

bot = commands.Bot(command_prefix=config.command_prefix, description=desc, pm_help=False)

class Server():
    def __init__(self, bot):
        self.bot = bot

    def is_admin(self, member:discord.Member):
        role_ids = []
        for r in member.roles:
            role_ids.append(r.id)
        if any(role_id in config.admin_role_ids for role_id in role_ids):
            return True
        else:
            return False

    @commands.command()
    async def list(self):
        """Get a list of all online players"""
        await self.bot.say(pufferpanel.get_player_list())

    @commands.command(pass_context=True)
    async def controlstatus(self, ctx, action:str):
        """Controls the server. Valid actions are start, stop, restart, and kill"""
        if not self.is_admin(ctx.message.author):
            await self.bot.say("You do not have permission to use this command.")
            return
        if action.lower() == "start" or action.lower() == "stop" or action.lower() == "restart" or action.lower() == "kill":
            await self.bot.say(pufferpanel.control_server_status(action.lower()))
            return
        await self.bot.say("Invalid action! Valid actions are `start`, `stop`, `restart`, and `kill`!")

    @commands.command(pass_context=True)
    async def sendcommand(self, ctx, *, command:str):
        """Sends a command as the console. (You do not need to put a slash)"""
        if not self.is_admin(ctx.message.author):
            await self.bot.say("You do not have permission to use this command.")
            return
        await self.bot.say(pufferpanel.send_console_command(command))

    @commands.command()
    async def getstatus(self):
        """Checks if the server is online or not"""
        await self.bot.say(pufferpanel.get_server_status())

bot.add_cog(Server(bot))

@bot.event
async def on_ready():
    print("Connected! Logged in as {}/{}".format(bot.user, bot.user.id))

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        return
    try:
        await bot.send_message(ctx.message.channel, error)
    except:
        pass
    print("An error occured while executing the command named {}: {}".format(ctx.command.qualified_name, error))

print("Connecting...")
bot.run(config._token)
