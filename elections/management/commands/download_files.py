from django.core.management.base import NoArgsCommand
import os

class Command(NoArgsCommand):
    """
    Download the files
    """
    def handle_noargs(self, **options):
        """
        Yep, download the files
        """
        from elections.ftpdownload import SimpleFTP
        from elections.settings import (FTP_USER, FTP_PASSWORD, FTP_HOST, 
                                        DOWNLOAD_PATHS, DEST_PATH)
        
        client = SimpleFTP(FTP_HOST, FTP_USER, FTP_PASSWORD)
        
        for path in DOWNLOAD_PATHS:
            dpath = os.path.join(DEST_PATH, path[1:])
            ddir, dfile = os.path.split(dpath)
            if not os.path.exists(ddir):
                try:
                    os.makedirs(ddir)
                except OSError, e:
                    pass
            print "Downloading '%s' to '%s'" % (path, dpath)
            client.get_file(path, DEST_PATH, path[1:])