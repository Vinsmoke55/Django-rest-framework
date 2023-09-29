from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewset,basename='hello-viewset')
router.register('profile',views.UserProfileViewset,)
router.register('login',views.LoginViewSet,basename='login')

urlpatterns=[
	path('helloview/',views.HelloApiView.as_view()),
	path('',include(router.urls))
]