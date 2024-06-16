echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/Chowdhury-Siam/Jisshu-forward-bot Chowdhury-Siam/Jisshu-forward-bot 
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/Chowdhury-Siam/Jisshu-forward-bot -b $BRANCH /Jisshu-forward-bot
fi
cd Chowdhury-Siam/Jisshu-forward-bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
