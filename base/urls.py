from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('market/', market, name='market'),
    path('cart/', cart, name='cart'),
    path('product_info/<str:pk>/', product_info, name='product_info'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('searchResults/', search, name='search'),
    path('update-item/', update_item, name='update_item'),
]