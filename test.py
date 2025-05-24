import smtplib

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("officeopsnoreply@gmail.com", "ijumzywfwctsjmsm")
    print("Login successful ✅")
    server.quit()
except smtplib.SMTPAuthenticationError as e:
    print("Login failed ❌:", e)
except Exception as e:
    print("An error occurred ❗", e)
