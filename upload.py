from qiniu import Auth, put_file, etag


def upload(file, qiniu):
    access_key = qiniu.access_key
    secret_key = qiniu.secret_key

    q = Auth(access_key, secret_key)

    # bucket_name = 'testbast'
    bucket_name = qiniu.bucket_name

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
