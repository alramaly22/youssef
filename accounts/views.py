from django.shortcuts import render
from django.http import JsonResponse
import json
import requests

# ------------------- الصفحات الأساسية -------------------

def index(request):
    return render(request, 'accounts/index.html')

def about(request):
    return render(request, 'accounts/about.html')

def form(request):
    return render(request, 'accounts/form.html')

def calc(request):
    return render(request, 'accounts/calc.html')

def calc2(request):
    return render(request, 'accounts/calc2.html')

def card(request):
    return render(request, 'accounts/card.html')

def wheel(request):
    return render(request, 'accounts/wheel.html')

def book(request):
    return render(request, 'accounts/book.html')


# ------------------- دالة تحديد الموقع والعملة -------------------

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def location_view(request):
    ip = get_client_ip(request)

    # لو Localhost
    if ip in ["127.0.0.1", "localhost"]:
        return JsonResponse({
            "country": "EG",
            "currency": "EGP"
        })

    try:
        url = f"https://ipinfo.io/{ip}/json?token=5f01ba4857444e"
        res = requests.get(url, timeout=5)
        data = res.json()

        country = data.get("country", "US")

    except Exception as e:
        print("IP ERROR:", e)
        country = "US"

    # 3 حالات بس
    if country == "EG":
        currency = "EGP"
    elif country == "SA":
        currency = "SAR"
    else:
        currency = "USD"

    return JsonResponse({
        "country": country,
        "currency": currency
    })


# ------------------- Webhook فواتيرك -------------------

def paid_webhook(request):
    """Webhook لاستقبال بيانات الدفع من فواتيرك"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("✅ Payment Data Received:", data)

            # الحالة المستلمة من فواتيرك
            payment_status = data.get("status")

            if payment_status == "paid":
                return JsonResponse({"redirect_url": "/form/"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"status": "received"}, status=200)
