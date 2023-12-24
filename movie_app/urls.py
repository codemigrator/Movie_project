from django.urls import path
from. import views

app_name = 'movieapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:movie_id>/', views.details, name='details'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('search', views.search, name='search')

]
