from django.conf.urls import url
from . import views
urlpatterns=[
url('form',views.index,name='index')

]