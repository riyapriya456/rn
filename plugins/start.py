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
       photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
       caption=f""" <b> ⍟ Hᴇʟʟᴏ Mʏ Fʀɪᴇɴᴅ {message.from_user.mention} ⍟ 
 
⍟ Mʏ Nᴀᴍᴇ Iꜱ <a href='https://t.me/kr_renamer_bot'>『 Fɪʟᴇs Rᴇɴᴀᴍᴇ Pʀᴏ 』</a> ⍟
✌︎ I Aᴍ PᴏᴡᴇʀFᴜʟ 👑 Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ  
🚀 Sᴇᴇ Mʏ Pᴏᴡᴇʀ ⚡.....!!
⚜️ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us 💖......!!! </b> """,reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[
          InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
          ],[
          InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
          InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
          ],[
          InlineKeyboardButton(' Iɴʟɪɴᴇ 🔍 Sᴇᴀʀᴄʜ ', switch_inline_query_current_chat='')
          ],[
          InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
          InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
          ]]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Your Frind Alredy Using Our Bot")
	            await message.reply_photo(
       photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
       caption=f""" <b> ⍟ Hᴇʟʟᴏ Mʏ Fʀɪᴇɴᴅ {message.from_user.mention} ⍟ 
 
⍟ Mʏ Nᴀᴍᴇ Iꜱ <a href='https://t.me/kr_renamer_bot'>『 Fɪʟᴇs Rᴇɴᴀᴍᴇ Pʀᴏ 』</a> ⍟
✌︎ I Aᴍ PᴏᴡᴇʀFᴜʟ 👑 Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ  
🚀 Sᴇᴇ Mʏ Pᴏᴡᴇʀ ⚡.....!!
⚜️ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us 💖......!!! </b> """,reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[
          InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
          ],[
          InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
          InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
          ],[
          InlineKeyboardButton(' Iɴʟɪɴᴇ 🔍 Sᴇᴀʀᴄʜ ', switch_inline_query_current_chat='')
          ],[
          InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
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
       photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
       caption=f""" <b> ⍟ Hᴇʟʟᴏ Mʏ Fʀɪᴇɴᴅ {message.from_user.mention} ⍟ 
 
⍟ Mʏ Nᴀᴍᴇ Iꜱ <a href='https://t.me/kr_renamer_bot'>『 Fɪʟᴇs Rᴇɴᴀᴍᴇ Pʀᴏ 』</a> ⍟
✌︎ I Aᴍ PᴏᴡᴇʀFᴜʟ 👑 Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ  
🚀 Sᴇᴇ Mʏ Pᴏᴡᴇʀ ⚡.....!!
⚜️ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us 💖......!!! </b> """,reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[
          InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
          ],[
          InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
          InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
          ],[
          InlineKeyboardButton(' Iɴʟɪɴᴇ 🔍 Sᴇᴀʀᴄʜ ', switch_inline_query_current_chat='')
          ],[
          InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
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
            text=f""" <b> ⍟ Hᴇʟʟᴏ Mʏ Fʀɪᴇɴᴅ {query.from_user.mention} ⍟ 
 
⍟ Mʏ Nᴀᴍᴇ Iꜱ <a href='https://t.me/kr_renamer_bot'>『 Fɪʟᴇs Rᴇɴᴀᴍᴇ Pʀᴏ 』</a>
✌︎ I Aᴍ PᴏᴡᴇʀFᴜʟ 👑 Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ  
🚀 Sᴇᴇ Mʏ Pᴏᴡᴇʀ ⚡.....!!
⚜️ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us 💖......!!! </b> """,
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
                ],[
                InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
                InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
                ],[
                InlineKeyboardButton(' Iɴʟɪɴᴇ 🔍 Sᴇᴀʀᴄʜ ', switch_inline_query_current_chat='')
                ],[
                InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
               ],[
               InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
               ],[
               InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇ", url= "https://t.me/KR_Botz"),
               InlineKeyboardButton("👨‍💻 Dᴇᴠs 🥷", callback_data = "dev")
               ],[
               InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton('๑۩ tค๓เl ۞ التاميل ۩๑', url='https://t.me/mr_tamil_kid'),
               ],[
               InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data = "about"),
               InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )
    elif data == "don":
        await query.message.edit_text(
            text=mr.DON_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton('Pᴀʏ 💰 Aᴍᴏᴜɴᴛ', url='https://t.me/mr_happy_kid_sk'),
               ],[
               InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "start"),
               InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

@Client.on_inline_query()
async def answerX(bot, update):

    answer = list()
    answer.append(InlineQueryResultArticle(title="Dᴏɴᴀᴛᴇ Pᴀʏᴍᴇɴᴛ Oʀ Hᴇʀᴏᴋ Aᴄᴄᴏᴜɴᴛ", description="Dᴏɴᴀᴛᴇ Oɴʟʏ Oɴᴇ Rᴜᴘᴇᴇ 🥲.",
    input_message_content=InputTextMessageContent(message_text=mr.DON_TXT),
    reply_markup=InlineKeyboardMarkup( [[ 
        InlineKeyboardButton("Dᴏɴᴀᴛᴇ 💳", url="https://p.paytm.me/xCTH/1icxtwpo"),
        ],[
        InlineKeyboardButton("🧛‍♂️ Aᴅᴍɪɴ", url="https://t.me/mr_tamil_kid"), 
        InlineKeyboardButton("ʜᴇʀᴏᴋ ⚜️ Aᴄᴄᴏᴜɴᴛ ", url="https://t.me/mrtamil_kid")
        ]] 
    ),
    thumb_url="https://telegra.ph/file/3d7e72118de22df4f553f.jpg") )

    answer.append(InlineQueryResultArticle(title="I Nᴇᴇᴅ Pʀɪᴠᴀᴛᴇ Bᴏᴛs  ", description="Fɪʀsᴛ Cᴏɴᴛᴀᴄᴛ Aᴅᴍɪɴ.",
    input_message_content=InputTextMessageContent(message_text=mr.PRI_TXT),
    reply_markup=InlineKeyboardMarkup( [[ 
        InlineKeyboardButton("♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎", url="https://t.me/mrtamil_kid")
        ],[
        InlineKeyboardButton("Pᴀʏ 💰 ₹80", url="https://p.paytm.me/xCTH/1icxtwpo"), 
        InlineKeyboardButton("Pᴀʏ 💰 ₹160", url="https://p.paytm.me/xCTH/1icxtwpo")
        ]]
    ),
    thumb_url="https://telegra.ph/file/25c04a16291bd879f6184.jpg") )
    try:
        await update.answer(results=answer, cache_time=0)
    except Exception as e:
        print(f"🚸 ERROR : {e}")
    except QueryIdInvalid:
        pass
