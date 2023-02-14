from django.urls import reverse_lazy
import random
from django.shortcuts import get_object_or_404, redirect
from .forms import CardCheckForm

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from .models import Card

# Create your views here.


class CardListView(ListView):
    # Card comes from models.py
    model = Card

    # adding - before date_created means descending order (old card first)
    queryset = Card.objects.all().order_by("box", "-date_created")


class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    # reverse() returns a string & reverse_lazy() returns an <object>
    # reverse() use in funcation & reverse_lazy() use in class.
    success_url = reverse_lazy("card-create")


# Took advantage of existing CardCreateView
class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")


class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm


    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))
