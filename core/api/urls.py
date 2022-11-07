from django.urls import path,include
from core.api.views import CurrencyListAPIView,CategoryModelViewSet,TransactionsModeldViewSet
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.SimpleRouter()
router.register('categories',CategoryModelViewSet,basename='category')
router.register('transactions',TransactionsModeldViewSet,basename='transaction')

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('',CurrencyListAPIView.as_view(),name='cur_list'),   
] + router.urls
