from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import ChangePasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name="home"),
    path('productdetail/<int:pk>', views.ProductDetailsView.as_view(), name="product-details"),
    path('productdetail/<int:pk>', views.ProductDetailsView.as_view(), name="product-details"),
    path('mobile/', views.mobile, name="mobile"),
    path('mobile/<slug:data>', views.mobile, name="mobiledata"),

    path('registration/',views.CustomerRegistrationView.as_view(),name="customerregistration"),

    path('login/',views.CustomerLoginView.as_view(),name='customerlogin'),

    path('logout/',auth_views.LogoutView.as_view(next_page='customerlogin'),name='logout'),

    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=ChangePasswordForm,success_url='passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'),name='passwordchangedone'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 