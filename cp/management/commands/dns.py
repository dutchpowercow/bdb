from django.core.management.base import BaseCommand, CommandError
#from cp.models import Question as Poll
import argparse


class Command(BaseCommand):
    help = 'DNS'
    args = []

    def add_arguments(self, parser):
        parser.add_argument('-c', '--string', type=str, required=True)
        #self.args = parser.parse_args()
        #print(self.args.accumulate(args.integers))
        ## werkt nog niet
        self.args = ['234', "asdf"]

    def handle(self, *args, **options):
            self.stdout.write(self.style.SUCCESS('DNS stuff ' + str.join(",", self.args)))
