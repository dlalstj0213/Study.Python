from main import main
from os import times
from typing import List
from urllib.request import urlopen
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
import json
from datetime import datetime
import time
import asyncio


@dataclass
class HttpClient:
    async def request_html(self, url) -> BeautifulSoup:
        response = await loop.run_in_executor(None, requests.get, url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            return soup
        else:
            print(response.status_code)
            return None


@dataclass
class KakaoJob:
    title: str
    url_link: str
    tags: str
    recruitment_period: str
    work_palce: str
    company: str
    emp_type: str


@dataclass
class KakaoCrawler:
    base_url: str = field(default="https://careers.kakao.com")
    target_url: str = field(default="/jobs?page=")
    http: HttpClient = field(default_factory=HttpClient)

    async def find_total_page(self) -> int:
        url = self.base_url + self.target_url + "1"
        soup = await self.http.request_html(url)
        page_query = soup.select_one(".change_page.btn_lst")["href"]
        page = page_query[(page_query.index("=")+1):]
        return int(page)

    async def find_recruitment_by_page(self, page: str) -> List[KakaoJob]:
        url = self.base_url + self.target_url
        futures = [asyncio.ensure_future(
            self.http.request_html(f"{url}{1}")) for p in range(1, 21)]
        # futures = [asyncio.ensure_future(
        #     self.http.request_html(f"{url}{p}")) for p in range(1, page+1)]
        soups = await asyncio.gather(*futures)
        if len(soups) == 0:
            return None
        item_list = []
        for soup in soups:
            ul = soup.select('ul.list_jobs > li')
            for li in ul:
                item = KakaoJob(
                    li.select_one("h4").get_text(),
                    self.base_url + li.select_one(".link_jobs")['href'],
                    [a.get_text().strip()
                        for a in li.select(".list_tag > a")],
                    li.select(".list_info > dd")[0].get_text(),
                    li.select(".list_info > dd")[1].get_text(),
                    li.select(".item_subinfo > dd")[0].get_text(),
                    li.select(".item_subinfo > dd")[1].get_text()
                )
                # item_list.append(item)
                item_list.append(item.__dict__)
        return item_list


@dataclass
class FileService:
    base_json_dir: str = field(init=False, default="./json")
    base_logs_dir: str = field(init=False, default="./logs")

    def write_logs_in_json(self, file_name, source: list, text_log: str = None):
        file_json_path = self.base_json_dir + "/" + file_name + ".json"
        file_log_path = self.base_logs_dir + "/" + file_name + ".log"
        with open(file_json_path, "w") as out_file:
            json.dump(source, out_file, indent=2, ensure_ascii=False)

        if text_log is not None and len(text_log.strip()) != 0:
            with open(file_log_path, "a") as out_file:
                out_file.write(text_log + f" | 크롤링 결과 위치: .{file_json_path}")
                out_file.write("\n")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    kakao = KakaoCrawler()
    future_total_page = asyncio.ensure_future(kakao.find_total_page())
    loop.run_until_complete(future_total_page)
    total_page = future_total_page.result()

    future_find_recruitment = asyncio.ensure_future(
        kakao.find_recruitment_by_page(total_page))
    start = time.time()
    loop.run_until_complete(future_find_recruitment)
    end = time.time()
    time_took = end - start

    now = str(datetime.now())
    data = {'timestamp': now}
    data['recruitment'] = []
    data['recruitment'].extend(future_find_recruitment.result())

    f = FileService()
    text_log = f"{now} :: test_main >>> 크롤링 걸린시간: {end - start} | 크롤링 갯수: {len(data['recruitment'])}"
    f.write_logs_in_json("sample", data, text_log)

    main()

###############################################
