from django.shortcuts import render
from django.http import JsonResponse
import json

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

def paid_webhook(request):
    """ Webhook لاستقبال بيانات الدفع من فواتيرك """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("✅ Payment Data Received:", data)

            # الحصول على حالة الدفع من بيانات الاستجابة
            payment_status = data.get("status")  # تأكد من أن المفتاح صحيح حسب استجابة فواتيرك
            
            if payment_status == "paid":
                return JsonResponse({"redirect_url": "/form/"})  # إعادة التوجيه إلى الفورم عبر JSON
            
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"status": "received"}, status=200)
