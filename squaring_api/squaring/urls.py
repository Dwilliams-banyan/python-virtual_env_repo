from django.urls import path

from squaring.views import SquaringView, HelloWorldView

urlpatterns = [
    path('', HelloWorldView.as_view()),
    path('<int:number>', SquaringView.as_view()),
]