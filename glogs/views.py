from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_daraja.mpesa.core import MpesaClient
from glogs.models import Paid


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


def Pay(request):
    if request.method == 'POST':
        payment = MpesaClient()
        account_reference = 'reference'
        phone_number = request.POST.get('phone')
        amount_str = request.POST.get('amount')

        try:
            amount = int(amount_str)
        except ValueError:
            messages.error(request, "Invalid amount. Please enter a valid integer.")
            return render(request, 'pay.html')

        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment'

        response = payment.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        HttpResponse(response, 'index.html')
        data = Paid(phone=phone_number, amount=int('amount'),)
        data.save()
        messages.success(request, f"Congratulations! Your payment of {{ amount }} has been successfully made!")
        return redirect("index.html")
    return render(request, 'pay.html')

#
# def paid(request):
#     all_paid = Paid.objects.all()
#     context = {"paid": all_paid}
#     return render(request, 'index.html', context)
