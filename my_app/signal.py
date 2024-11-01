# signals.py
from django.dispatch import Signal
from django.dispatch import receiver
from django.contrib import messages


# Define the signal without providing_args
message_sent = Signal()
# message_sent = Signal(providing_args=["name", "email", "subject", "message"])


@receiver(message_sent)
def send_success_message(sender, **kwargs):
    name = kwargs.get('name')
    messages.success(sender, f"Thank you {name}, your message has been successfully sent!")
