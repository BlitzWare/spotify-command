@client.command()
async def spotify(ctx, user: discord.Member=None):
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity, Spotify):
            await ctx.send(f"**{user} is listening to {activity.title} by {activity.artist}**")
