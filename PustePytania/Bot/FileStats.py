from Bot import Report
import Config
import os
import requests

class FileStats:

    @staticmethod
    async def stats(ctx, ext: str) -> None:
        """ Count all stats on channel """
        authors = {}

        async for message in ctx.channel.history(limit=None):
            for att in message.attachments:
                if att.filename.split('.')[-1] in ext.split(','):
                    if message.author in authors:
                        authors[message.author] += 1
                    else:
                        authors[message.author] = 1

        message = "🔥🔥🔥"
        for author in authors.keys():
            message += f"\n{author}  -  {authors[author]}"

        message += f"\n\n files of format: {ext}"
    
        await ctx.send(message)

