import qrcode
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import get_template
from django.core.files.base import ContentFile
from django.conf import settings
import os
from xhtml2pdf import pisa
from .forms import CertificateForm
from .models import Certificate

def certificate_form_view(request):
    if request.method == "POST":
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Certificate saved successfully!")
            return redirect("certificate_list")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CertificateForm()
    
    return render(request, "certificate_form.html", {"form": form})

def certificate_list_view(request):
    certificates = Certificate.objects.all()
    return render(request, "certificate_list.html", {"certificates": certificates})

from io import BytesIO
import qrcode
from django.core.files.base import ContentFile
import base64


def download_certificate_pdf(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    template_path = "certificate_pdf.html"
    context = {"certificate": certificate}

    # Generate QR Code dynamically
    qr_data = f"{request.build_absolute_uri('/certificates/')}{certificate.id}/"
    qr = qrcode.make(qr_data)
    
    # Save the QR code to an in-memory file
    qr_image = BytesIO()
    qr.save(qr_image, format='PNG')
    qr_image.seek(0)
    
    # Convert the in-memory image to base64 for embedding in the PDF
    qr_code_data = base64.b64encode(qr_image.read()).decode('utf-8')
    context['qr_code_data'] = qr_code_data
    
    # Add the absolute path of the photo to the context
    if certificate.photo:
        context['photo_path'] = certificate.photo.path
    else:
        context['photo_path'] = None

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="certificate_{certificate.id}.pdf"'
    
    # Render the HTML to PDF
    template = get_template(template_path)
    html = template.render(context)

    # Generate PDF
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)
    
    return response


from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")


from django.shortcuts import render, get_object_or_404
from .models import Certificate

def certificate_detail(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    return render(request, 'certificate_detail.html', {'certificate': certificate})
