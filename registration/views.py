from django.shortcuts import render, redirect, get_object_or_404
from .models import Registration


# CREATE
def registration(request):

    form_data = {
        'name': '',
        'email': '',
        'phone': '',
        'city': ''
    }

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        city = request.POST.get("city")

        Registration.objects.create(
            name=name,
            email=email,
            phone=phone,
            city=city
        )

    return render(request, "form.html")


# READ
def registration_list(request):

    registrations = Registration.objects.all()

    return render(
        request,
        "registration_list.html",
        {"registrations": registrations}
    )


# UPDATE
def registration_update(request, id):

    registration = get_object_or_404(Registration, id=id)

    if request.method == "POST":

        registration.name = request.POST.get("name")
        registration.email = request.POST.get("email")
        registration.phone = request.POST.get("phone")
        registration.city = request.POST.get("city")

        registration.save()

        return redirect('registration_list')

    return render(
        request,
        "registration_update.html",
        {"registration": registration}
    )


# DELETE
def registration_delete(request, id):

    registration = get_object_or_404(Registration, id=id)

    if request.method == "POST":

        registration.delete()

        return redirect('registration_list')

    return redirect('registration_list')