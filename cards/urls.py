from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [

    # This path takes over the responsibility from flashcards/urls.py of dispatching URLss
    # path(
    #     "",
    #     TemplateView.as_view(template_name="cards/base.html"),
    #     name="home"
    # ),

    # showing all cards + boxes in frontend
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),

    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),


    # Note the <int:pk> pattern in the route
    # that points to the CardUpdateView.
    # Since we're editing an existing card,
    # we need a primary key (pk) to identify
    # which card you want to update.
    # ex. http://127.0.0.1:8000/edit/2
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),

    path(
        # By adding <int:box_num> into the URL pattern,
        # Django hands over this box_num as a keyword
        # argument to the view.
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name="box"
    ),
]
