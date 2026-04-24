from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employee-login/', views.login_view, name='employee_login'),
    path('employee-logout/', views.logout_view, name='employee_logout'),


    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),

    path('store/', views.store_page, name='store_page'),
    path('events/', views.events_page, name='events_page'),
    path('job_postings/', views.jobs_page, name='job_postings'),    

    path('feedback_form/', views.feedback_page, name='feedback_form'),

    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
]
