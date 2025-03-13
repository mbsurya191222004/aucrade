from django.urls import path
from . import views

urlpatterns = [
    path("allitems/", views.All_items.as_view()),
    path("sellingitems/", views.Selling_items.as_view()),
    path("sell/", views.post_item.as_view()),
    path("bid/", views.Bid.as_view()),
    path("check-auth/",views.check_auth),
]
