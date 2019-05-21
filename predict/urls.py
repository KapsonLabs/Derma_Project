from django.urls import path, include
from .views import PredictData

urlpatterns = [
    path('predict_data/', PredictData.as_view(), name="predict"),
]