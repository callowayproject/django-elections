import os
from PIL import Image

from django.core.management.base import LabelCommand
from django.core.files import File

from elections.models import Candidate
from elections.ftpdownload import SimpleFTP
from elections.settings import (FTP_USER, FTP_PASSWORD, FTP_HOST, DEST_PATH)

class Command(LabelCommand):
    args = '[file1 file2 ...]'
    help = 'Imports media'
    ftp_path = "/PreElection_Content/images/bios/"

    def get_file(self, path):
        dpath = os.path.join(DEST_PATH, path[1:])
        ddir, dfile = os.path.split(dpath)
        if not os.path.exists(ddir):
            try:
                os.makedirs(ddir)
            except OSError:
                pass
        print "Downloading '%s' to '%s'" % (path, dpath)
        client = SimpleFTP(FTP_HOST, FTP_USER, FTP_PASSWORD)
        client.get_file(path, DEST_PATH, path[1:])
        return dpath

    def handle_label(self, label, **options):
        import csv
        bios = csv.reader(open(label, 'rb'), delimiter='|')
        for row in bios:
            row[0] = int(row[0]) #politician id
            filename = "%s.%s" % (row[2], row[3])
            filepath = os.path.join(self.ftp_path, filename)
            candidate, created = Candidate.objects.get_or_create(politician_id=row[0])
            if created:
                print "Had to create the candidate"
            
            if "small" in filename and not candidate.thumbnail:
                print 'Downloading thumbnail for %s' % candidate
                dest_path = self.get_file(filepath)
                
                try:
                    img = Image.open(dest_path)
                    width, height = img.size
                    candidate.thumbnail.save(filename, File(open(dest_path, 'rb')), save=True)
                    candidate.thumbnail_width = width
                    candidate.thumbnail_height = height
                    candidate.save()
                except Exception, e:
                    print e
                    raise
            elif not candidate.photo:
                print 'Downloading photo for %s' % candidate
                dest_path = self.get_file(filepath)
                try:
                    img = Image.open(dest_path)
                    width, height = img.size
                    candidate.photo.save(filename, File(open(dest_path, 'rb')), save=True)
                    candidate.photo_width = width
                    candidate.photo_height = height
                    candidate.save()
                except Exception, e:
                    print e
                    raise
