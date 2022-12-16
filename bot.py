import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5860785519:AAGLJ9ionJJvRWq2EV8lfo6TlSvZ9JDgaUY")

API_ID = int(os.environ.get("API_ID", "25712813"))

API_HASH = os.environ.get("API_HASH", "c201751b80c7d185f986141cbadc4275")

STRING = os.environ.get("STRING", "BQApDlTNdmaNTBMmrScFkFQQfqSlIcgQ7PkNOH6O4_mLeK2EBWfc_CxOYR6VQVNkwk8j10bXswsk6s8dmwD2XDKTob6PWI_DKLiAUrRIUduIeCP-RD3zZ_CNIhRh_t6TCuPqN9c8treQvTrsQn2RQK4ucnYmCT6kyozioM_uCRiQMKHyB8iCnKOblU9XIE9zEQZlTUmM7gURBKBlf-X_f4QBwhaSK1EJYsimtBgwXOjbqZA69BPGrM9IvL1JBSJNbDGrCQFb24IoWqDB2R8zUUB4O2GfmyQHhWgK3itMIz9pwWuI_kb44lX7EN8Xg_zlHTqLmjPj1Kcn9LTYPjMhihDgAAAAAUd3TLwA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
