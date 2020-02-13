### Django ?

* 모델 - 뷰 - 컨트롤러 (MVC)패턴을 따르고 있으며, 파이썬으로 작성된 오픈소스 웹 프레임워크 입니다.

* 관리자 웹 인터페이스 제공.

* 객체 관계 매핑 (ORM) 
      
      SQL명령어를 대신하여 데이터베이스에 접근 하도록 해주는 인터페이스 역할.
      
 
 
###### 프레임워크 VS 라이브러리 ? 
 
  * 프레임워크 : 개발에 필요한 알고리즘, 암호화, 데이터베이스 등 기능을 구성 되있는 것을 프레임워크라고 합니다. 즉 개발에 필요한 뼈대를 제공한다     고 볼 수 있습니다. 
   
   
   * 라이브러리 : 기능에 대한 API를 모은 집합을 라이브러리라고 합니다
  
   ```
     프레임워크는 단지 미리 단들어 둔 반 제품이나, 확장해서 사용하도록 준비된  추상적인 라이브러리의 집합이 아니다.
     
     라이브러리를 사용하는 애플리케이션 코드는 애플리케이션 흐름을 직접 제어한다.
     단지 동작하는 중에 필요한 기능이 있을 때 능동적으로 라이브러리 사용.
     
     프레임워크는 반대로 애플리케이션 코드가 프레임워크에 의해 사용된다.
     프레임워크에는 제어의 역전 개념이 있어야한다.
     애플리케이션 코드는 프레임워크가 짜놓은 틀에서 수동적으로 동작해야 한다.
     
     -토비 스프링-
   ```
   
    * 제어의 역전이란? 제어의 역전 프레임워크에 제어의 권한을 넘겨주는 것을 말합니다.
   
   
#### MVC패턴

Model - view - controller 패턴 Model은 데이터, View는 사용자 인터페이스, Controller는 데이터 처리. 

각 부분을 나눠서 한 요소가 다른 요소에 영향을 주지 않도록 하는 방법입니다.

각 개발자가 각자 분야에만 집중해서 개발의 효율성을 증대 시키는 패턴입니다.

Djnago도 역시 MVC 패턴을 그대로 이용하고 있습니다. 단지 용어만 다르게 ```MTV(Model- Template - controller )```를 사용합니다. 

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/Django_API.PNG)
```
클라이언트의 request가 오면 url을 분석하여 뷰에 처리합니다.
뷰에 데이터베이스 처리가 필요한 경우 모델을 통해서 처리하고 결과를 반환하여 템플릿과 함께 html파일 생성 후 뷰에서 생성된 html파일을 클라이언트에게 전송하는 방식입니다.
````

#### ORM기법

Model은 데이터에 대한 정의를 담고 있는 장고 클래스입니다. 

ORM은 Oject-Relational Mapping의 약자로 객체와 관계형데이터베이스를 연결하여 SQL문 없이 데이터베이스에 접근이 가능하게 하며 데이터베이스 엔진의 종속성에 자유로워져 질 수 있습니다.

```
* 테이블의 모든 데이터 가져오기
>> 모델이름.objects.all() <select * from 테이블이름> 

