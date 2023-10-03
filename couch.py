import couchdb
import asyncio
import aiofiles
from aiocsv import AsyncDictReader
import pandas as pd
import aiohttp
import logging

pd.set_option("display.max_columns", None)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(asctime)s : %(message)s",
    datefmt="%d-%m-%Y %H:%M",
    filename="couch.log",
)


class DB:
    def __init__(self, file_path, db_name, db_url):
        self.file_path = file_path
        self.db_url = db_url
        self.db_name = db_name
        self.loop = asyncio.get_event_loop()
        self.couch = couchdb.Server(db_url)

    async def read_data(self):
        try:
            if self.db_name not in self.couch:
                self.couch.create(self.db_name)
                db = self.couch[self.db_name]
                async with aiofiles.open(
                    self.file_path, mode="r", encoding="utf-8"
                ) as file:
                    async for row in AsyncDictReader(file):
                        db.save(row)
            else:
                print("Database {} already exists \n".format(self.db_name))

        except Exception as e:
            logging.error((e))

    async def get_data_info(self):
        try:
            db = self.couch[self.db_name]
            await asyncio.sleep(0.1)
            rows = db.view("_all_docs", include_docs=True)
            data = [row["doc"] for row in rows]
            df = pd.DataFrame(data)
            print("TOTAL ROWS = {}".format(df.shape[0]))
            print("COLUMNS = {}".format(list(df.columns)[2:]))
        except Exception:
            logging.error(Exception)


async def main():
    obj = DB("train.csv", "titanic", "http://admin:root@127.0.0.1:5984")
    read_data = asyncio.create_task(coro=obj.read_data())
    data_info = asyncio.create_task(coro=obj.get_data_info())
    await read_data
    await data_info


if __name__ == "__main__":
    asyncio.run(main())
