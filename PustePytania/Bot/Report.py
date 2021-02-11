
async def echo(ctx, message: str) -> None:
    """ Print and send value """
    await ctx.send(message)
    print(message)
