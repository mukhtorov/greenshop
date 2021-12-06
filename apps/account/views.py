from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect


def test_logout(request):
    logout(request)
    return redirect("homepage")

