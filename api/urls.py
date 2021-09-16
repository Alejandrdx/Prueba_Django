from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('user', views.UserViewSet)
router.register('country', views.CountryViewSet)
router.register('city', views.CityViewSet)
router.register('game', views.GameViewSet)



urlpatterns = [
      path('', include(router.urls)),
      path('login/', views.UserLoginApiView.as_view())
]