from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Core app routes
    path('', include('core.urls')),

    # Login Page
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    # Redirect after login
    path('redirect/', user_views.redirect_after_login, name='redirect_after_login'),
]



from django.contrib.auth import views as auth_views

urlpatterns += [
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
]
