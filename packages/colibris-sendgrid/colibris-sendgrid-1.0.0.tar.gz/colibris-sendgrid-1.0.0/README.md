
# SendGrid email backend for Colibris

In `settings.py`, set:

    EMAIL = {
        'backend': 'colibrissendgrid.SendGridBackend',
        'api_key': 'yourapikey'
    }
