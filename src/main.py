from utils.console import fore, style
from requests import get

print(f"""{fore.Magenta}
░██████╗░██████╗░░█████╗░███╗░░██╗██╗░░██╗
██╔════╝░██╔══██╗██╔══██╗████╗░██║██║░██╔╝
██║░░██╗░██████╔╝███████║██╔██╗██║█████═╝░
{fore.Bright_Magenta}██║░░╚██╗██╔══██╗██╔══██║██║╚████║██╔═██╗░
╚██████╔╝██║░░██║██║░░██║██║░╚███║██║░╚██╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝
{style.RESET_ALL}
{style.Italic + style.Bold}GITHUB: {style.RESET_ALL}https://github.com/didlly/grank
{style.Italic + style.Bold}INSTALLED VERSION: {style.RESET_ALL}v0.2.2-alpha
{style.Italic + style.Bold}LATEST VERSION: {style.RESET_ALL}{get("https://raw.githubusercontent.com/didlly/grank/main/current_version").content.decode()}
{style.Italic + style.Bold}DISCORD SERVER: {style.RESET_ALL}https://discord.com/invite/C4TMcemPTG
""")

import sys
from platform import system
from os.path import dirname
from configuration.config import load_config
from configuration.credentials import load_credentials
from threading import Thread
from utils.shared import data
from discord.message import send_message
from json import load, dumps
from scripts.crime import crime_parent
from scripts.daily import daily_parent
from scripts.beg import beg_parent
from scripts.dig import dig_parent
from scripts.fish import fish_parent
from scripts.hunt import hunt_parent
from scripts.search import search_parent
from scripts.highlow import highlow_parent
from scripts.postmeme import postmeme_parent
from scripts.trivia import trivia_parent

if getattr(sys, "frozen", False):
    cwd = dirname(sys.executable)
elif __file__:
    cwd = dirname(__file__)

if system().lower() == "windows":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

config = load_config(cwd)
credentials = load_credentials(cwd)

for index in range(len(credentials)):
    user_id = credentials[index][0]
    username = credentials[index][1]
    session_id = credentials[index][2]
    channel_id = credentials[index][3]
    token = credentials[index][4]
    data[channel_id] = True

    database = load(open(f"{cwd}/database.json", "r"))
    if f"{user_id}_confirmation" not in database.keys():
        send_message(channel_id, token, config, username, "pls settings confirmations nah")
        database[f"{user_id}_confirmation"] = True
        open(f"{cwd}/database.json", "w").write(dumps(database))

    if config["commands"]["daily"]:
        Thread(target=daily_parent, args=(username, channel_id, token, config, cwd)).start()

    if config["commands"]["beg"]:
        Thread(target=beg_parent, args=(username, channel_id, token, config)).start()

    if config["commands"]["crime"]:
        Thread(target=crime_parent, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["dig"]:
        Thread(target=dig_parent, args=(username, channel_id, token, config, user_id, cwd, session_id)).start()

    if config["commands"]["fish"]:
        Thread(target=fish_parent, args=(username, channel_id, token, config, user_id, cwd, session_id)).start()

    if config["commands"]["hunt"]:
        Thread(target=hunt_parent, args=(username, channel_id, token, config, user_id, cwd, session_id)).start()

    if config["commands"]["search"]:
        Thread(target=search_parent, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["highlow"]:
        Thread(target=highlow_parent, args=(username, channel_id, token, config, user_id, session_id)).start()

    if config["commands"]["postmeme"]:
        Thread(target=postmeme_parent, args=(username, channel_id, token, config, user_id, session_id, cwd)).start()

    if config["commands"]["trivia"]:
        Thread(target=trivia_parent, args=(username, channel_id, token, config, user_id, session_id, cwd)).start()