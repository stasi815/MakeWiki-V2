from django.urls import path

from api.views import PageList, PageDetail

urlpatterns = [
    path('', PageList.as_view(), name='page_list'),
    path('<str:slug>/', PageDetail.as_view(), name='page_detail')
]