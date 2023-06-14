from django.urls import path
from . import views


# We can use int/str: to check for types in the url
urlpatterns = [
    # path('january', views.jan_index),
    # path('february', views.feb_index),
    # path('march', views.march_index),
    path('', views.index),
    path('<int:cur_month>', views.index_monthly_challenge),
    path('<str:cur_month>', views.monthly_challenge),
]
