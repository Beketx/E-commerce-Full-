from django.urls import path
from .views import*

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('products/',products_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/',CategoryAPIView.as_view()),
    path('categories/<int:category_id>/',CategoryDetailAPIView.as_view()),
    path('categories/<int:fk>/products/',category_product),
    path('products/feedback',FeedbackAPIView),
    path('cart/',cart_list),
    path('cart/<int:pk>',cart_list),
]