* 하나의 Row만 가져오기
>> 모델이름.objects.get(id=khk37601') <id가 khk37601인 row하나만 가져온다.>
 
* 특정조건에 맞는 Row들을 가져오기 
 >> 모델이름.objects.filter(id='khk37601') <id가 khk37601인 모든 row를 가져온다. select * from 테이블 where id='khk37601'>
 
 >>   queryset = 모델이름.objects.all()
      queryset = queryset.filter(조건필드1=조건값1, 조건필드2=조건값2)    
      queryset = queryset.filter(조건필드3=조건값3)

 
* 특정 조건을 제외한 나머지 Row 가져오기
 >> 모델이름.objects().exclude(id ='khk37601') <seelct * from 테이블 where id <> 'khk37601'>  

* 데이터의 Row갯수를 세기
>> 모델이름.objects.count() <select count(*) from 테이블이름>

* 중복된값 하나로만 표시하기
>> 모델이름.objects.distinct('id') <id 필드에 중복되는 경우 한번만 표시>

* 데이터 중 처음에 있는 Row만 가져오기.
>> 모델이름.objects.order_by('id').frist()
>> 모델이름.objects.order_by('id').last()

* 데이터 정렬
>> 모델이름.objects.order_by('id') <오름차순 정렬>
>> 모델이름.objects.order_by('-id') <내림차순 정렬>
 
 
* 데이터 업데이트

>>  name = 모델이름.objects.get(id='khk37601')
    name.id = 'KIM'
    name.save()

* 데이터 삭제
>>  name = 모델이름.objects.get(id='khk37601')
    name.delete()

* or 조건
>> from django.db.models import Q

 >> 모델이름.objects.all().filter(Q(조건필드1=조건값1) | Q(조건필드2=조건값2)) # or 조건 
 >> 모델이름.objects.all().filter(Q(조건필드1=조건값1) & Q(조건필드2=조건값2)) # and 조건

```

#### Django 설치
* os는 Window 기준입니다.
```
>> mkdir Django_project # 디렉토리 생성

>> cd Django_project # 디렉토리 이동

>> python -m venv myvenv 

>> python -m pip install --upgarde pip # pip 업데이트

>> pip install django = 버전 # Django 설치
```

#### Django Rest FrameWork
```
Django와 DRF (Django Rest Framework)는 사용되는 방식이 다릅니다. 
웹 응용 프로그램을 만들려면 django가 도움이되며 API 만 만들려면 DRF가 유용 할 수 있습니다.
예, django에서도 API 종류의 구조를 만들 수 있지만 DRF는 serializer, 필터링 및 OAuth 지원 또는 Markdown, PyYAML, Markdown, YAML, XML 컨텐츠유형 지원 등을 쉽게 사용할 수 있도록 더 많은 기능을 제공합니다. 
따라서 기본적으로 API를 만들려면 DRF를 사용해야한다고 말할 수 있습니다. 웹 애플리케이션을 만들어야한다면 장고를 사용해야합니다.

```
제가 생각하기에는 재사용성을 높이기 위해서 사용하는거 같습니다.

우선  Django Rest FrameWork를 다뤄보기 전에 Restful에 대해서 알아 볼려고 합니다.

###### ```Restful```란?

자원을 이름으로 구분하여 자원의 정보를 주고받는 모든 행위를 의미합니다.

즉, HTTP url를 이용해서 자원을 명시하고 HTTP Method를 통해서 자원에 대한 CURD 작업을 수행합니다.

클라이언트와 서버 사이의 통신 방식중 하나로 HTTP 프로토콜을사용하여 웹의 장점을 최대한 이용가능 합니다.

(데이터는 XML,JSON으로 주고 받습니다.)

* 생성 : Post -> 데이터를 body에 포함시켜 서버에 요청하는 방법으로 길이의 제한이 없으며, 데이터를 윽닉가능합니다.
* 조회 : Get  -> url에 데이터를 첨부하여 서버에 요청하는 방법으로 길이의 제한이 있습니다.
* 수정 : Put 
* 삭제 : Delete 
* 정보조회 : Head 

###### ```Rest API```란?

Rest기반으로 서비스 API를 구현한 것입니다. 

* Rest 기반으로 시스템을 분산하여 확정성과 재사용성을 높일 수 있습니다.

-Rest API 디자인 규칙 -책 참고.


##### djangorestfamework 설치.

```
>> pip install djangorestfamework #설치
```

* django에 reest_frame 추가.

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/resframwork_setting%EC%84%A4%EC%A0%95.PNG)


* MariaDB 연결

```
>> pip install mysqlclient
 
=== 오류생기는 경우 ===

https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient 에서 본인의 파이썬 버전에 맞는 whl 파일을 다운로드 받습니다.

pip insatll 파일위치\~.whl

```
* Django는 기본적으로 sqllite3를 제공하기 때문에 아래와 같이 변경해야 합니다. 

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/mariaDB%EC%97%B0%EA%B2%B0.PNG)



* Serializers 생성.
데이터를 Json으로 변환 하여 통신하게 해주는 역할을 합니다.

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/restfamework_%EB%AA%A8%EB%8D%B8.PNG)


* urls 매핑
urls.py rest_framework에 router를 이용하여 등록.

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/restfamework_urls.PNG)

* 어플리케이션 실행.
```
>> python manage.py runserver
```
![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/restframewotk%EB%82%B4%EC%9A%A9%EC%B6%94%EA%B0%80PNG.PNG)

```
>> pip install requests

data = (request.get('localhiost/premier2')).json() 
하여서 Server와 클라이언트의 데이터를 통신 할 수 있게 됩니다.
```
프론트와 백엔드를 나눠서 개발이 가능해집니다.

<img src="https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/restframework_%EC%95%84%ED%82%A4%ED%85%8D%ED%8A%B8.PNG" width="60%">

--------------------------------------------------------------------------------------------------------------------------

#### 검색화면.
<img src="https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/Django_project_%EB%A9%94%EC%9D%B8.PNG" width="50%">

#### 검색된 리그 순위정보와 선수정보.
<img src="https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC.PNG" width="50%">

#### 회원가입.
<img src="https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.PNG" width="40%" >


===== 프론트와 백엔드을 분리하여 개발 진행.. 하지만 Setting문제 생겨 해결 하고 있습니다. ======


2020.02.11 현재 오류
#### 원인이 뭔지 모르겠습니다.
![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/Restframework%20%EC%98%A4%EB%A5%98%20%EB%B0%9C%EC%83%9D.PNG)

##### 문제 해결 하였습니다. ^^

무슨 문제인지 파악이 필요해서 원본 UpdateAPIView의 원본 소스를 봤습니다.

```
def update(self, request, *args, **kwargs):
     # kwargs가 삭제할 번호를 가지고 있는 매개변수 입니다.
     partial = kwargs.pop('partial', False)
     # 해당 정보를 가져 DB에서 가져옵니다.
     instance = self.get_object()
     # 가져오는 값을 직렬화 합니다.
     serializer = self.get_serializer(instance, data=request.data, partial=partial)
     serializer.is_valid(raise_exception=True)
     # 값을 업데이트 합니다.
     self.perform_update(serializer)
```
기존에 구현된 메소드를 쓰면 get_object()에서 아무 값도 못가져오게 되는 문제 가 발생 했던 것 입니다.
계속해서 이부분에서 에러가 발생하여 아래 처럼 코드를 수정하여서 오류를 수정 하였습니다.

```
class PremierLeague_update(UpdateAPIView):


    queryset = PremierLeague.objects.all()
    serializer_class = Serial_Premierleague

    def get_object(self, pk):
        try:
            return PremierLeague.objects.get(rank=pk)
        except:
            raise Http404


    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        ** instance = self.get_object(kwargs['rank'])** # get_object에 key값을 넣어서 어떤거 값을 가져올지 알려줍니다.
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

```

##### 파이어베이스

파이어베이스는 웹, 모바일 등의 개발에 필요한 ```Baas(Backend as a Service)```를 제공해주는 서비스입니다.

실시간 데이터베이스, 인증, 클라우드 저장소, 호스팅, 성능 모니터링 등 많인 서비스를 제공해 줍니다.

여기서 저는 인증 서비스를 이용해 로그인 처리를 해볼려고 합니다.

인증 서비스는  이메일/비밀번호, 타사 제공업체(Facebook 등), 기존 계정 시스템 직접 사용 등의 다양한 인증 방법을 제공하는 서비스 입니다. 


pyrebase 설치

```
>> pip install pyrebase 

# 이렇게 설치하면 setup.py 에서 UnicodeDecodeError 'cp949' codec can't decode 오류가 발생 하게 됩니다.

```
##### 왜 이러한 에러가 발생하는 것일 까요?

이 문제를 발생시킨 setup.py을 들려다 보겠습니다.

* setup.py
```
# 여기서 오류가 발생하는 지점입니다.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jws",
    version = "0.1.3",
    author = "Brian J Brennan",
    author_email = "brianloveswords@gmail.com",
    description = ("JSON Web Signatures implementation in Python"),
    license = "MIT",
    keywords = "jws json web security signing",
    url = "http://github.com/brianloveswords/python-jws",
    packages=['jws'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    test_suite = 'nose.collector',
)
```
UnicodeDecodeError 'cp949' codec can't decode 오류는
Setup.py에서 read 함수에서 open 한 파일은 cp949로 인코딩 할 수 없는 내용이 존재하기 때문에 문제가 발생하게 되는 것입니다.

오류를 해결하기 위해서는 open 함수에 인코딩을 ``utf-8```로 하겠다고 명시적으로 알려주면 오류는 간단하게 해결이 됩니다.

```
 >> return open(os.path.join(os.path.dirname(__file__), fname)).read() #이전
 >>  return open(os.path.join(os.path.dirname(__file__), fname), encoding="UTF-8").read() # 수정.
                  
```

###### pyrebase 설치.
```
>> pip  download jws

# jws.tar.gz 파일 생성 -> jws.tar.gz 압축을 풀고 setup.py파일을 위에 내용처럼 수정 합니다.

>> pip install pyrebase # 설치 성공 

* 참고로 pyrebase는 파이어베이스를 쉽게 사용하기 위해서 만든 소스로 오픈소스 파이썬으로 구성되어 있습니다.
(https://github.com/thisbejim/Pyrebase 소스를 분석하고 싶은 분들은 참고하세요.)

```

그러면 파이어베이스를 사용해보겠습니다.
저는 firabse_setting.py에  파이에베이스를 설정코드를 작성해봤습니다.
![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/%ED%8C%8C%EC%9D%B4%EC%96%B4%EB%B2%A0%EC%9D%B4%EC%8A%A4%20%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC.PNG)

```
# firebase_setting.py

import pyrebase

class FirebaseSetting():

    def __int__(self):
        pass

    def get_firbase_auth(self):
        config = {
                  "본인 설정내용 입력."
        }
        
        firbase = pyrebase.initialize_app(config)
        f_auth = firbase.auth()
        # 데이터 베이스 생성.
        database = firbase.database()

        return f_auth

# viwe.py
      
 try:
         # 
        f_auth = FirebaseSetting().get_firbase_auth()
        
        # 로그인 확인.
        user = f_auth.sign_in_with_email_and_password(email, pwd)
 except Exception as e:
        print(e)
       return render(request, 'front_html/login.html', {'message': message})
 else:
      # 정상적인 로그인이 이루어지면 해당 아이디에 토큰이 발행이 됩니다. 
      # 토큰 저장.
      session_id = user['idToken']
      # 그 토큰 값을 Django session에 저장 시킵니다.
      # 세션저장.
       request.session['uid'] = str(session_id)
       request.session['email'] = email

       return render(request, 'front_html/premier_index.html')


# 위에 같은 간단한 코드로 파이어베이스 인증 서비스를 이용할 수 있게 됩니다.

# 이메일 로그인방법 허용 방법.

      Authentication >> 로그인 방법 >> 이메일/비밀번호 >> 사용설정


# 파이어베이스 설정값 찾는방법.

      설정(톱니바퀴) >> 프로젝트 설정 -> 하단 -> 내앱 >> Firebase SDK snippet 

```

~~개인적인 생각으로 규모가 작은 스타트업이나 소기업에 부담없이 사용하기 좋은 서비스 인거같습니다.






