import discord, os, datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix=os.environ.get(
    'BOT_PREFIJO'), description='Covid')
bot.remove_command('help')


async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help"))
    print('Codavi bot iniciado correctamente.')


@bot.command()
async def help(contexto):
    descripcion = """
    > -vacunas <dosis> | Cantidad de vacunas aplicadas por marca.\n
    """
    embed = discord.Embed(
        title="Comandos", description=descripcion,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.red()
    )

    embed.set_footer(text=f"Comando solicitado por: {contexto.author.name}")
    # embed.set_author(
    #    name="ne0de",
    #    icon_url="https://avatars.githubusercontent.com/u/83357673?v=4")
    await contexto.send(embed=embed)


@bot.command()
async def ping(contexto):
    await contexto.send('pong')

bot.run(os.environ.get('BOT_TOKEN'))
