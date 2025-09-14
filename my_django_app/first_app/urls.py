from django.urls import path
from first_app.views import home, not_found, HomeView, NotFoundView

urlpatterns = [
    path('', home, name='home'),
    path('not_found/', not_found, name='not_found'),
    path('class_home_page', HomeView.as_view(), name='class_home'),
    path('class_not_found', NotFoundView.as_view(), name='class_not_found'),
]