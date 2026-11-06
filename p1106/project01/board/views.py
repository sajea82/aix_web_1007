from django.shortcuts import render,redirect
from django.db.models import F,Q
from board.models import Board
from django.conf import settings
from django.conf.urls.static import static
import os
from member.models import Member
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def blist(request):
    if request.method == 'GET':
    # 전체 게시글
        qs = Board.objects.all().order_by('-bgroup', 'bstep')
        # 페이지수
        paginator = Paginator(qs,5)
        # 현재 페이지 번호
        page = int(request.GET.get('page',1))
        p_qs = paginator.get_page(page)

        # 템플릿으로 데이터 전달
        context = {'list':p_qs, 'page':page}
        return render(request,'blist.html', context)

    elif request.method == 'POST':
        # 카테고리와 검색어 가져오기
        category = request.POST.get('category')
        search_word = request.POST.get('search_word')
        # 조건에 따른 필터링 처리
        if category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search_word).order_by('-bgroup','bstep')
        elif category == 'bcontent':
            qs = Board.objects.filter(bcontent__contains=search_word).order_by('-bgroup','bstep')
        else:
            # 제목 + 내용 통합 검색
            qs = Board.objects.filter\
                (Q(btitle__contains=search_word) | Q(bcontent__contains=search_word)).order_by('-bgroup','bstep')
            
        # 검색된 결과에 페이징 적용하기
        paginator  = Paginator(qs, 5)
        page = int(request.GET.get('page',1))
        p_qs = paginator.get_page(page)

        context = {'list':p_qs,'page':page}
        return render(request, 'blist.html', context)

    

# 게시글 등록
# GET - 페이지열기, POST - 저장
def bwrite(request):
    if request.method == 'GET':
        return render(request, 'bwrite.html')
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        id = request.session['session_id']
        bcontent = request.POST.get('bcontesnt')
        bfile = request.FILES.get('bfile')
        print(f'데이터 확인 : {btitle},{id},{bcontent},{bfile}')
        member = Member.objects.get(id=id)
        qs = Board.objects.create(btitle=btitle,member=member,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()

        context = {'temp':1}
        return render(request, 'bwrite,html',context)



# 게시글 상세보기
def bview(request,bno):
    return render(request, 'bwiew.html')