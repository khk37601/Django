import lxml
import requests
from bs4 import BeautifulSoup

from .crawling_setting import CSetting
from ..models import PremierLeague


class CProcessing(object):
    def __init__(self):
        self.url = "https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&year=2019&tab=team"
        #self.person_url = "https://sports.news.naver.com/wfootball/record/index.nhn?category=epl&league=100&tab=player&year=2019"
        self.driver = CSetting().get_driver()

    def parsing(self, url):
        self.driver.get(url)
        html = BeautifulSoup(self.driver.page_source, "lxml")

        return html

    def insert_db(self):

        html = self.parsing(self.url)
        team_list = html.select('#wfootballTeamRecordBody>table>tbody>tr')

        for i in team_list:
            rank = i.select('.num>div.inner>strong')[0].text
            team = i.select('.name')[0].text
            winning = i.select('.selected>div.inner>span')[0].text
            record = PremierLeague(rank, team, winning)
            record.save()


if "__main__" == __name__:

    print(CProcessing().insert_db())