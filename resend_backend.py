from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
import resend

class ResendBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently, **kwargs)
        resend.api_key = settings.RESEND_API_KEY  # Set the API key globally

    def send_messages(self, email_messages):
        success = True
        for email in email_messages:
            try:
                resend.Emails.send({
                    "from": email.from_email,
                    "to": email.to,
                    "subject": email.subject,
                    "text": email.body
                })
            except Exception as e:
                success = False
                if not self.fail_silently:
                    raise e
        return success
