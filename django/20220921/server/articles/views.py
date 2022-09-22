from django.shortcuts import render
import random

# Create your views here.
def index(request):
    names = ['주세환', '오진수', '임수경', '조병진', '차화영', '최근영', '김선교']
    name = random.choice(names)
    context = {
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
    return render(request, 'index.html', context)
    # render(인자, 이동할페이지, context)

def welcome(request, name):
    # 사람들이 /welcome/이름 을 쓰면, 환영 인사와 이름을 보여줌.
    # print를 하면 서버에 출력됨. web X
    
    context = {
        'name': name,
        'img': 'https://cdn.crowdpic.net/detail-thumb/thumb_d_063DE2526E75F644AA2AE4BD774FE330.jpg',
    }
    return render(request, 'welcome.html', context)