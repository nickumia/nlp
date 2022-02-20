
import boto3
import pickle


class LocalStorage():
    def __init__(self):
        self.save = None

    def restore(self, filename):
        '''
        IN: filename, str: File that has stored state of dictionary
        '''
        with open(filename, 'rb') as intar:
            self.save = pickle.load(intar)

    def backup(self, filename):
        '''
        IN: filename, str: File to store dictionary in
        '''
        with open(filename, 'wb') as outar:
            pickle.dump(self.save, outar, protocol=pickle.HIGHEST_PROTOCOL)


class S3Storage():
    def __init__(self, bucket_name, cred_profile):
        self.bucket_name = bucket_name
        self.session = boto3.session.Session(
            profile_name=cred_profile).client('s3')
        self.save = None
        self.temp_file = '/tmp/nlp_dev_dictionary'

    def restore(self, filename):
        '''
        Retrieve pickled var as file from s3 bucket
        '''
        with open(self.temp_file, 'wb') as tempfile:
            self.session.download_fileobj(self.bucket_name, filename, tempfile)
        with open(self.temp_file, 'rb') as tempfile:
            self.save = pickle.loads(tempfile.read())

    def backup(self, filename):
        '''
        Upload pickled var as file to s3 bucket
        '''
        with open(self.temp_file, 'wb') as tempfile:
            pickle.dump(self.save, tempfile, protocol=pickle.HIGHEST_PROTOCOL)
        with open(self.temp_file, 'rb') as tempfile:
            self.session.upload_fileobj(tempfile, self.bucket_name, filename)
