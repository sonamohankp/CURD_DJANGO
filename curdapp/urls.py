
from django.urls import path,include
from .import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('<int:id>/',views.home,name='update'),
    path('delete/<int:id>/',views.emplyee_del,name='employee_delete'),
    path('employee_list/',views.employee_list,name='employee_list'),
     path('login/',views.login_view, name='login'),
    path('',views.register_view, name='register'),
]
