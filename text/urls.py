from django.urls import path,include
from .views import *
from django.urls import re_path
from authentication import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'snippets', SnippetModelViewSet)
urlpatterns = [
    path('tag/',Tags.as_view(),name='tag'),
    path('snippet/',Snippets.as_view(),name='snippet'),
    path('snippetbytagid/(?P<tag_id>[0-9]+)/$',SnippetByTagId.as_view(),name='snippetbytagid'),
    path('snippentbyid/(?P<pk>[0-9]+)/$',SnippetById.as_view(),name='snippentbyid'),
    path('overview/',Overview.as_view(),name='overview'),

    path('snippet/create', CreateSnippetView.as_view(),name="create-snippet"),
    path('snippet/detail/<int:pk>',SnippetDetailView.as_view(),name="snippet-detail"),
    path('snippet/update/<int:pk>',SnippetUpdateView.as_view(),name="snippet-update"),
    path('snippet/delete/bulk',SnippetDeleteView.as_view(),name="snippet-delete"),
    path('snippet/list',SnippetListView.as_view(),name="snippet-list"),
    path('', include(router.urls)),
]