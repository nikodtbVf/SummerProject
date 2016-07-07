from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:

    url(r'^face_detection/detect/$', 'face_detector.views.detect'),
    url(r'^face_detection/image/$', 'face_detector.views.image'),
    url(r'^face_detection/addPerson/$', 'face_detector.views.addperson'),
    url(r'^face_detection/getInfo/$', 'face_detector.views.getinfo'),

    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)