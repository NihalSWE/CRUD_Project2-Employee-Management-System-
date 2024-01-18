from django.urls import path
from . import views


urlpatterns = [
    path("",views.base,name="Home"),
    path("allemp/",views.allemp,name="allemp"),
    path("add/",views.add,name="add"),
    path("remove/",views.remove,name="remove"),
    path("remove/<int:emp_id>",views.remove,name="remove"),
    path("update/<int:id>/",views.update,name="update"),
    path("search/",views.search,name="search"),
]
