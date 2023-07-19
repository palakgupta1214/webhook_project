from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Webhook
import uuid
from django.views.decorators.csrf import csrf_exempt
import json

def generate_unique_id():
    return str(uuid.uuid4())

from django.http import JsonResponse

@csrf_exempt ##handle request from external call
def create_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', '')
            email = data.get('email', '')
        except json.JSONDecodeError:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
    else:
        name = request.GET.get('name', '')
        email = request.GET.get('email', '')

    unique_id = generate_unique_id()

    webhook = Webhook.objects.create(
        webhook_id=unique_id,
        name=name,
        email=email,
    )
    return JsonResponse({
        'webhook_id': webhook.webhook_id,
        'name': webhook.name,
        'email': webhook.email
    })

def webhook_detail(request, webhook_id):
    webhook = get_object_or_404(Webhook, webhook_id=webhook_id)

    if request.method == 'POST':
        webhook.data = request.POST.get('data', '')
        webhook.save()

    return render(request, 'webhook_detail.html', {'webhook': webhook})


def home(request):
    return render(request, 'home.html')




# @csrf_exempt
# def create_webhook(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             name = data.get('name', '')
#             email = data.get('email', '')
#         except json.JSONDecodeError:
#             name = request.POST.get('name', '')
#             email = request.POST.get('email', '')
#     else:
#         # return JsonResponse({'error': 'Invalid request method'}, status=400)
#         return JsonResponse({'message': "success"})
#         #  return JsonResponse({'webhook_id': webhook.webhook_id})
#     unique_id = generate_unique_id()

#     webhook = Webhook.objects.create(
#         webhook_id=unique_id,
#         name=name,
#         email=email,
#     )
#     return JsonResponse({'webhook_id': webhook.webhook_id})


















































