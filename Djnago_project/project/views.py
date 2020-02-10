from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from .processing_model.process import Processing
from apscheduler.schedulers.blocking import BlockingScheduler
from .models import PremierLeague2
from itertools import chain
import pyrebase
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import auth
import requests
import json
from rest_framework import viewsets
from  .templates.project_py.serializers import Premierleague_2
from .models import PremierLeague2

# 추가
#myvenv\Scripts\activate
from django.views import View


config = {

          "본인의 파이어베이스 내용추가."
        }

firbase = pyrebase.initialize_app(config)
f_auth = firbase.auth()
# 데이터 베이스 생성.
database = firbase.database()


def sign(request):
    return render(request, "project/sign.html")


def signup(request):
    return render(request, "project/signup.html")


def join(request):
    return render(request, 'project/join.html')


# 이메일 아이디 분리.
def email_id(email):
    return email[:email.index('@')]


def random_number():

    import random

    rstr = "0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"
    rstr_len = len(rstr) - 1
    result = ""
    for i in range(5):
        result += rstr[random.randint(0, rstr_len)]
    return result


# 이메일 발송.
def check_email(request):

    email = request.GET['email']
    check_number = random_number()
    context = {"check_number": check_number}
    message = EmailMessage("인증을 위한 이메일", check_number, to=[email])
    message.send()

    return HttpResponse(json.dumps(context), content_type= "application/json")


# 로그아웃.
def logout(request):
        auth.logout(request)
        return render(request, 'project/sign.html')


# 로그인 처리.
def post_sign(request):
        if request.method == "POST":
            email = request.POST.get('email')
            pwd = request.POST.get('pwd')

            try:
                # 확인
                user = f_auth.sign_in_with_email_and_password(email, pwd)
            except:
                message = "다시 입력해주세요."
                return render(request, "project/sign.html", {"message": message})

            # 토큰 저장.
            session_id = user['idToken']
            # 세션저장.
            request.session['uid'] = str(session_id)
            email = email_id(email)
            request.session['name'] = email

            return render(request, "project/main-first.html")


# 회원가입 처리.
def post_signup(request):

        if request.method == "POST":
            email = request.POST.get('email')
            pwd = request.POST.get('pwd')
            name = request.POST.get('name')

            try:
                user = f_auth.create_user_with_email_and_password(email, pwd)

                uid = user['localId']
                data = {"email": email, "name": name, "status": "1"}
                # 계층 새성.
                database.child('users').chlid(uid).child("details").set(data)

            except requests.exceptions.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']

            return render(request, 'project/sign.html')


def main(request):

    if request.method == "POST":
            if request.POST['user_date'].strip():
                word = request.POST['user_date']
                try:
                    rank, team, scor, reson = Processing().start(word)
                    person_list, score_list = Processing().person_rank(word)

                    # 리스트 한겹 없애기
                    score_list = list(chain(*score_list))

                    person_rank = score_list[0]
                    person_name = score_list[1]
                    person_score = score_list[2]
                    person_asset = score_list[3]
                    person_at_point = score_list[4]
                    person_try_shot = score_list[5]
                    person_correct_shot = score_list[6]

                    if team == reson:
                        reson = ""
                except:
                        return render(request, 'project/main-first.html', {'message': "다시 입력하세요"})

                return render(request, 'project/main-first.html',
                              {'rank': rank,
                                                                'team': team,
                                                                'scor': scor,
                                                                'reson': reson,
                                                                'person_rank': person_rank,
                                                                'person_name': person_name,
                                                                'person_asset': person_asset,
                                                                'person_at_point': person_at_point,
                                                                'person_correct_shot': person_correct_shot,
                                                                'person_try_shot': person_try_shot,
                                                                'person_score': person_score,
                                                                'score': score_list,
                                                                'range': range(5)}
                              )
            else:
                return render(request, 'project/main-first.html')
    else:
        return render(request, 'project/main-first.html')


scheduler = BlockingScheduler()
#hours=3
scheduler.add_job(Processing().insert_db, 'interval', seconds =10 , id="start_sc")


def start_scheduler(request):
        try:
            scheduler.start()
        except:
            pass

        return redirect('/')


def shutdown(request):
        #scheduler.remove_job('start_sc')
        try:
            scheduler.pause_job('start_sc')
        except:
            pass
        return redirect('/')


def email_duplicate_check(request):

        email = request.GET['email']
        check = Processing().email_duplicate_check(email)
        context = {'check' : check}

        return HttpResponse(json.dumps(context), content_type= "application/json")

class RestAPI(viewsets.ModelViewSet):
    queryset = PremierLeague2.objects.all()
    serializer_class = Premierleague_2

