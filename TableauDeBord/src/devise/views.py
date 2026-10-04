from django.shortcuts import render, redirect

from src import api


# Create your views here.

def redirect_page(request):
    return redirect("dashboard", days_range=30, currencies='EUR')

def dashboard(request, days_range = 30, currencies = "CAD"):

    days, rates = api.get_rates(currencies=currencies.split(","), nb_days=days_range)
    page_label = {7:"Semaine", 30:"Mois", 365:"Année"}.get(days_range, "Personalisé")
    return render(request, r"devise/index.html", context={"days": days, "rates": rates, "page_label": page_label, "currencies": currencies})
