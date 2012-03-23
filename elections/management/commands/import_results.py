import time
import datetime
import hashlib

from django.core.management.base import LabelCommand, CommandError


class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports PAC contributions'

    def handle_label(self, label, **options):
        from elections.electionmap import write_results
        
        write_results(label)
