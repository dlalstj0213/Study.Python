import base64
from typing import List
from github import Github
from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class GitRepository:
    name: str
    url: str
    description: str
    language: str
    forks: str
    stars: str
    created_at: date
    pushed_at: date
    last_days: str


def date_convert_to_string(dt):
    days_hms = str(dt)
    list_dhms = days_hms.split(", ")
    days = ""
    if len(list_dhms) == 2:
        days = list_dhms[0]

    hhmmss = list_dhms[-1]
    if(len(hhmmss) == 7):
        hhmmss = '0' + hhmmss

    list_hms = hhmmss.split(":")
    cvt_hms = str(int(list_hms[0]))+"시" + \
        str(int(list_hms[1]))+"분" + \
        str(int(list_hms[2][0:list_hms[2].index(".")]))+"초"
    day_hour_min_sec = days.replace(
        " days", "일 ").replace(" day", "일 ") + cvt_hms
    return f"{day_hour_min_sec}전"


class GitService:
    def __init__(self, username, token=None):
        if token is not None:
            self.user = Github(token).get_user(username)
        else:
            self.user = Github().get_user(username)

    def find_all_repo(self) -> List:
        time_now = datetime.now()
        repo_list = []
        for repo in self.user.get_repos():
            repo_list.append(GitRepository(
                repo.name,
                repo.html_url,
                repo.description,
                repo.language,
                repo.forks,
                repo.stargazers_count,
                repo.created_at,
                repo.pushed_at,
                date_convert_to_string(time_now - repo.pushed_at)
            ))
        return repo_list


if __name__ == "__main__":
    mygit = GitService("dlalstj0213")
    result = mygit.find_all_repo()

    result
    for t in result:
        print(t["push_date_state"])
