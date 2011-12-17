import time
import datetime
import hashlib

from django.core.management.base import LabelCommand, CommandError
from elections.models import Candidate, CandidateOffice

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports candidate office history'

    def handle_label(self, label, **options):
        import csv
        bios = csv.reader(open(label, 'rb'), delimiter='|')
        for row in bios:
            row[0] = int(row[0]) #politician id
            row[12] = int(row[12])
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
                office = candidate.offices.get(office_id=row[1], state=row[2], district_number=row[3])
                if office.checksum != checksum.hexdigest():
                    office.office_id = row[1]
                    office.state = row[2]
                    office.district_number = row[3]
                    office.party_id = row[4]
                    office.status_id = row[5]
                    office.office = row[6]
                    office.state_name = row[7]
                    office.district_name = row[8]
                    office.party_name = row[9]
                    office.office_description = row[10]
                    office.status_description = row[11]
                    office.next_election = row[12]
                    print 'Updating %s' % (" ".join([row[7], row[6], row[8]]))
                    office.save()
                else:
                    print "Skipping %s. No change." % (" ".join([row[7], row[6], row[8]]))
                    
            except CandidateOffice.DoesNotExist:
                print 'Adding %s' % (" ".join([row[7], row[6], row[8]]))
                office = candidate.offices.create()
                office.office_id = row[1]
                office.state = row[2]
                office.district_number = row[3]
                office.party_id = row[4]
                office.status_id = row[5]
                office.office = row[6]
                office.state_name = row[7]
                office.district_name = row[8]
                office.party_name = row[9]
                office.office_description = row[10]
                office.status_description = row[11]
                office.next_election = row[12]
                office.save()