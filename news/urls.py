from django.urls import path
from .views import news, create_new, NewsDetailView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', news, name='news'),
    path('create/', create_new, name='create_new'),
    path('<int:pk>', NewsDetailView.as_view(), name='detail-view'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='update-new'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete-new'),
]
