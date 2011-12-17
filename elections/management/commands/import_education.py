import time
import datetime
import hashlib

from django.core.management.base import LabelCommand, CommandError
from elections.models import Candidate, CandidateEducation

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports candidate education'

    def handle_label(self, label, **options):
        import csv
        bios = csv.reader(open(label, 'rb'), delimiter='|')
        for row in bios:
            row[0] = int(row[0]) #politician id
            row[1] = row[1].replace('<p>', '').replace('</p>', '')
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
                education = candidate.education.get(school_name=row[1], school_type=row[2], degree=row[4])
                if education.checksum != checksum.hexdigest():
                    education.school_name = row[1]
                    education.school_type = row[2]
                    education.major = row[3]
                    education.degree = row[4]
                    education.school_city = row[5]
                    education.school_state = row[6]
                    education.school_province = row[7]
                    education.school_country = row[8]
                    print 'Updating %s %s' % (row[1], row[4])
                    education.save()
                else:
                    print "Skipping %s %s. No change." % (row[1], row[4])
                    
            except CandidateEducation.DoesNotExist:
                print 'Adding %s %s' % (row[1], row[4])
                education = candidate.education.create()
                education.school_name = row[1]
                education.school_type = row[2]
                education.major = row[3]
                education.degree = row[4]
                education.school_city = row[5]
                education.school_state = row[6]
                education.school_province = row[7]
                education.school_country = row[8]
                education.save()