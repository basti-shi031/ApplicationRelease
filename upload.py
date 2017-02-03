from qiniu import Auth, put_file, etag
import qiniu.config


def upload(file):
    access_key = 'pNwdZ3bvSi5QuStSOcx0vnrEBzxgChzp6ARajJlq'
    secret_key = 'nz__MH4jk0B0ZcQSCunbrdj5omJFoRs7ca00GaAz'

    q = Auth(access_key, secret_key)

    bucket_name = 'testbast'

    key = file.split('\\')[-1];
    print(key)

    # 生成token
    token = q.upload_token(bucket_name, key, 3600)
    print(token)

    ret, info = put_file(token, key, file)
    print(info)
    return key
    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
