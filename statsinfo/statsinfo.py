# statistics logics are from R.danny.
import datetime

import discord
import pkg_resources
from redbot.core import commands
from redbot.core.utils.chat_formatting import box, humanize_number


class StatsInfo(commands.Cog):
    """Shows some stats for [botname]."""

    __author__ = "MAX"
    __version__ = "2.6.0"

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthor: {self.__author__}\nCog Version: {self.__version__}"

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def statsinfo(self, ctx):
        """Statistics for [botname]."""
        total_members = 0
        total_unique = len(self.bot.users)
        text = 0
        voice = 0
        stage_channels = 0
        category_channel = 0
        store_channel = 0
        guilds = 0
        for guild in self.bot.guilds:
            guilds += 1
            total_members += guild.member_count
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    text += 1
                elif isinstance(channel, discord.VoiceChannel):
                    voice += 1
                elif isinstance(channel, discord.StageChannel):
                    stage_channels += 1
                elif isinstance(channel, discord.CategoryChannel):
                    category_channel += 1
                elif isinstance(channel, discord.StoreChannel):
                    store_channel += 1

        shards = humanize_number(self.bot.shard_count)
        version = pkg_resources.get_distribution("discord.py").version
        servers = str(len(self.bot.guilds))
        users = str(len(self.bot.users))
        emb = discord.Embed(
            title=f"botstats for {self.bot.user.name}:", color=await ctx.embed_color()
        )
        emb.add_field(
            name="Shards:",
            value=box(
                f"{shards} shards",
                "css",
            ),
            inline=False,
        )
        emb.add_field(
            name="Users:",
            value=box(
                f"{servers} Servers\n{total_members} Total Users\n{total_unique} Unique Users",
                "css",
            ),
        )
        emb.add_field(
            name="Channels:",
            value=box(
                f"{text} Text Channels\n{voice} Voice Channels\n{stage_channels} Stage Channels",
                "css",
            ),
        )
        emb.add_field(
            name="\N{ZERO WIDTH SPACE}", value="\N{ZERO WIDTH SPACE}", inline=False
        )
        emb.add_field(
            name="Total channels:",
            value=box(
                f"{text + voice + stage_channels} Total Channels\n{category_channel} Total Categories\n{store_channel} Total Store Channels",
                "css",
            ),
        )

        emb.set_footer(text=f"Discord.py v{version}")
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)
