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
pip install djangorestfamework #설치
```

* django에 reest_frame 추가.

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/resframwork_setting%EC%84%A4%EC%A0%95.PNG)


* MariaDB 연결

```
pip install mysqlclient
 
=== 오류생기는 경우 ===

https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient 에서 본인의 파이썬 버전에 맞는 whl 파일을 다운로드 받습니다.

pip insatll 파일위치\~.whl

```
* Django는 기본적으로 sqllite3를 제공하기 때문에 아래와 같이 변경해야 합니다. 

![](https://github.com/khk37601/Django/blob/master/Django_%EC%9D%B4%EB%AF%B8%EC%A7%80/mariaDB%EC%97%B0%EA%B2%B0.PNG)





