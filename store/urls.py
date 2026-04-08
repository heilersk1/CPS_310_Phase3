from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # homepage
    path('login/', views.login_view, name='login'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('store/', views.store_page, name='store'), # store page
    path('events/', views.events_page, name='events'), # events page
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]
