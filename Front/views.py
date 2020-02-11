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


class Search(View):
    def post(self, request):
        pass

    def get(self, request):
        __url = 'http://127.0.0.1:8000/premier-league-list/{}/'.format(request.GET.get('user_date'))
        data = (requests.get(__url)).json()

        return render(request, 'front_html/premier_index.html',{'detail_team': data})


class PostLogin(View):

    def post(self, request):

        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        message = "빈칸을 입력하지 마세요."

        # 빈칸 체크.
        if (email is None or pwd is None) or email == "" or pwd == "":
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

    def get(self, request):
        return render(request, 'front_html/login.html')


# 로그아웃.
def logout(request):
    response = render(request, 'front_html/login.html')
    auth.logout(request)
    response.delete_cookie('email')
    response.delete_cookie('pwd')

    return HttpResponseRedirect(reverse('login'))


