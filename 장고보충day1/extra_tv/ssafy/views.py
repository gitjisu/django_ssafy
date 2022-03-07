from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'ssafy/ping.html')

# 사용자 제출 데이터를 받을 곳
def pong(request):
    #x # NameError: name 'x' is not defined
    context = {
        'heading' : request.GET['heading'],
        'bg_color' : request.GET['bg-color'],
        'text_color' : request.GET['text-color']
    }
    return render(request, 'ssafy/pong.html', context)