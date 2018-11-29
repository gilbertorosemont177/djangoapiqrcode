from django.conf.urls import url
from . import views
urlpatterns=[
   url('form',views.FormulaireView.as_view(),name='get'),
   url('newuser',views.FormulaireView.as_view(),name='post')

]