from django.urls import path

from . import views

urlpatterns=[
	path('helloview/',views.HelloApiView.as_view())
]