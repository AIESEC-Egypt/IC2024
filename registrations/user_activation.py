from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def send_setup_email(user):
    setup_token = default_token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    setup_link = reverse('setup_account', kwargs={'token': setup_token, 'uidb64': uidb64})
    print(user.delegate.aiesec_email)
    print(setup_link)
