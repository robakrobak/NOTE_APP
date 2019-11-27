from django.core.mail import send_mail
from NoteApp.settings import EMAIL_HOST_USER


def confirms_registration(email, username, password):
    subject = 'Register confirmation'
    message = f'Registration complete.\nEmail address: {email}\nUsername: {username}\nPassword: {password}\n' \
              f'Do not show this password to anyone who want to crack your precious Python code.\n' \
              f'Stay cool. There is nothing to worry about.'
    from_email = EMAIL_HOST_USER
    to_list = [email, EMAIL_HOST_USER]

    send_mail(subject, message, from_email, to_list, fail_silently=False)


def password_reset_fail(email):
    subject = 'NoteApp password reset'
    message = 'You have no account in our service.\n\n Sincerely, \n The NoteApp Team'
    from_email = EMAIL_HOST_USER
    to_list = [email, ]
    send_mail(subject, message, from_email, to_list, fail_silently=False)


def note_assign_mail(email, title):
    send_mail(
        subject="You have been assigned(...)",
        message=f"You have been assigned to note '{title}'."
                f"Check your current status at NOTE_APP application",
        from_email="noteapp12345@gmail.com",
        recipient_list=[user.email for user in email])
