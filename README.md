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

