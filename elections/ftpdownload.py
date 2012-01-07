import ftplib
import os


class MaxAttemptsExceeded(Exception):
    pass

class SimpleFTP(object):
    """
    A replacement for ``ftplib.FTP``.
    """
    def __init__(self, host, user='anonymous', passwd=''):
        self.host = host
        self.port = 21
        self.username = user
        self.password = passwd
        self.ftp = None
        self.max_attempts = 3
        self.attempts = 0
        self.connect()
    
    def close(self):
        if self.ftp is not None:
            self.ftp.close()
    
    def connect(self):
        self.close()
        self.ftp = ftplib.FTP()
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.username, self.password)
        self.attempts += 1
    
    def get_file(self, remote_file, local_dir, local_filename=''):
        """
        Fetches a file from the remote server.
        
        local_dir is where to save the file.
        local_filename is the name of the file. An empty string saves it as
            with the same as the remote name
        """
        remote_dirname, remote_filename = os.path.split(remote_file)
        if not local_filename:
            local_filename = remote_filename
        local_path = os.path.abspath(os.path.join(local_dir, local_filename))
        while self.attempts <= self.max_attempts:
            try:
                dest = open(local_path, 'wb')
                self.ftp.retrbinary('RETR %s' % remote_file, dest.write)
            except ftplib.all_errors, e:
                print e
                self.connect()
                continue
            else:
                dest.close()
                return
        # Attempts failed! Remove the empty file and raise an error
        try:
            os.remove(local_path)
        except OSError:
            pass
        raise MaxAttemptsExceeded
