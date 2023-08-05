from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
import logging

class Command(BaseCommand):
    help = 'Runs CRON jobs for given frequency'
    can_import_settings = True

    def add_arguments(self, parser):
        parser.add_argument('frequency', nargs = 1, type = int)

    def handle(self, *args, **options):
        from congo.conf import settings

        model_name = settings.CONGO_CRON_MODEL
        if not model_name:
            raise ImproperlyConfigured("In order to use Cron model, configure settings.CONGO_CRON_MODEL first.")
        model = apps.get_model(*model_name.split('.', 1))

        frequency = options['frequency'][0]
        frequency_dict = dict(model.FREQUENCY_CHOICE)
        try:
            frequency_label = frequency_dict[frequency]
        except KeyError:

            message = "CRON jobs for frequency @ %s" % options['frequency'][0]
            logger = logging.getLogger('system.cron')
            logger.error(message)

            raise CommandError('Incorrect frequency argument. Valid values are: %s' % ', '.join(frequency_dict.keys()))

        message = "CRON jobs for frequency %s (%s) invoked" % (frequency, frequency_label)
        extra = {}

        logger = logging.getLogger('system.cron')
        logger.debug(message, extra = extra)

        i = j = 0

        for cron in model.objects.filter(frequency = frequency, is_active = True):
            if cron.run_job(None):
                i += 1
            j += 1

#        self.stdout.write("%s (%s / %s)" % (message, i, j))
