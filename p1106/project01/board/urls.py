from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('bwrite/', views.bwrite,name='bwrite'),       # 게시글 등록
    path('blist/', views.blist,name='blist'),          # 게시글 리스트
    path('bview/<int:bno>', views.bview,name='bview'), # 게시글 상세보기
]
