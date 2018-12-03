from django.conf.urls import url
from . import viewslistform
from . import views
from . import viewsetudiants
urlpatterns=[
   url('form',views.FormulaireView.as_view(),name='get'),
   url('newuser',views.FormulaireView.as_view(),name='post'),
   url('etudiantsinfo/(?P<user>.+)',viewsetudiants.EtudiantsInfos.as_view(),name='get')
 

]