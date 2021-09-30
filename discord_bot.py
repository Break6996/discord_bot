BOT_PREFIX = "BOT_PREFIX"
BOT_TOKEN = "BOT_TOKEN"
Channel_ID1 = Channel_ID1

import discord
from discord.ext import commands
import logging
from discord.ext.commands.errors import ExtensionAlreadyLoaded

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(
    command_prefix=BOT_PREFIX,
    intents=discord.Intents().all()
)

@bot.event
async def on_ready():
    print(">>bot was online<<")
    await bot.get_channel(Channel_ID1).send('祖安bot已启动 \nxdm今天司马了吗')

@bot.event
async def on_member_join(member):
    await bot.get_channel(Channel_ID1).send(f'欢迎 {member.name} 加入 ━(*｀∀´*)ノ亻!')

@bot.event
async def on_member_remove(member):
    await bot.get_channel(Channel_ID1).send(f'{member.name}已退出服务器')

@bot.command(name = 'test')
async def test(ctx):
    await ctx.send('爬')

bot.run(BOT_TOKEN)
