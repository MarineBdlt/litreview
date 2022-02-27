from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from flux import models
from django.core.paginator import Paginator

# Create your views here.


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    tickets_ordered = tickets.order_by("-time_created")

    paginator = Paginator(tickets, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "home.html", context=context)


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    print("ticket", ticket, ticket.title)
    reviews = sorted(
        models.Review.objects.filter(ticket=ticket),
        key=lambda instance: instance.time_created,
        reverse=True,
    )
    context = {
        "title": ticket.title,
        "description": ticket.description,
        "author": ticket.user,
        "image": ticket.image.url,
        "time": ticket.time_created,
        "reviews": reviews,
    }

    # ticket_and_reviews = {}
    return render(request, "ticket_detail.html", context=context)
