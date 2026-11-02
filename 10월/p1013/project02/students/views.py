from django.shortcuts import render,redirect
from students.models import Students

# 학생정보상세보기 - 1개
def sview(request,no):
    qs = Students.objects.get(no=no)
    context = {'stu':qs}
    return render(redirect, 'sview.html',context)

# 학생정보리스트 - 여러개
def slist(request):
    # 딕셔너리 형태로 데이터를 전달함.
    qs = Students.objects.all().order_by('-no') # 전체가져오기, 정렬(-역순정렬)
    # qs = Students.objects.get(name='홍길동') # 1개 가져오기
    # __contains:포함, __endswith
    # qs = Students.objects.filter(name__contains='s') # s가 포함되어 있는 학생
    # qs = Students.objects.filter(name__endswith='s') # s가 포함되어 있는 학생
    # gt,gte,lt,lte
    # qs = Students.objects.filter(grade__gt=3) # 3학년이상

    context = {'list':qs}
    return render(request, 'slist.html',context)

# 학생정보입력페이지
def swrite(request):
    if request.method == 'GET':
        return render(request, 'swrite.html')
    elif request.method == 'POST': #1. form값전달
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')  # checkbox 값이 여러개
        # save저장
        Students(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby).save()
        # create저장
        # Students.objects.create(name=name,major=major,grade=grade,age=age,\
        #                         gender=gender,hobby=hobby)
        print(name,major,grade,age,gender,hobby)
        return redirect('/')
