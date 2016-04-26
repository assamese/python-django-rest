from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from post import views

urlpatterns = patterns('',
	url(r'^(?P<post_id>\d+)/$', 'post.views.post'),
 	url(r'^api/$', views.PostList.as_view()),
 	url(r'^api/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)

# (?P<pk>[0-9]+)/$
# , allowed=['json', 'html']
#  	url(r'^api\.(?P<format>(json|html))/?$', views.PostDetail.as_view()),
