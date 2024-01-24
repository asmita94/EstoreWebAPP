from django.urls import path
from msgqpp import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   # path('testing',views.testing),
    path('home2',views.home2),
    path('home3',views.home3),
     path('pd/<pid>',views.pd),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('updategty/<qv>/<cid>',views.updategty),
     path('addcart/<pid>',views.addcart),
     path('remove/<cid>',views.remove),
    path('cart',views.cart),
    path('registration',views.registration),
    path('login',views.login_user),
    path('range',views.range),
    path('contact',views.contact),
    path('pd',views.product_details),
    path('place_order',views.place_order),
    path('logout',views.user_logout),
    path('create',views.create),
    path('dashbord',views.dashbord),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('sendmail',views.sendusermail),
    path('makepayment',views.makepayment),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


