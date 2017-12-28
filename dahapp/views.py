from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import *


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
    all_remittance = Remittance.objects.all()
    return render(request, 'dahapp/remittance.html', {'all_remittance': all_remittance})


def payment(request):
    all_payment = Payment.objects.all()
    return render(request, 'dahapp/payments.html', {'all_payment': all_payment})


def opening_balance(request):
    all_opening_balance = OpeningBalance.objects.all()
    return render(request, 'dahapp/opening_balance.html', {'all_opening_balance': all_opening_balance})


def stamps(request):
    all_stamp = Stamp.objects.all()
    return render(request, 'dahapp/stamps.html', {'all_stamp': all_stamp})


def cheques(request):
    all_cheque = Cheque.objects.all()
    return render(request, 'dahapp/cheques.html', {'all_cheque': all_cheque})


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
