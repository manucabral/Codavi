import discord
import os
import datetime
import requests as req
import base64
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

bot = commands.Bot(command_prefix=os.environ.get(
    'BOT_PREFIJO'), description='Covid')
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-comandos"))
    print('Codavi bot iniciado correctamente.')


@bot.command()
async def comandos(contexto):
    descripcion = """
    > -vacunas <dosis> | Cantidad de vacunas aplicadas por marca.\n
    """
    embed = discord.Embed(
        title="Comandos", description=descripcion,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.green(),
        url="https://github.com/manucabral/Codavi/blob/main/codavi_portada.png"
    )

    embed.set_footer(text=f"Comando solicitado por: {contexto.author.name}")
    # embed.set_author(
    #    name="ne0de",
    #    icon_url="https://avatars.githubusercontent.com/u/83357673?v=4")
    await contexto.send(embed=embed)


async def error(contexto, mensaje):
    embed = discord.Embed(
        title="Error de comando", description=mensaje,
        timestamp=datetime.datetime.utcnow(),
        color=discord.Color.red()
    )
    await contexto.send(embed=embed)


@bot.command()
async def vacunas(contexto, *args):
    if len(args) == 0:
        await error(contexto, 'Especifica la dosis.\nUtiliza: -vacunas <dosis>')
    else:
        dosis = args[0]
        if int(dosis) > 2:
            await error(contexto, f'No existe la dosis {dosis}.')
        else:
            await contexto.send("Cargando..")
            res = req.get(f'http://localhost:5000/vacunas/{dosis}')
            data = res.json()
            filename = data['titulo'] + '.jpg'
            descripcion = f"""
                > Sputnik: {data['data']['Sputnik']['total']:,}\n
                > AstraZeneca: {data['data']['AstraZeneca']['total']:,}\n
                > Sinopharm: {data['data']['Sinopharm']['total']:,}\n
                > Moderna: {data['data']['Moderna']['total']:,}\n
                > Covishield: {data['data']['Covishield']['total']:,}\n
            """
            imgdata = base64.b64decode(data['grafico'])
            with open(filename, 'wb') as f:
                f.write(imgdata)

            embed = discord.Embed(
                title=data['titulo'], description=descripcion,
                timestamp=datetime.datetime.utcnow(),
                color=discord.Color.green()
            )
            embed.set_footer(
                text=f"Comando solicitado por: {contexto.author.name}")
            file = discord.File(filename, filename=filename)
            await contexto.send(embed=embed, file=file)


@bot.command()
async def ping(contexto):
    await contexto.send('pong')

bot.run(os.environ.get('BOT_TOKEN'))
