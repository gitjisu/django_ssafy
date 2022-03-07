# How to start django project ?

:star:싸피과정 한장요약 요청=URL , 응답=Document :star:

: frame work = MTV라는 틀 안에서, 일을 한다  but  틀을 벗어날 수 없음 but 틀 안에서 효율적임

1. git init
2. touch README.md .gitignore
3. python -m venv venv
4. source venv/Scripts/activate(가상환경/독립환경 = 아무것도 깔려있지 않음)
5. pip install django==3.2.12 (pip list = 라이브러리 깔려있는거 확인 방법)
6. gitignore.io > python > django > venv > 복사 > gitignore 추가 (변경사항 6k에서 줄어듬!)
7. django-admin startproject <파일명> . (되돌리기 : rm -rf <파일명>)
   - manage.py = 집사! 프로젝트 총괄 관리
   - extra_tv(settings 있는 폴더) = master app / 앱은 아니지만 총괄 관리를 위해 존재함
8. python manage.py startapp <앱이름> 
   - settings에 앱 등록 + ','필수!
     - local file 
     - 3rd party
     - native



# django flow



<요청 (URL)이 들어오면 ->  urls.py에서 '행동'을 한다 >



1. urls.py 파일 안에 써야 할 내용 (콜백함수)

```django
form django.urls import path
from . import views

app name = '앱네임'

urlpatterns = [
	path('URL/', views.URL),
	path('URL2/', views.URL2),
]
```

2. view 함수 작성

```django
def URL(request):
	return render(request, '파일이름.html') # 무조건 return 으로 끝나야 함
def URL2(request):
	return render(request, '파일이름.html') # 첫번째 인자 request!!! 두번째 인자 파일이름!!
```

```
Q. templates 안에 따로 폴더를 왜 만들까????
A. 여러개의 templates안에 같은 이름의 html파일이 있을 때 이름이 겹치면 django가 알 수 없으니까, 라벨링 해 주는 거
```



:star: 서버한테 정보를 주는 거 = form 태그 :star:



말로만 요청 되는 거: a태그

데이터와 함께 요청 되는 거: form태그

- form action = "URL"

