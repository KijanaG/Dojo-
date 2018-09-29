from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.logreg),
    url(r'^registration$', views.registration),
    url(r'^main$', views.main),
    url(r'^login$', views.login),
    url(r'^new$', views.new_book),
    url(r'^add_both$', views.add_both),
    url(r'^show/(?P<book_id>\d+)$', views.show),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^delete/(?P<review_id>\d+)/(?P<book_id>\d+)$', views.delete),
    url(r'^user/(?P<user_id>\d+)$', views.user)
]