import asyncio
from random import choice

import aiohttp
import discord
from redbot.core import commands

# API's and icons
MARTINE_API = "https://api.martinebot.com/v1/images/subreddit?name="
MARTINE_ICON = "https://cdn.martinebot.com/current/website-assets/avatar.png"
NEKOS_API = "https://nekos.best/"

SPACE = [
    "spaceporn",
    "astrophotography",
]


class Images(commands.Cog):
    """Image cog that shows images."""

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __version__ = "3.0.2"
    __author__ = ["MAX"]

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    @commands.command(aliases=["astro"])
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def space(self, ctx):
        """Send a random space images."""
        async with ctx.typing():
            await asyncio.sleep(0.1)
        async with aiohttp.ClientSession() as session:
            async with session.get(MARTINE_API + choice(SPACE)) as resp:
                if resp.status == 410:
                    return await ctx.send("Failed to fetch API. Unknown error.")
                if resp.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                response = await resp.json()
            embed = discord.Embed(
                title=response["data"].get("title", "[No Title]"),
                url=response["data"]["post_url"],
                description=f"Posted by: {response['data']['author']['name']}",
            )
            embed.set_footer(
                text=f"Powered by martinebot.com API | Upvotes {response['data']['upvotes']}",
                icon_url=MARTINE_ICON,
            )
            embed.colour = await ctx.embed_color()
            embed.set_image(url=response["data"]["image_url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def earth(self, ctx):
        """Send a random earth images."""
        async with aiohttp.ClientSession() as session:
            async with session.get(MARTINE_API + "earthporn") as resp:
                if resp.status == 410:
                    return await ctx.send("Failed to fetch API. Unknown error.")
                if resp.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                response = await resp.json()
            embed = discord.Embed(
                title=response["data"].get("title", "[No Title]"),
                url=response["data"]["post_url"],
                description=f"Posted by: {response['data']['author']['name']}",
            )
            embed.set_footer(
                text=f"Powered by martinebot.com API | Upvotes {response['data']['upvotes']}",
                icon_url=MARTINE_ICON,
            )
            embed.colour = await ctx.embed_color()
            embed.set_image(url=response["data"]["image_url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def critique(self, ctx):
        """Send a random Critique images."""
        async with aiohttp.ClientSession() as session:
            async with session.get(MARTINE_API + "photocritique") as resp:
                if resp.status == 410:
                    return await ctx.send("Failed to fetch API. Unknown error.")
                if resp.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                response = await resp.json()
            embed = discord.Embed(
                title=response["data"].get("title", "[No Title]"),
                url=response["data"]["post_url"],
                description=f"Posted by: {response['data']['author']['name']}",
            )
            embed.set_footer(
                text=f"Powered by martinebot.com API | Upvotes {response['data']['upvotes']}",
                icon_url=MARTINE_ICON,
            )
            embed.colour = await ctx.embed_color()
            embed.set_image(url=response["data"]["image_url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def food(self, ctx):
        """Send a random food images."""
        async with aiohttp.ClientSession() as session:
            async with session.get(MARTINE_API + "food") as resp:
                if resp.status == 410:
                    return await ctx.send("Failed to fetch API. Unknown error.")
                if resp.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                response = await resp.json()
            embed = discord.Embed(
                title=response["data"].get("title", "[No Title]"),
                url=response["data"]["post_url"],
                description=f"Posted by: {response['data']['author']['name']}",
            )
            embed.set_footer(
                text=f"Powered by martinebot.com API | Upvotes {response['data']['upvotes']}",
                icon_url=MARTINE_ICON,
            )
            embed.colour = await ctx.embed_color()
            embed.set_image(url=response["data"]["image_url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def neko(self, ctx):
        """Send a random neko images.

        Powered by [nekos.best.](https://nekos.best)"""
        async with aiohttp.ClientSession() as session:
            async with session.get(NEKOS_API + "nekos") as response:
                if response.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                url = await response.json()
            embed = discord.Embed(
                title="Here's an image from nekos.", colour=await ctx.embed_color()
            )
            embed.set_footer(text="From nekos.best")
            embed.set_image(url=url["url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")

    @commands.command(aliases=["city"])
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def cityview(self, ctx):
        """Send a random City images."""
        async with aiohttp.ClientSession() as session:
            async with session.get(MARTINE_API + "CityPorn") as resp:
                if resp.status == 410:
                    return await ctx.send("Failed to fetch API. Unknown error.")
                if resp.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                response = await resp.json()
            embed = discord.Embed(
                title=response["data"].get("title", "[No Title]"),
                url=response["data"]["post_url"],
                description=f"Posted by: {response['data']['author']['name']}",
            )
            embed.set_footer(
                text=f"Powered by martinebot.com API | Upvotes {response['data']['upvotes']}",
                icon_url=MARTINE_ICON,
            )
            embed.colour = await ctx.embed_color()
            embed.set_image(url=response["data"]["image_url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")

    @commands.command(aliases=["pics", "pic"])
    @commands.cooldown(1, 3, commands.BucketType.guild)
    @commands.max_concurrency(1, commands.BucketType.guild)
    @commands.bot_has_permissions(embed_links=True)
    async def picture(self, ctx):
        """Send a random images."""
        async with aiohttp.ClientSession() as session:
            async with session.get(MARTINE_API + "pics") as resp:
                if resp.status == 410:
                    return await ctx.send("Failed to fetch API. Unknown error.")
                if resp.status != 200:
                    return await ctx.send(
                        "Something went wrong while trying to contact API."
                    )
                response = await resp.json()
            embed = discord.Embed(
                title=response["data"].get("title", "[No Title]"),
                url=response["data"]["post_url"],
                description=f"Posted by: {response['data']['author']['name']}",
            )
            embed.set_footer(
                text=f"Powered by martinebot.com API | Upvotes {response['data']['upvotes']}",
                icon_url=MARTINE_ICON,
            )
            embed.colour = await ctx.embed_color()
            embed.set_image(url=response["data"]["image_url"])
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Bad reponse, please retry the command again.")
