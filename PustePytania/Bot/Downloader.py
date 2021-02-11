from Bot import Report
import Config
import os
import requests

class Downloader:
    __local_dir = Config.DOWNLOAD_DIR
    __file_cnt = 0

    @staticmethod
    async def get_all_from_channel(ctx, ext: str) -> None:
        """ Downloand all files from channel """
        Downloader.__file_cnt = 0
        Downloader.create_dir_if_not_exist()
        async for message in ctx.channel.history(limit=None):
            Downloader.__get_from_message(message, ext)

        await Report.echo(ctx, Downloader.__get_report(ext))

    @staticmethod
    def __get_from_message(message, ext: str) -> None:
        for att in message.attachments:
            if att.filename.split('.')[-1] == ext:
                answer = requests.get(att.url)
                open(Downloader.__get_file_path(att), "wb").write(answer.content)
                Downloader.__inc()

    @staticmethod
    def __get_file_path(att) -> str:
        return f"{Downloader.__local_dir}/{att.filename}"

    @staticmethod
    def create_dir_if_not_exist() -> None:
        if not os.path.isdir(Downloader.__local_dir):
            os.mkdir(Downloader.__local_dir)

    @staticmethod
    def __inc() -> None:
        Downloader.__file_cnt += 1

    @staticmethod
    def __get_report(ext: str) -> str:
        return f"Pobrano {Downloader.__file_cnt} plików {ext}."
