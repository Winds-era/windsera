from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', include('user_account.urls')),
                  path('content/', include('website_content.urls')),
                  path('admin/', admin.site.urls),

                  # password Reset
                  path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
                      template_name='registration/password_change_done.html'), name='password_change_done'),
                  path('password_change/',
                       auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
                       name='password_change'),
                  path('password_reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(
                           template_name='registration/password_reset_done.html'),
                       name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
                       name='password_reset_confirm'),
                  path('password_reset/', auth_views.PasswordResetView.as_view(),
                       name='password_reset'),
                  path('reset/done/',
                       auth_views.PasswordResetCompleteView.as_view(
                           template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

                  # quiz section
                  path('quiz/', include('quiz.urls', namespace='quiz')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
