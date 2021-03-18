from django.urls import path

from appearance.views import AppearanceView

app_name = "appearance"
urlpatterns = [
    path('appearance/', AppearanceView.as_view()),
]
