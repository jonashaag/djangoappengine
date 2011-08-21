from email.utils import make_msgid
from django.core.mail.backends.console import EmailBackend
from ..utils import appid

class ConsoleBackend(EmailBackend):
    def send_messages(self, email_messages):
        return super(ConsoleBackend, self).send_messages(
            self._inject_msgid(email_messages))

    def _inject_msgid(self, email_messages):
        for msg in email_messages:
            msg['Message-ID'] = make_msgid(domain=appid)
            yield msg
