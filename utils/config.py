import os
import configparser

class Defaults:
    name = "a minecraft server"
    token = None
    command_prefix = "srv!"
    admin_role_ids = []
    xas = None
    xat = None
    puffer_url = None

class Config:
    def __init__(self):

        self.config_file = "config.ini"

        config = configparser.ConfigParser(interpolation=None)
        config.read(self.config_file, encoding="utf-8")

        sections = {"Bot", "PufferPanel"}.difference(config.sections())
        if sections:
            print("Could not load a section in the config file, please obtain a new config file from the github repo")
            os._exit(1)
        self.name = config.get("Bot", "Name", fallback=Defaults.name)
        self._token = config.get("Bot", "Token", fallback=Defaults.token)
        self.command_prefix = config.get("Bot", "Command_Prefix", fallback=Defaults.command_prefix)
        self.admin_role_ids = config.get("Bot", "Admin_Role_IDs", fallback=Defaults.admin_role_ids)
        self.xas = config.get("PufferPanel", "X-Access-Server", fallback=Defaults.xas)
        self.xat = config.get("PufferPanel", "X-Access-Token", fallback=Defaults.xat)
        self.puffer_url = config.get("PufferPanel", "URL", fallback=Defaults.puffer_url)

        self.check()

    def check(self):
        if not self._token:
            print("No token was specified in the config, please put your bot's token in the config.")
            os._exit(1)

        if len(self.admin_role_ids) is not 0:
            try:
                self.admin_role_ids = list(self.admin_role_ids.split())
            except:
                self.admin_role_ids = Defaults.admin_role_ids

        if not self.xas:
            print("No X-Access-Server was specified in the config")
            os._exit(1)

        if not self.xat:
            print("No X-Access-Token was specified in the config")
            os._exit(1)

        if not self.puffer_url:
            print("No PufferPanel url was specified in the config")
            os._exit(1)
