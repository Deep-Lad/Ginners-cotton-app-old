from bbc.views import index,about,admin,contact,forgot,owner,purchase,sigunp,staff,display
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("about", about, name="about"),
    path("admin", admin, name="admin"),
    path("contact", contact, name="contact"),
    path("forgot", forgot, name="forgot"),
    path("owner", owner, name="owner"),
    path("purchase", purchase, name="purchase"),
    path("signup", sigunp, name="signup"),
    path("staff", staff, name="staff"),
    path("display",display,name="display")
]