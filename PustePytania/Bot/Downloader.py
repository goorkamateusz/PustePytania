from Bot import Report
import os
import requests

class Downloader:
    local_dir = "data_files/download"
    file_cnt = 0

    @staticmethod
    async def get_all_from_channel(ctx, ext: str) -> None:
        """ public """
        Downloader.file_cnt = 0
        Downloader.create_dir_if_not_exist()
        async for message in ctx.channel.history(limit=None):
            Downloader.get_from_message(message, ext)

        await Report.echo(ctx, Downloader.get_report(ext))

    @staticmethod
    def get_from_message(message, ext: str) -> None:
        """ private """
        for att in message.attachments:
            if att.filename.split('.')[-1] == ext:
                answer = requests.get(att.url)
                open(Downloader.get_file_path(att), "wb").write(answer.content)
                Downloader.inc()

    @staticmethod
    def get_file_path(att) -> str:
        """ private """
        return f"{Downloader.local_dir}/{att.filename}"

    @staticmethod
    def create_dir_if_not_exist() -> None:
        """ private """
        if not os.path.isdir(Downloader.local_dir):
            os.mkdir(Downloader.local_dir)

    @staticmethod
    def inc() -> None:
        """ private """
        Downloader.file_cnt += 1

    @staticmethod
    def get_report(ext: str) -> str:
        """ private """
        return f"Pobrano {Downloader.file_cnt} plików {ext}."
