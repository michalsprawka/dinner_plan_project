from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [

    url(r'^adddinnesrshow/$', views.addDinnersShow, name='ads'),
    url(r'^adddinner/$', views.addDinner,name='add'),
    url(r'^adddinnerdate/$', views.addDinnerDate,name='adindate'),
    url(r'^dinnerdateshow/$', views.DinnerDateShow,name='dds'),
    url(r'^dinnersdelete/(?P<number>[0-9]+)/$', views.DinnersDelete,name='delete'),
    url(r'^dinnersdetail/(?P<number>[0-9]+)/$', views.DinnersDetail,name='detail'),
    url(r'^dinnersaddrecipe/(?P<number>[0-9]+)/$', views.DinnersAddRecipe,name='addrecipe'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^adddinnerdate/ajax/dinner_validate/$',views.validate_dinner,name='validate_dinner'),
    url(r'^dayschoice/$',views.DinnerChoice,name='dinerschoice'),


]
