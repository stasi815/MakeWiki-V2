from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new-page/', PageCreateView.as_view(), name='new-entry-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
