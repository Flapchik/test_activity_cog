from .activity_cog import ActivityCog


def setup(bot):
    bot.add_cog(ActivityCog(bot))
