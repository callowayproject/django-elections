import time
import datetime
import hashlib

from django.core.management.base import LabelCommand, CommandError
from elections.models import ElectionEvent

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports election events'

    def handle_label(self, label, **options):
        import csv
        events = csv.reader(open(label, 'rb'), delimiter='|')
        for row in events:
            row[3] = datetime.datetime.strptime(row[3], "%Y-%m-%d").date()
            checksum = hashlib.md5()
            
            for item in row[:-1]:
                if item:
                    checksum.update(str(item))
                else:
                    checksum.update('')
            try:
                evt = ElectionEvent.objects.get(event_code=row[0])
                if evt.checksum != checksum.hexdigest():
                    evt.state = row[1]
                    evt.state_name = row[2]
                    evt.event_date = row[3]
                    evt.description = row[4]
                    print 'Updating %s' % (" ".join([row[0], row[4],]))
                    evt.save()
                else:
                    print "Skipping %s. No change." % row[0]
            except ElectionEvent.DoesNotExist:
                print 'Adding %s' % (" ".join([row[0], row[4],]))
                evt = ElectionEvent.objects.create(
                    event_code=row[0], 
                    state=row[1],
                    state_name=row[2],
                    event_date=row[3],
                    description = row[4]
                )
                evt.save()