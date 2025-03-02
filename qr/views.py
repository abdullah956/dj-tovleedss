from django.contrib import messages
from .forms import CertificateForm
from .models import Certificate
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("all_records")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

def certificate_form_view(request):
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Certificate saved successfully!")
            return redirect("all_records")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CertificateForm()
    
    return render(request, "certificate_form.html", {"form": form})

def validate_now (request):
    return render(request,"validate-now.html")

def track_equipment (request):
    return render(request,"track_equipment.html")

def track_operator(request):
    certificates = None
    message = None
    if request.method == "GET":
        card_no = request.GET.get("cardNo", "").strip()
        iqama_number = request.GET.get("iqamaNumber", "").strip()
        if card_no or iqama_number:
            certificates = Certificate.objects.filter(card_no=card_no, iqama_number=iqama_number)
            if certificates.exists():
                return render(request, "search_operator.html", {"certificates": certificates})
            else:
                return render(request, "search_operator.html", {"message": "No records found."})
    return render(request, "track_operator.html", {"certificates": certificates, "message": message})

def all_records_view(request):
    certificates = Certificate.objects.all()
    return render(request, "all_records.html", {"certificates": certificates})
