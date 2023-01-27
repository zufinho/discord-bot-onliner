import time
import os
bot=0
try:
    import discord
    from discord.ext import commands
except:
    os.system("pip install discord.py")
os.system("title Discord Bot onliner")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
while True:
    print("Discord Bot onliner")
    print("")
    print("")
    print("")
    print("[1] Set Token")
    print("[2] Bot online")
    print("[3] Exit")
    command=input(">")
    if command=="1":
        print("Bot token")
        token=input(">")
        tokentxt=open("token", "w")
        tokentxt.write(token)
        tokentxt.close()
        os.system("cls")
        print("Token set!")
        time.sleep(1.5)
        os.system("cls")
    elif command=="2":
        tokenread = open("token", "r")
        os.system("title Discord Bot onliner - bot on")
        bot.run(tokenread.read())
        tokenread.close()
        os.system("title Discord Bot onliner")
        os.system("cls")
    elif command=="3":
        exit()
    else:
        os.system("cls")