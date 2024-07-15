from helper.bot_factory import BotFactory

from api.requests import APIRequests
from helper.bot_service import BotService
from config.config_files import APIkeys

def main():
    DEPLOYMENT = APIkeys.deployment

    api_requests = APIRequests()
    
    bot_service = BotService(api_requests)
    
    bot = BotFactory.create_bot(DEPLOYMENT, bot_service)

    bot.run()


if __name__ == '__main__':
    main()