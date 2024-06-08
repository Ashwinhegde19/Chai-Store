from . import views
from django.urls import path

urlpatterns = [
    path('', views.allchai, name='allchai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
    
]