from django.urls import path
from .import views

urlpatterns = [
    path('test/',views.test,name="test"),
    path('',views.index,name='dashboard'),
    
    path('e-table/',views.employeesTable,name='e_table'),
    path('e-create/',views.employeCreate,name='e_create'),
    path('e-update/<str:pk>',views.updateEmployee,name='e_update'),
    path('e-delete/<str:pk>',views.employeDelete,name='e_delete'),
    
    path('p-table',views.productsTable,name="p_table"),
    path('n-table',views.noutbookTable),
    
    path('register/',views.registerUser,name='register'),
    path('login',views.loginUser,name='login'),
     path('logout/', views.logoutUser, name='logout_user'),
]
