from django.shortcuts import render,redirect
from students.models import Students

# 학생정보리스트
def slist(request):
    qs = Students.objects.all()
    context = {'list':qs}
    return render(request,'slist.html',context)


# 학생성적 입력페이지,저장
def swrite(request):
    if request.method == 'GET':    
        return render(request,'swrite.html')
    elif request.method == 'POST':
        name = request.POST.get('name') # 데이터가 없어도 에러가 나지 않음
        major = request.POST.get('major')    # 데이터가 없을때 에러
        age = request.POST.get('age')    # 데이터가 없을때 에러
        grade = request.POST.get('grade')    # 데이터가 없을때 에러
        gender = request.POST.get('gender')    # 데이터가 없을때 에러
        # 1. save()
        qs = Students(name=name,major=major,age=age,grade=grade,gender=gender)
        qs.save()
        # 2. create()
        # Students.objects.create(name=name,major=major,age=age,grade=grade,gender=gender)
        print(f'확인 : {name},{major},{age},{grade},{gender}')

        return redirect('/students/slist')
