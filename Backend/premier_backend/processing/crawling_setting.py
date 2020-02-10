from selenium import webdriver


class CSetting(object):
    def __init__(self):
        self.__options = webdriver.ChromeOptions()
        self.__options.add_argument('headless')
        self.__options.add_argument('window-size=1920x1080')
        self.__options.add_argument('--disable-gpu')
        self.__options.add_argument("lang=ko_KR")  # 한국어!
        self.__options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/"
                                    "537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        # dirver가 없는 경우.
        try:
            self.__driver = webdriver.Chrome('C:/Users/khk37/OneDrive/Documents/chromedriver',
                                             chrome_options= self.__options)
        except:
            print("드라이브를 설치하거나 경로를 다시 설정 해주세요")
            # self.check_chrome_version()

    def get_driver(self):
        return self.__driver

    def __str__(self):
        return self.__driver