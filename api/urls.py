from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


from api import views

urlpatterns = [
    url('students/', views.StudentList.as_view()),
    # url('students/<int:pk>/', views.StudentDetail.as_view()),
    url('note/', views.NoteList.as_view()),
    url('note/(?P<pk>[0-9]+)/', views.NoteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
