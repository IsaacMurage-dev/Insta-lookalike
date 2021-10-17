from django.conf.urls import url,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
url(r'^signup/',views.signup,name='signup'),
url(r'^$',views.home,name='Home',),
url(r'^timeline/',views.index,name='Index'),
url(r'^profile/(\d+)',views.first_profile,name='Profile'),
url(r'^images/',views.add_image,name='Image'),
url(r'^details/(\d+)',views.details,name='Details'),
url(r'^search/',views.search_profile, name='Search'),
url(r'^nav/(\d+)',views.nav,name='Nav'),
url(r'^comments/(\d+)',views.comment,name='Comment'),
url(r'^likes/(\d+)',views.like_post,name="like_post"),
url(r'^follow/(\d+)',views.follow,name="Follow"),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
