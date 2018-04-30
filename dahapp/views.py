from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RemitForm, PayForm, ChequeForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            # cleaned (Sanitized Data)
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login.html')
                else:
                    return HttpResponse('Disable Account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dahapp/dashboard.html', {'section': 'dashboard'})


def reports(request):
    return render(request, 'dahapp/reports.html', {'reports': 'reports'})


def remittance(request):
    # all_remittance = Remittance.objects.all()
    # Latest_remit = Remittance.objects.latest()

    if request.method == 'POST':
        form = RemitForm(request.POST or None)
        if form.is_valid():
            remit = Remittance()
            remit.usd = form.cleaned_data['usd']
            remit.djf = form.cleaned_data['djf']
            remit.created_on = timezone.now()
            remit.created_by = request.user
            remit.save()
            messages.success(request, 'Well Done! You have successfully saved Today\'s Remittance.')
        else:
            messages.error(request, 'The data is not correctly stored. Please Try again!')
    else:
        form = RemitForm(request.POST or None)
    return render(request, 'dahapp/remittance.html', {'form': form})


def payment(request):
    # all_payment = Payment.objects.all()

    if request.method == 'POST':
        form = PayForm(request.POST or None)
        if form.is_valid():
            pay = Payment()
            pay.usd = form.cleaned_data['usd']
            pay.djf = form.cleaned_data['djf']
            pay.created_on = timezone.now()
            pay.created_by = request.user
            pay.save()
            messages.success(request, 'Well Done! You have successfully saved Today\'s Payment.')
        else:
            messages.error(request, 'The data is not correctly stored. Please Try again!')
    else:
        form = PayForm(request.POST or None)
    return render(request, 'dahapp/payments.html', {'form': form})


def opening_balance(request):
    all_opening_balance = OpeningBalance.objects.all()
    return render(request, 'dahapp/opening_balance.html', {'all_opening_balance': all_opening_balance})


def stamps(request):
    all_stamp = Stamp.objects.all()
    return render(request, 'dahapp/stamps.html', {'all_stamp': all_stamp})


def cheques(request):
    # all_cheque = Cheque.objects.all()

    if request.method == 'POST':
        form = ChequeForm(request.POST or None)
        if form.is_valid():
            cheques = Cheque()
            cheques.cheque_no = form.cleaned_data['cheque_no']
            cheques.bank_name = form.cleaned_data['bank_name']
            cheques.customer_name = form.cleaned_data['customer_name']
            cheques.amount = form.cleaned_data['amount']
            cheques.currency = form.cleaned_data['currency']
            cheques.created_on = timezone.now()
            cheques.created_by = request.user
            cheques.save()
            messages.success(request, 'Well Done! You have successfully saved The data.')
        else:
            messages.error(request, 'The data is not correctly stored. Please Try again!')
    else:
        form = ChequeForm(request.POST or None)
    return render(request, 'dahapp/cheques.html', {'form': form})


def transfer(request):
    all_transfer = Transfer.objects.all()
    return render(request, 'dahapp/transfer.html', {'all_transfer': all_transfer})


def vouchers(request):
    all_vouchers = Vouchers.objects.all()
    return render(request, 'dahapp/expenses.html', {'all_vouchers': all_vouchers})


def deposit(request):
    all_deposit = Deposit.objects.all()
    return render(request, 'dahapp/deposit.html', {'all_deposit': all_deposit})


def withdrawal(request):
    all_withdrawal = Withdrawal.objects.all()
    return render(request, 'dahapp/withdrawal.html', {'all_withdrawal': all_withdrawal})


def loans(request):
    all_loan = Loan.objects.all()
    return render(request, 'dahapp/loans.html', {'all_loan': all_loan})


def refunds(request):
    all_refund = Refund.objects.all()
    return render(request, 'dahapp/refunds.html', {'all_refund': all_refund})
