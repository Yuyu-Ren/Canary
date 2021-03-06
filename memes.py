#!/usr/bin/env python3

# discord-py requirements
from discord.ext import commands
import asyncio

# Other utilities
import random


class Memes():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lenny(self, ctx):
        """
        Lenny face
        """
        await ctx.send("( ͡° ͜ʖ ͡°) ")
        await ctx.message.delete()

    @commands.command()
    async def license(self, ctx):
        """
        License
        """
        await ctx.send("This bot is free software: you can redistribute"
                            " it and/or modify it under the terms of the GNU"
                            " General Public License as published by the "
                            "Free Software Foundation, either version 3 of "
                            "the License, or (at your option) any later "
                            "version. **This bot is distributed in the hope "
                            "that it will be useful**, but WITHOUT ANY "
                            "WARRANTY; without even the implied warranty of "
                            "MERCHANTABILITY or **FITNESS FOR A PARTICULAR "
                            "PURPOSE**.  See the GNU General Public License "
                            "for more details. This bot is developed "
                            "primarily by student volunteers with better "
                            "things to do. A copy of the GNU General Public "
                            "License is provided in the LICENSE.txt file "
                            "along with this bot. The GNU General Public "
                            "License can also be found at "
                            "<http://www.gnu.org/licenses/>.")
        await ctx.message.delete()

    @commands.command()
    async def gohere(self, ctx):
        """
        for future mcgillians
        """
        await ctx.send("http://gph.is/1cN9wO1")
        await ctx.message.delete()

    @commands.command()
    async def tunak(self, ctx):
        """
        bitch pls
        """
        await ctx.send("http://i.imgur.com/rNNLyjK.gif")
        await ctx.message.delete()

    @commands.command()
    async def bb8(self, ctx):
        """
        nice job bb8
        """
        await ctx.send("http://i.imgur.com/SUvaUM2.gif")
        await ctx.message.delete()

    @commands.command()
    async def longtime(self, ctx):
        """
        That's a name I've not heard in a long time
        """
        await ctx.send("http://i.imgur.com/e1T1xcq.mp4")
        await ctx.message.delete()

    @commands.command()
    async def thonk(self, ctx):
        """
        when thonking consumes you
        """
        await ctx.send("https://i.imgur.com/VADGUwj.gifv")
        await ctx.message.delete()

    @commands.command()
    async def dealwithit(self, ctx):
        """
        deal with it trump
        """
        await ctx.send("http://i.imgur.com/5jzN8zV.mp4")
        await ctx.message.delete()

    @commands.command()
    async def lmao(self, ctx):
        """
        that's hilarious
        """
        await ctx.send("http://i.imgur.com/o5Cc3i2.mp4")
        await ctx.message.delete()

    @commands.command()
    async def chirp(self, ctx):
        """:^)"""
        await ctx.send('CHIRP CHIRP')

    @commands.command()
    async def mix(self, ctx, *, inputStr: str=None):
        if inputStr is None:
            await ctx.send()
        msg = "".join([(c.upper() if
                        random.randint(0, 1) else
                        c.lower()) for c in inputStr])
        await ctx.send(msg)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Memes(bot))
