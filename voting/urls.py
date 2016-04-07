from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voting.views.home', name='home'),
    # url(r'^voting/', include('voting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$|^home/$','voting_app.views.home'),
     url(r'^success/$','voting_app.views.success'),
     url(r'^quiz-authenticate/$','voting_app.views.quizauthenticate'),
     url(r'^validate/$','voting_app.views.adminvalidate'),
     url(r'^quiz_creation/$','voting_app.views.quizcreation'),
     url(r'^quiz-success/$','voting_app.views.quizsuccess'),
     url(r'^quiz/$','voting_app.views.quiz'),
     url(r'^ques-success/$','voting_app.views.quessuccess'),
     url('^logout/$','voting_app.views.logout'),
 #    url('^share/$','voting_app.views.share'),
)
