from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from apps.account.forms import *


def test_logout(request):
    logout(request)
    # messages.info(request, "You have successfully logged out.")
    return redirect("homepage")
