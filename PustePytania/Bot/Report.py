
async def echo(ctx, message: str) -> None:
    """ Print and send message with text message """
    await ctx.send(message)
    print(message)
