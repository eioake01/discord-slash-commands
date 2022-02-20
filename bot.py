import os
import interactions
from dotenv import load_dotenv

def spawn_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    bot = interactions.Client(token=TOKEN)

    @bot.command(
        name="woof",
        description="Say woof!"
    )
    async def woof(ctx):
        await ctx.send(f"Woof woof 🐕")


    @bot.command(
        name="meow",
        description="Say meow!"
    )
    async def meow(ctx):
        await ctx.send("Meoooww 🐈")
    
    bot.start()


if __name__ == '__main__':
    spawn_bot()
    