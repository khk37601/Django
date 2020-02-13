from django.shortcuts import render, Http404
from django.views.generic import View
import requests
from django.contrib import auth
from .firabse.firabase_setting.firabase_settings import FirebaseSetting
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
   return render(request, 'front_html/premier_index.html')


def validation(*args, func="None"):

    length = len(args)

    if args is None:
        return True

    if length == 1:
        if args[0] is None or not args[0]:
            return True

    elif length == 2:
        if (args[0] is None or not args[0] ) or (args[1] is None or not args[1]):
                return True
    elif length == 3:
        if (args[0] is None or not args[0]) or (args[1] is None or not args[1]) or(args[2] is None or not args[2]):
                return True


class Search(View):
    def post(self, request):
        pass

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        word = request.GET.get('user_date')

        # if word is None or word == "":
        if validation(word):
            return render(request, 'front_html/premier_index.html', {'message': "공백은 노노"})

        try:
            __url = 'http://127.0.0.1:8000/premier-league-list/{}/'.format(request.GET.get('user_date'))
            data = (requests.get(__url)).json()
        except:
            return render(request, 'front_html/premier_index.html',{'message': "이상한 특수기호 노노"})

        return render(request, 'front_html/premier_index.html', {'detail_team': data})

    # noinspection PyMethodMayBeStatic
    def total_list(request):

        __url = 'http://127.0.0.1:8000'
        data = (requests.get(__url)).json()
        return render(request, 'front_html/premier_index.html', {'total_list': data})


class AdminPage(View):

    # noinspection PyMethodMayBeStatic
    def get(self, request):

            team_name = request.GET.get('user_date')
            rank = request.GET.get('user_rank')
            winning = request.GET.get('user_winning')

            if validation(team_name, rank, winning):
                return render(request, 'front_html/insert-page.html', {'message': "공백은 노노"})

            else:
                data = {
                    'rank' : rank,
                    'team_name' : team_name,
                    'winning' :  winning
                }
                try:
                    requests.post('http://127.0.0.1:8000/premier-league-list/', data)
                    return render(request,'front_html/insert-page.html', {'data': data})

                except:
                    return

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        return render(request, 'front_html/insert-page.html')

class PostLogin(View):

    # 로그인 처리.
    # noinspection PyMethodMayBeStatic
    def post(self, request):

        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        message = "빈칸을 입력하지 마세요."

        # 빈칸 체크.
        # if (email is None or pwd is None) or email == "" or pwd == "":
        if validation(email, pwd):
            return render(request, 'front_html/login.html', {'message': message})

        try:
            f_auth = FirebaseSetting().get_firbase_auth()
            user = f_auth.sign_in_with_email_and_password(email, pwd)
        except Exception as e:
            print(e)
            return render(request, 'front_html/login.html', {'message': message})

        else:

            # 토큰 저장.
            session_id = user['idToken']
            # 세션저장.
            request.session['uid'] = str(session_id)
            request.session['email'] = email

            return render(request, 'front_html/premier_index.html')

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return render(request, 'front_html/login.html')

    # 로그아웃 처리.
    # noinspection PyMethodMayBeStatic
    def logout(self, request):
        response = render(request, 'front_html/login.html')
        auth.logout(request)
        response.delete_cookie('email')
        response.delete_cookie('pwd')

        return HttpResponseRedirect(reverse('login'))
