from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # create
    path('create/', views.create, name='create'),
    # read
    path('', views.index, name='index'), # articles/ 경로가 들어오면 index 보여줌
    path('<int:id>/', views.detail, name='detail'),
    # update
    path('<int:id>/update/', views.update, name='update'),
    # delete
    path('<int:id>/delete/', views.delete, name='delete'),
    # Comment
    # Create
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
    

]