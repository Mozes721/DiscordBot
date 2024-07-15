from bot.discord import DiscordBot
from bot.local_bot import LocalBot

class BotFactory:
    @staticmethod
    def create_bot(deployment, service):
        if deployment:
            return DiscordBot(service)
        else:
            return LocalBot()
