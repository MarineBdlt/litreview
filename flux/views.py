from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from flux import forms, models as flux_models
from authentication import models as auth_models
from django.core.paginator import Paginator
from itertools import chain
from django.db.models import CharField, Value, Q


@login_required
def home(request):
    relations = auth_models.UserFollow.objects.filter(user__exact=request.user)

    tickets = flux_models.Ticket.objects.filter(
        Q(user__id__in=relations.values_list("followed_user"))
        | Q(user__exact=request.user)
    )
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    reviews = flux_models.Review.objects.filter(
        Q(user__id__in=relations.values_list("followed_user"))
        | Q(user__exact=request.user)
    )
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )

    paginator = Paginator(posts, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "home.html", context=context)


@login_required
def profil(request):
    tickets = flux_models.Ticket.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    reviews = flux_models.Review.objects.filter(user=request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    profil = request.user

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )

    paginator = Paginator(posts, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    header = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "header": header, "profil": profil}
    return render(request, "profil.html", context=context)


@login_required
def ticket_list(request):
    tickets = flux_models.Ticket.objects.all()
    tickets_ordered = tickets.order_by("-time_created")

    paginator = Paginator(tickets_ordered, 6)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, "ticket_list.html", context=context)


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(flux_models.Ticket, id=ticket_id)
    reviews = sorted(
        flux_models.Review.objects.filter(ticket=ticket),
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
            ticket.user = request.user
            ticket.save()
            return redirect("home")
    return render(request, "add_ticket.html", context={"form": form})


@login_required
def add_review(request, ticket_id):
    ticket = get_object_or_404(flux_models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()

    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        review = review_form.save(commit=False)
        review.user = request.user
        review.ticket = ticket
        print(review.rating)
        print(review.body)
        review.save()
        return redirect("review_added")

    context = {
        "instance": ticket,
        "review_form": review_form,
    }
    return render(request, "add_review.html", context=context)


@login_required
def add_ticket_and_review(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == "POST":
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("review_added")

    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "add_ticket_and_review.html", context=context)


def review_added(request):
    return render(request, "review_added.html")
