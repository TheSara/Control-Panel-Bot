import requests

from utils.config import Config

config = Config()
xas = config.xas
xat = config.xat
url = config.puffer_url

def get_player_list():
    players = requests.get("{}/server".format(url), headers={"X-Access-Server":xas, "X-Access-Token":xat}).json()["query"]["players"]
    list = []
    for p in players:
        list.append(p["name"])
    if len(list) == 0:
        list = "```There are no players online```"
    else:
        list = "```{}```".format(", ".join(list))
    return list

def control_server_status(action):
    r = requests.get("{}/server/power/{}".format(url, action), headers={"X-Access-Server":xas, "X-Access-Token":xat})
    if r.status_code == 204:
        return "Successfully {}ed the server".format(action)
    else:
        return "Failed to {} the server".format(action)

def send_console_command(command):
    r = requests.post("{}/server/console".format(url), headers={"X-Access-Server":xas, "X-Access-Token":xat}, data={"command":command})
    if r.status_code == 204:
        return "Command successfully sent"
    else:
        return "Failed to send command"

def get_server_status():
    status = requests.get("{}/server".format(url), headers={"X-Access-Server":xas, "X-Access-Token":xat}).json()["status"]
    if status == 1:
        status = "online"
    else:
        status = "offline"
    return "The server is currently **{}**".format(status)

