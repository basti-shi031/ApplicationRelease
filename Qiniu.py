class Qiniu(object):
    def __init__(self, access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
