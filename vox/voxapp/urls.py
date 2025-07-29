# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.login_view, name='login'),  # Show login page on /
#     path('home/', views.home, name='home'),    # Homepage now at /home
#     path('movies/', views.vox_list, name='vox_list'),
#     path('book/<int:movie_id>/', views.book_movie, name='book_movie'),
#     path('register/', views.register_view, name='register'),
#     path('payment/<int:movie_id>/', views.payment_page, name='payment_page'),
#     path('process-payment/', views.process_payment, name='process_payment'),
#     path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),  # Removed duplicate
# ]






from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Show login page on /
    path('home/', views.home, name='home'),    # Homepage now at /home
    path('movies/', views.vox_list, name='vox_list'),
    path('book/<int:movie_id>/', views.book_movie, name='book_movie'),
    path('register/', views.register_view, name='register'),
    path('payment/<int:movie_id>/', views.payment_page, name='payment_page'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('search/', views.search, name='search'),
]
