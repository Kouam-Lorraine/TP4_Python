import os
from pydoc import doc

from dotenv import load_dotenv

from discord.ext import commands

from argparse import ArgumentParser, Namespace

load_dotenv(dotenv_path="config")

class DocBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")
        #self.log.infolog(f"{self.user} has connected to Discord!")

    async def parse_args(self) -> Namespace:
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()

doc_bot = DocBot()
doc_bot.parse_args()
doc_bot.run(os.getenv("TOKEN"))
#if doc_bot.parse_args():
    #doc_bot.run(os.getenv("TOKEN"))