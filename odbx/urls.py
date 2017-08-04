# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'odbx.views.home', name='home'),
    # url(r'^odbx/', include('odbx.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('odbx.api.urls', namespace='api')),
    # url(r'^alarms/', include('odbx.alarms.urls', namespace='alarms')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^i18n/setlang/$', 'django.views.i18n.set_language', name='set_language'),
)

urlpatterns += patterns(
    '',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns += patterns(
    '',
    url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^token/refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
)


from django.conf import settings

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

    from django.views.generic import TemplateView
    urlpatterns += patterns('',
        url(r'^$', TemplateView.as_view(template_name='index.html')),
    )


if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
