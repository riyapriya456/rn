import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5377834462:AAHMIicrsgAhYS4_bKnp2tLHwg9U4eilRnE")

API_ID = int(os.environ.get("API_ID", "13384432"))

API_HASH = os.environ.get("API_HASH", "ea9db4503ed7088b788e06dfd818e00e")

STRING = os.environ.get("STRING", "BQDMOvAAtCL0AccvASgo8J9mPqZUsZn2_kdxMSoHDOMD0j4m1PyNPdMdHvg_frq1psssdtKbEnjNyK41nqV-QmyScKmSOmIomNuS87QkcqBOk4cZYhn5hSZxREAd6kBrc3Mmrqo7IvnVbkQBmHvyIWVmIhUV_HsVw81mM6vLCBYOhoaVw7AR4pdsX7n8ugaYsavw-H5NMwfCVjsi4TITG5tFsx2CngQn-f5CGEigeEIVhVBPB8u9eV9Sdc5w3IGhV9J6oD2ZQXeXou8rI1y9-p5LEQS3uthcgXernvRK0jm8liTTW-sm24djVh9GeJaUnlauqwldnI25opf6eWGNqk7-ThLV4AAAAABZsWSfAA")


botssss = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,botssss]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    botssss.run()
