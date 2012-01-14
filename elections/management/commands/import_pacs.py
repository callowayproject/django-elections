import time
import datetime
import hashlib

from django.core.management.base import LabelCommand, CommandError
from elections.models import Candidate, PACContribution

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports PAC contributions'

    def handle_label(self, label, **options):
        import csv
        bios = csv.reader(open(label, 'rb'), delimiter='|')
        for row in bios:
            row[4] = int(row[4]) #politician id
            try:
                row[7] = int(row[7])
            except ValueError:
                row[7] = None
            row[17] = datetime.datetime.strptime(row[17], "%Y-%m-%d").date()
            try:
                row[18] = int(row[18])
            except ValueError:
                row[18] = 0
            checksum = hashlib.md5()
            
            for i, item in enumerate(row[:-1]):
                if i in (10, 11, 12):
                    continue
                elif i == 4 and item == 0:
                    checksum.update('')
                elif item:
                    checksum.update(str(item))
                else:
                    checksum.update('')
            try:
                try:
                    candidate = Candidate.objects.get(politician_id=row[4])
                except Candidate.DoesNotExist:
                    candidate = None
                
                contribution = PACContribution.objects.get(fec_record_number=row[0])
                if contribution.checksum != checksum.hexdigest():
                    contribution.fec_record_number = row[0]
                    contribution.fec_pac_id = row[1]
                    contribution.pac_name = row[2]
                    contribution.recipient_committee = row[3]
                    contribution.candidate = candidate
                    contribution.office_id = row[5]
                    contribution.state = row[6]
                    contribution.district_number = row[7]
                    contribution.party_id = row[8]
                    contribution.fec_candidate_id = row[9]
                    contribution.office = row[13]
                    contribution.state_name = row[14]
                    contribution.district_name = row[15]
                    contribution.party_name = row[16]
                    contribution.date_given = row[17]
                    contribution.amount = row[18]
                    print 'Updating %s' % row[0]
                    contribution.save()
                else:
                    print "Skipping %s. No change." % row[0]
            except PACContribution.DoesNotExist:
                print 'Adding %s' % row[0]
                contribution = PACContribution()
                contribution.fec_record_number = row[0]
                contribution.fec_pac_id = row[1]
                contribution.pac_name = row[2]
                contribution.recipient_committee = row[3]
                contribution.candidate = candidate
                contribution.office_id = row[5]
                contribution.state = row[6]
                contribution.district_number = row[7]
                contribution.party_id = row[8]
                contribution.fec_candidate_id = row[9]
                contribution.office = row[13]
                contribution.state_name = row[14]
                contribution.district_name = row[15]
                contribution.party_name = row[16]
                contribution.date_given = row[17]
                contribution.amount = row[18]
                contribution.save()