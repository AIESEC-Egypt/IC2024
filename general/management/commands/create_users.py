# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from registrations.models import Delegate
# from django.urls import reverse
# from django.utils.http import urlsafe_base64_encode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator


# def send_setup_email(user):
#     setup_token = default_token_generator.make_token(user)
#     uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
#     setup_link = reverse('setup_account', kwargs={'token': setup_token, 'uidb64': uidb64})
#     return "http://127.0.0.1:8000/" + setup_link

# class Command(BaseCommand):
#     help = 'Creates user accounts for old data and sends emails'

#     def handle(self, *args, **options):
#         old_data_entries = Delegate.objects.all()

#         for entry in old_data_entries:
#             print(entry.personal_email)
#             # Extract relevant information from the old data entry
#             email = entry.aiesec_email
#             # You may need to map other fields like password, name, etc.

#             # Create a new user object
#             entry.user = User.objects.create_user(username=email, is_active=False)
#             entry.save()

#             setup_link = send_setup_email(entry)
#             delegate_name = entry.first_name

#             # Send email to the user
#             subject = '[IMP] IC Account Activation'
#             html_content = render_to_string('email_template.html', {'delegate_name': delegate_name, 'setup_link': setup_link})
#             text_content = strip_tags(html_content)  # Strip the HTML tags for the plain text version
#             msg = EmailMultiAlternatives(subject, text_content, 'international.congress_2024eg@aiesec.net', [email])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()

#         self.stdout.write(self.style.SUCCESS('Successfully created users and sent emails.'))