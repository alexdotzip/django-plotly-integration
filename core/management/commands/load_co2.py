import csv
from datetime import date
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import Rokkr
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load data from CO2 file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'co2_mm_mlo.csv'

        with open(datafile, 'r' as csvfile):
            reader = csv.DictReader(csvfile)
        raise NotImplementedError