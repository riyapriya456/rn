import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply,CallbackQuery)
import humanize
from helper.progress import humanbytes
from helper.txt import kr

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"KR_BOtz")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","BQDMOvAAtCL0AccvASgo8J9mPqZUsZn2_kdxMSoHDOMD0j4m1PyNPdMdHvg_frq1psssdtKbEnjNyK41nqV-QmyScKmSOmIomNuS87QkcqBOk4cZYhn5hSZxREAd6kBrc3Mmrqo7IvnVbkQBmHvyIWVmIhUV_HsVw81mM6vLCBYOhoaVw7AR4pdsX7n8ugaYsavw-H5NMwfCVjsi4TITG5tFsx2CngQn-f5CGEigeEIVhVBPB8u9eV9Sdc5w3IGhV9J6oD2ZQXeXou8rI1y9-p5LEQS3uthcgXernvRK0jm8liTTW-sm24djVh9GeJaUnlauqwldnI25opf6eWGNqk7-ThLV4AAAAABZsWSfAA")
log_channel = int(os.environ.get("LOG_CHANNEL","-1001580040547"))
token = os.environ.get('TOKEN','5377834462:AAHMIicrsgAhYS4_bKnp2tLHwg9U4eilRnE')
botid = token.split(':')[0]

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Good morning."
elif 12 <= currentTime.hour < 12:
	wish = 'Good afternoon.'
else:
	wish = 'Good evening.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_photo(
       photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
       caption=f""" <b> Hᴇʟʟᴏ 👋 {message.from_user.mention} I Aᴍ 🧛‍♂️ Fɪʟᴇs Rᴇɴᴀᴍᴇʀ Bᴏᴛ + Fɪʟᴇ 2 Vɪᴅᴇᴏ Cᴏɴᴇʀᴛᴇʀ BOT Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ 💞....!!
 Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us......!!! 🦋 </b> 🤩 """,reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[
         InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url='https://t.me/KR_Admin_Bot')
         ],[
         InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/KR_botz'),
         InlineKeyboardButton('ℹ️ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/+9o1NJzs67xc5ODA1')
         ],[
         InlineKeyboardButton('💡 Hᴇʟᴘ', callback_data='help'),
         InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
         ]]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Your Frind Alredy Using Our Bot")
	            await message.reply_photo(
       photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
       caption=f""" <b> Hᴇʟʟᴏ 👋 {message.from_user.mention} I Aᴍ 🧛‍♂️ Fɪʟᴇs Rᴇɴᴀᴍᴇʀ Bᴏᴛ + Fɪʟᴇ 2 Vɪᴅᴇᴏ Cᴏɴᴇʀᴛᴇʀ BOT Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ 💞....!!
 Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us......!!! 🦋 </b> 🤩 """,reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[
         InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url='https://t.me/MrTamil_KiD')
         ],[
         InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/KR_botz'),
         InlineKeyboardButton('ℹ️ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/+9o1NJzs67xc5ODA1')
         ],[
         InlineKeyboardButton('💡 Hᴇʟᴘ', callback_data='help'),
         InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
         ]]))
	        except:
	             return
	    else:
	         await client.send_message(id,"Congrats! You Won 100MB Upload limit")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 104857600
	         uploadlimit(int(id),new_limit)
	         await message.reply_photo(
       photo="https://telegra.ph/file/e954574ef60c1790caa79.jpg",
       caption=f""" <b> Hᴇʟʟᴏ 👋 {message.from_user.mention} I Aᴍ 🧛‍♂️ Fɪʟᴇs Rᴇɴᴀᴍᴇʀ Bᴏᴛ + Fɪʟᴇ 2 Vɪᴅᴇᴏ Cᴏɴᴇʀᴛᴇʀ BOT Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ 💞....!!
 Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us......!!! 🦋 </b> 🤩 """,reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[
         InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url='https://t.me/KR_Admin_Bot')
         ],[
         InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/KR_botz'),
         InlineKeyboardButton('ℹ️ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/+9o1NJzs67xc5ODA1')
         ],[
         InlineKeyboardButton('💡 Hᴇʟᴘ', callback_data='help'),
         InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
         ]]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__You are not subscribed my channel__** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Support 🇮🇳" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       
       bot_data = find_one(int(botid))
       prrename = bot_data['total_rename']
       prsize = bot_data['total_size']
       user_deta = find_one(user_id)
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       	user_type = user_deta["usertype"]
       except:
           await message.reply_text("database has been Cleared click on /start")
           return
           
           
       c_time = time.time()
       
       if user_type=="Free":
           LIMIT = 600
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
           		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f" sᴏʀʀʏ! I ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ᴛʜᴀᴛ ᴀʀᴇ ʟᴀʀɢᴇʀ ᴛʜᴀɴ {humanbytes(limit)}. ғɪʟᴇ sɪᴢᴇ ᴅᴇᴛᴇᴄᴛᴇᴅ {humanbytes(file.file_size)}\n ᴜsᴇᴅ ᴅᴀʟʏ ʟɪᴍɪᴛ {humanbytes(used)} ɪғ ᴜ ᴡᴀɴᴛ ᴛᴏ ʀᴇɴᴀᴍᴇ ʟᴀʀɢᴇ ғɪʟᴇ ᴜᴘɢʀᴀᴅᴇ ʏᴏᴜʀ ᴘʟᴀɴ ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton(" ᴜᴘɢʀᴀᴅᴇ 💰💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ᴍᴏʀᴇ ᴛʜᴇɴ {humanbytes(limit)} ᴜsᴇᴅ ᴅᴀʟʏ ʟɪᴍɪᴛ {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("ᴜᴘɢʀᴀᴅᴇ 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ",callback_data = "rename"),InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            uploadlimit(message.from_user.id,2147483648)
       		            usertype(message.from_user.id,"Free")
	
       		            await message.reply_text(f'ʏᴏᴜʀ ᴘʟᴀɴᴇ ᴇxᴘɪʀᴇᴅ ᴏɴ {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("ᴄᴀɴ'ᴛ ᴜᴘʟᴏᴀᴅ ғɪʟᴇs ʙɪɢɢᴇʀ ᴛʜᴀɴ 2GB ")
       		          	return
       		else:
       		    if buy_date:
       		        pre_check = check_expi(buy_date)
       		        if pre_check == False:
       		            uploadlimit(message.from_user.id,2147483648)
       		            usertype(message.from_user.id,"Free")
       		        
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ",callback_data = "rename"),
       		InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ",callback_data = "cancel")  ]]))
       		

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=kr.START_TXT,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url='https://t.me/KR_Admin_Bot')
                ],[
                InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/KR_botz'),
                InlineKeyboardButton('ℹ️ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/+9o1NJzs67xc5ODA1')
                ],[
                InlineKeyboardButton('💡 Hᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=kr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='dev')
               ],[
               InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=kr.ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='dev')
               ],[
               InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=kr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton('Pᴀʏ 💰 Aᴍᴏᴜɴᴛ', url='https://t.me/happy_kid_sk'),
               ],[
               InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("❌ Cʟᴏsᴇ ❌", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

