from django.urls import path
from . import views

app_name = 'properties'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:property_id>/', views.detail, name='detail'),
    path('<int:property_id>/trade/', views.trade, name='trade'),

]
