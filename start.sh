echo "Cloning Repository"
git clone https://github.com/KR-BOTZ/KR-RENAMER-BOT1 /KR-RENAMER-BOT1
cd /KR-RENAMER-BOT1 
echo "installing requirements"
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
