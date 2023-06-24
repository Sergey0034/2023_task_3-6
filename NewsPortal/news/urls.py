from django.urls import path
from .views import NewList, NewDetail


urlpatterns = [
   path('', NewList.as_view()),
   path('<int:id>', NewDetail.as_view())
]