from cmath import log
from urllib.error import HTTPError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from flux import models, forms
from django.core.paginator import Paginator
from itertools import chain

from django.db.models import CharField, Value
from django.shortcuts import render
from urllib.error import HTTPError

# Create your views here.


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()

    # reviews = get_users_viewable_reviews(request.user)
    # returns queryset of reviews
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    # tickets = get_users_viewable_tickets(request.user)
    # returns queryset of tickets
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )

    paginator = Paginator(posts, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "home.html", context=context)


@login_required
def ticket_list(request):
    tickets = models.Ticket.objects.all()
    tickets_ordered = tickets.order_by("-time_created")

    paginator = Paginator(tickets_ordered, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "ticket_list.html", context=context)


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
        "ticket": ticket,
        "reviews": reviews,
    }
    return render(request, "ticket_detail.html", context=context)


@login_required
def add_ticket(request):
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # set the uploader to the user before saving the model
            ticket.user = request.user
            # now we can save
            ticket.save()
            return redirect("home")
    return render(request, "add_ticket.html", context={"form": form})


@login_required
def add_review(request):
    form = forms.ReviewForm()
    if request.method == "POST":
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            # set the uploader to the user before saving the model
            review.user = request.user
            # now we can save
            review.save()
            return redirect("home")
    return render(request, "partials/add_review_snippet.html", context={"form": form})


def add_ticket_and_review(request, ticket_id):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    context = {}

    try:
        ticket = get_object_or_404(models.Ticket, id=ticket_id)
        ticket_id = ticket.id
        context.update({"post": ticket})
    except:
        if request.method == "POST":
            if ticket_form.is_valid:
                ticket = ticket_form.save(commit=False)
                ticket.user = request.user
                ticket.save()
            context.update({"post": ticket})

    if request.method == "POST":
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
        return redirect("review_added")

    context.update(
        {
            "ticket_id": ticket_id,
            "ticket_form": ticket_form,
            "review_form": review_form,
        }
    )
    return render(request, "add_review.html", context=context)


def review_added(request):
    return render(request, "review_added.html")
