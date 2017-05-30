from django.core.management.base import BaseCommand, CommandError
from leave.models import employee

class Command(BaseCommand):

	help = "This event would be run daily by crontab for leave to be carried over the next year if the current day is the first day of the year"

	def handle(self, *args, **options):
		self.stdout.write("Doing All The Things!")
