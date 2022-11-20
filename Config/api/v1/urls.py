from django.urls import path, include

app_name = 'api-v1'

urlpatterns = [
    path('', include('portfolio.urls')),
    # path('auth/', include('coreapp.api.urls')),
]
