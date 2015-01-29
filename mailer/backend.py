from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend

from mailer.models import Message


class DbBackend(BaseEmailBackend):

    def send_messages(self, email_messages):
        num_sent = 0
        subject_prefix = getattr(settings, 'MAILER_EMAIL_SUBJECT_PREFIX', None)
        for email in email_messages:
            if subject_prefix:
                email.subject = u'%s %s' % (subject_prefix, email.subject)
            msg = Message()
            msg.email = email
            msg.save()
            num_sent += 1
        return num_sent
