from django.urls import path,include
from . import views

app_name='comment'
urlpatterns = [
    path('commlist/', views.commlist, name='commlist'),
    # ajax 댓글등록
    path('commWrite/', views.commWrite, name='commWrite'),
    # 댓글 삭제
    path('commDelete/', views.commDelete, name='commDelete'),
    # 댓글 수정 저장
    path('commUpdate/', views.commUpdate, name='commUpdate'),
]
