from django.shortcuts import render,redirect
from stuscore.models import Student

def score_write(request):
    if request.method == 'GET':  
        print("페이지가 로딩되었습니다.")
        return render(request,'score_write.html')
    elif request.method == 'POST':
        print("POST 페이지가 로딩")
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        # qs = Stu(name='홍길동,major='국문학과',grade=1,age=20,gender='남자')
        qs = Student(name=name,major=major,grade=grade,age=age,gender=gender)
        qs.save()

        print(name,major,grade,age,gender)
        return redirect('/')