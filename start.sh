echo "Cloning Repository"
git clone https://github.com/KR-BOTZ/kr-renamer-bot /kr-renamer-bot
cd /kr-renamer-bot 
echo "installing requirements"
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
