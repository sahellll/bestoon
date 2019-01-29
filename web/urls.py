from  django.conf.urls import url
from . import views

urlpatterns = [
    url('submit/expense/$',  views.submit_expense, name='submit_expense'),
    url('submit/income/$', views.submit_income, name='submit_income'),
    url('account/register/$',views.register,name='register'),

]