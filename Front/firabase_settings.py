import pyrebase


class FirebaseSetting():

    def __int__(self):
        pass

    def get_firbase_auth(self):
        config = {
           "본인 파이어베이스 데이터 입력."
        }

        firbase = pyrebase.initialize_app(config)
        f_auth = firbase.auth()
        # 데이터 베이스 생성.
        database = firbase.database()

        return f_auth
