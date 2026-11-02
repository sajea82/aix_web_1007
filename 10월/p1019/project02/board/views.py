from django.shortcuts import render,redirect
from django.db.models import F,Q
from board.models import Board


# 게시글 삭제
def bdelete(request):
    return render(request,'bwrite.html')

# 게시글 수정
def bupdate(request):
    return render(request,'bupdate.html')

# 게시글 리스트
def blist(request):
    return render(request,'blist.html')

# 게시글 등록
def bwrite(request):
    if request.method == 'GET':
        return render(request,'bwrite.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        id = request.POST.get('id')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        print(f'데이터확인 : {btitle},{id},{bcontent},{bfile}')
        qs = Board.objects.create(btitle=btitle,id=id,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()

        context = {'temp':1}
        return render(request,'bwrite.html',context)

# 게시글 상세보기
def bview(request):
    return render(request,'bview.html')