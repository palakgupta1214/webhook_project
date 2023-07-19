import os
import django

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webhook_project.settings")
django.setup()

from webhook_app.models import Webhook

# Retrieve all webhook objects
webhooks = Webhook.objects.all()

# Print the webhook data
for webhook in webhooks:
    print("Webhook ID:", webhook.webhook_id)
    print("Name:", webhook.name)
    print("Email:", webhook.email)
    print()  # Add an empty line for separation
