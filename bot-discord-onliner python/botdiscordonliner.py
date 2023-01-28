import time
import os
bot=0
repeat2=0
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
    print("Discord Bot Onliner")
    print("")
    print("")
    print("")
    print("[1] Set Token")
    print("[2] Bot online")
    print("[3] Exit")
    command=input(">")
    if command=="1":
        print("Bot token")
        tokenin=input(">")
        tokentxt=open("token", "w")
        tokentxt.write(tokenin)
        tokentxt.close()
        os.system("cls")
        print("Token set!")
        time.sleep(1.5)
        os.system("cls")
    elif command=="2":
        os.system("cls")
        readtoken= open("token", "r")
        token=readtoken.read()
        readtoken.close()
        os.system("title Discord Bot Onliner - Bot On")
        bot.run(token)
        os.system("cls")
        exit()
    elif command=="3":
        exit()
    else:
        os.system("cls")