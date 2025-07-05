from bot import Bot
import asyncio

if __name__ == "__main__":
    bot = Bot()
    asyncio.run(bot.start())
