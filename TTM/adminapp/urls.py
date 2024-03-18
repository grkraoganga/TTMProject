from django.urls import path
from . import views
urlpatterns = [
   # path("adminhome",views.adminhome,name="adminhome"),
  #  path("adminlogout",views.logout,name="adminlogout"),
    path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
    path("checkRegistration",views.checkregistration,name="checkregistration"),
    path("checkpackages",views.checkpackages,name="checkpackages"),
    path("viewplaces",views.viewplaces,name="viewplaces"),
    path("changepassword",views.checkChangePassword,name="changepassword"),
    path("logout",views.logout,name="logout"),
    path("mail",views.mail,name="mail"),
    path("sendmail",views.sendmail,name="sendmail"),
]