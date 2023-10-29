import discord
from discord.ext import tasks, commands
import asyncio
from MNOG2Chars import generateMatoran, isMatoran
import os
import SecretSauce

intents = discord.Intents.default()
intents.typing = False
intents.members = True

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

cooldowns = {}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def matoran(ctx, torsoC, footC, eyesC, maskC, maskName):
    createdAt = ctx.message.created_at
    authorID  = ctx.author.id
    if authorID in cooldowns and (createdAt - cooldowns[authorID]).seconds < 15:
        await ctx.send("Please wait up to 15 seconds before you're generating another matoran.")
        return
    maskName = maskName.lower()
    isValid, torsoC, footC, eyesC, maskC = isMatoran(torsoC, footC, eyesC, maskC, maskName)
    if not isValid:
        return
    #create matoran image, save it so it can get uploaded and then delete it, also add to cooldown:
    matoranImg = generateMatoran(torsoC, footC, eyesC, maskC, maskName)
    savePath = "matoran/"+createdAt.now().strftime("%y_%m_%d_%H_%M_%S")+"_"+str(authorID)+".png"
    matoranImg.save(savePath)
    await ctx.send(file=discord.File(savePath))
    cooldowns[authorID] = createdAt
    os.remove(savePath)

#key goes here
bot.run(SecretSauce.get())