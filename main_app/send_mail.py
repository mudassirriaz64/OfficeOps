from django.core.mail import send_mail
from django.conf import settings

def send_leave_request_email(employee_name, leave_reason):
    subject = f"Leave Request from {employee_name}"
    message = f"""
    Dear Admin,

    {employee_name} has requested leave for the following reason:
    {leave_reason}

    Please review the request at your earliest convenience.

    Regards,
    OfficeOps System
    """
    recipient_list = [settings.ADMIN_EMAIL]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

def send_leave_approval_email(employee_name, employee_email, leave_date, leave_message):
    subject = "Leave Request Approval"
    message = f"""
    Dear {employee_name},

    Your leave request for {leave_date} has been approved.

    Reason: {leave_message}

    Regards,
    OfficeOps Admin
    """
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [employee_email])