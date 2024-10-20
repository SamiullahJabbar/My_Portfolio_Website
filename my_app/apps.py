from django.apps import AppConfig
from my_app.signal import message_sent


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'



# apps.py
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'my_app'  # Replace with your actual app name

    def ready(self):
        import my_app.signal  # Ensure this points to the correct signals file


# @receiver(message_sent)
# def send_success_message(sender, **kwargs):
#     name = kwargs.get('name')
#     messages.success(sender, f"Thank you {name}, your message has been successfully sent!")

