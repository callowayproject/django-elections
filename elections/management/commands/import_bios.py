import time
import datetime

from django.core.management.base import LabelCommand, CommandError
from elections.models import Candidate

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports candidate biographies'

    def handle_label(self, label, **options):
        import csv
        bios = csv.reader(open(label, 'rb'), delimiter='|')
        for row in bios:
            row[0] = int(row[0]) #politician id
            if row[5]:
                row[5] = int(row[5]) #year first elected
            else:
                row[5] = None
            row[20] = datetime.datetime(*time.strptime(row[20], "%m-%d-%Y %I:%M:%S %p")[:6]) # timestamp
            row[13] = row[13][0] # gender
            if row[6]:
                row[6] = datetime.date(*time.strptime(row[6], "%Y-%m-%d")[:3]) # birthdate
            else:
                row[6] = None
            try:
                candidate = Candidate.objects.get(politician_id=row[0])
                if candidate.timestamp != row[20]:
                    candidate.first_name = row[1]
                    candidate.middle_name = row[2]
                    candidate.last_name = row[3]
                    candidate.junior = row[4]
                    candidate.year_first_elected = row[5]
                    candidate.birth_date = row[6]
                    candidate.birth_place = row[7]
                    candidate.birth_state = row[8]
                    candidate.birth_province = row[9]
                    candidate.birth_country = row[10]
                    candidate.residence_place = row[11]
                    candidate.residence_state = row[12]
                    candidate.gender = row[13]
                    candidate.ethnicity = row[14]
                    candidate.hispanic = row[15]
                    candidate.religion = row[16]
                    candidate.biography = row[17]
                    candidate.profile = row[18]
                    candidate.campaigns = row[19]
                    candidate.timestamp = row[20]
                    print 'Updating %s %s' % (row[1], row[3])
                    candidate.save()
                else:
                    print "Skipping %s %s. No change." % (row[1], row[3])
                    
            except Candidate.DoesNotExist:
                print 'Adding %s %s' % (row[1], row[3])
                candidate = Candidate()
                candidate.politician_id = row[0]
                candidate.ap_candidate_id = row[0]
                candidate.candidate_number = row[0]
                candidate.first_name = row[1]
                candidate.middle_name = row[2]
                candidate.last_name = row[3]
                candidate.junior = row[4]
                candidate.year_first_elected = row[5]
                candidate.birth_date = row[6]
                candidate.birth_place = row[7]
                candidate.birth_state = row[8]
                candidate.birth_province = row[9]
                candidate.birth_country = row[10]
                candidate.residence_place = row[11]
                candidate.residence_state = row[12]
                candidate.gender = row[13]
                candidate.ethnicity = row[14]
                candidate.hispanic = row[15]
                candidate.religion = row[16]
                candidate.biography = row[17]
                candidate.profile = row[18]
                candidate.campaigns = row[19]
                candidate.timestamp = row[20]
                
                candidate.save()