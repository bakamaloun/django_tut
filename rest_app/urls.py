from django.urls import path
from django.views.generic import TemplateView
from rest_app.views import restListView, restDetailView

urlpatterns = [
    path('rest_app/', TemplateView.as_view(template_name='rest_app/rest_app.html'), name='rest_app'),
    path('rest_app/api/request', restListView.as_view()),
    path('rest_app/api/request/<pk>', restDetailView.as_view()),
]