from django.urls import path

from demoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('userhome',views.userhome,name='userhome'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('add_questions', views.add_questions, name='add_questions'),
    path('question_view_admin', views.question_view_admin, name='question_view_admin'),
    path('delete_question/<int:id>/', views.delete_question, name='delete_question'),
    path('test',views.test,name='test'),

    ]