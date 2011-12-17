import time
import datetime
import hashlib

from django.core.management.base import LabelCommand, CommandError
from elections.models import Candidate, CandidatePhone

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports candidate phone numbers'

    def handle_label(self, label, **options):
        import csv
        bios = csv.reader(open(label, 'rb'), delimiter='|')
        for row in bios:
            row[0] = int(row[0]) #politician id
            checksum = hashlib.md5()
            
            for item in row[:-1]:
                if item:
                    checksum.update(str(item))
                else:
                    checksum.update('')
            try:
                candidate, created = Candidate.objects.get_or_create(politician_id=row[0])
                if created:
                    print "Had to create the candidate"
                phone = candidate.phones.get(phone_number=row[1], extension=row[2], detail=row[4])
                if phone.checksum != checksum.hexdigest():
                    phone.phone_number = row[1]
                    phone.extension = row[2]
                    phone.location = row[3]
                    phone.detail = row[4]
                    print 'Updating %s' % (" ".join([row[4], row[1],]))
                    phone.save()
                else:
                    print "Skipping %s. No change." % (" ".join([row[4], row[1],]))
                    
            except CandidatePhone.DoesNotExist:
                print 'Adding %s' % (" ".join([row[4], row[1],]))
                phone = candidate.phones.create()
                phone.phone_number = row[1]
                phone.extension = row[2]
                phone.location = row[3]
                phone.detail = row[4]
                phone.save()