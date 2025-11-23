from django.urls import path, include
from .views import *
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'tickets', ITSM_Ticket_ViewSet)


urlpatterns = [
    path('', index, name='home'),
    path('api/', include(router.urls)),
    path('users', users, name='users'),
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('reset/',pass_reset, name='pass_reset'),
]