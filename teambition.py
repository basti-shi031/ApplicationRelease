import requests
import json

# c = 'gr_user_id=66307169-c8ab-4bb6-84cc-23d30e171f42;' \
#     ' mp_a0378064615fc4a8c3dc1bca7a821e4c_mixpanel=%7B%22distinct_id%22%3A%20%' \
#     '2215640b2a4ab7b-01d1f7a6427015-404c0128-1fa400-15640b2a4ac24c%22%2C%22%24os_v' \
#     'ersion%22%3A%20%22Windows%20NT%206.3%22%2C%22%24initial_referrer%22%3A%20%22%24d' \
#     'irect%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; fs_uid=www.fu' \
#     'llstory.com`M776`5631537083056128:5629499534213120`576d295c1006b9cc63438ddf`false; mp' \
#     '_50a734e210e0719fb5a5c36da6c26e03_mixpanel=%7B%22distinct_id%22%3A%20%22157830e028c320-0' \
#     '512409ae7f03b-4045002a-1fa400-157830e028d214%22%2C%22%24os_version%22%3A%20%22Windows%20N' \
#     'T%206.3%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.teambition.com%2F%22%2C' \
#     '%22%24initial_referring_domain%22%3A%20%22www.teambition.com%22%7D; TEAMBITION_SESSIONID=' \
#     'eyJhdXRoVXBkYXRlZCI6MTQ2Njc3OTA1MTczNywidHMiOjE0ODU1NzMxNzM2NjksInVpZCI6IjU3NmQyOTVjMTAwNmI' \
#     '5Y2M2MzQzOGRkZiIsInVzZXIiOnsiYXZhdGFyVXJsIjoiaHR0cHM6Ly9zdHJpa2VyLnRlYW1iaXRpb24ubmV0L3RodW' \
#     '1ibmFpbC8xMTBpYzc4MzQ3ZmU3MDM1ODVmYWMwOWM1MDUwOTM4NzBiY2Mvdy8xMDAvaC8xMDAiLCJuYW1lIjoi5pa95Y2a5' \
#     'paHIiwiZW1haWwiOiI4NzY1NzIwNzhAcXEuY29tIiwiX2lkIjoiNTc2ZDI5NWMxMDA2YjljYzYzNDM4ZGRmIiwiaXNOZXc' \
#     'iOnRydWUsInJlZ2lvbiI6ImNuIn19; TEAMBITION_SESSIONID.sig=m8lUpel7kYzIxkl203L1N2HmAqQ; _ga=GA1.2.4603' \
#     '83935.1469964265; Hm_lvt_ec912ecc405ccd050e4cdf452ef4e85a=1483862482,1484835493,1485573182,148612605' \
#     '6; Hm_lpvt_ec912ecc405ccd050e4cdf452ef4e85a=1486126056; lang=zh; _cioid=876572078@qq.com; _cio=1c2569' \
#     'a1-907e-f881-7eee-2696bd0ef54d; _gat=1; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%2' \
#     '215640b2dde52d8-0637989f984275-404c0128-1fa400-15640b2dde6114%22%2C%22%24os_version%22%3A%20%22Windows%20NT%2' \
#     '06.3%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Faccount.teambition.com%2Flogin%22%2C%22%24initial' \
#     '_referring_domain%22%3A%20%22account.teambition.com%22%2C%22userKey%22%3A%20%22576d295c1006b9cc63438ddf%2' \
#     '2%2C%22created_at%22%3A%20%222016-06-24T12%3A36%3A44.800Z%22%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%2' \
#     '2%3A%20%22release%22%2C%22version%22%3A%20%227.23.0%22%2C%22daysSinceRegistered%22%3A%20225%2C%22timezone%22%3' \
#     'A%208%2C%22city%22%3A%20%22Suzhou%22%2C%22country%22%3A%20%22China%22%2C%22region%22%3A%20%22Jiangsu%22%2C%22org_' \
#     'subscription%22%3A%20true%2C%22experiments%22%3A%20%5B%0A%20%20%20%20%22all_sharelink.A%22%2C%0A%20%20%20%20%22a' \
#     'll_startbutton.C%22%2C%0A%20%20%20%20%22gantt_cohort_timeline.B%22%0A%5D%7D; mp_tbpanel__c=1'

c = 'gr_user_id=66307169-c8ab-4bb6-84cc-23d30e171f42; mp_a0378064615fc4a8c3dc1bca7a821e4c_mixpanel=%7B%22distinct_id%22%3A%20%2215640b2a4ab7b-01d1f7a6427015-404c0128-1fa400-15640b2a4ac24c%22%2C%22%24os_version%22%3A%20%22Windows%20NT%206.3%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; fs_uid=www.fullstory.com`M776`5631537083056128:5629499534213120`576d295c1006b9cc63438ddf`false; mp_50a734e210e0719fb5a5c36da6c26e03_mixpanel=%7B%22distinct_id%22%3A%20%22157830e028c320-0512409ae7f03b-4045002a-1fa400-157830e028d214%22%2C%22%24os_version%22%3A%20%22Windows%20NT%206.3%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.teambition.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.teambition.com%22%7D; _cioid=876572078@qq.com; _cio=1c2569a1-907e-f881-7eee-2696bd0ef54d; TEAMBITION_SESSIONID=eyJhdXRoVXBkYXRlZCI6MTQ2Njc3OTA1MTczNywidHMiOjE0ODYxMzEyMTUxNDMsInVpZCI6IjU3NmQyOTVjMTAwNmI5Y2M2MzQzOGRkZiIsInVzZXIiOnsiYXZhdGFyVXJsIjoiaHR0cHM6Ly9zdHJpa2VyLnRlYW1iaXRpb24ubmV0L3RodW1ibmFpbC8xMTBpYzc4MzQ3ZmU3MDM1ODVmYWMwOWM1MDUwOTM4NzBiY2Mvdy8xMDAvaC8xMDAiLCJuYW1lIjoi5pa95Y2a5paHIiwiZW1haWwiOiI4NzY1NzIwNzhAcXEuY29tIiwiX2lkIjoiNTc2ZDI5NWMxMDA2YjljYzYzNDM4ZGRmIiwiaXNOZXciOnRydWUsInJlZ2lvbiI6ImNuIn19; TEAMBITION_SESSIONID.sig=cZjj6ExpsgN7wsEwP7roFyCyD_M; _gat=1; _ga=GA1.2.460383935.1469964265; Hm_lvt_ec912ecc405ccd050e4cdf452ef4e85a=1484835493,1485573182,1486126056,1486130442; Hm_lpvt_ec912ecc405ccd050e4cdf452ef4e85a=1486133237; lang=zh; mp_eSpCz4lYpMYgtuhdH0F6Wgtt_mixpanel=%7B%22distinct_id%22%3A%20%2215640b2dde52d8-0637989f984275-404c0128-1fa400-15640b2dde6114%22%2C%22%24os_version%22%3A%20%22Windows%20NT%206.3%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Faccount.teambition.com%2Flogin%22%2C%22%24initial_referring_domain%22%3A%20%22account.teambition.com%22%2C%22userKey%22%3A%20%22576d295c1006b9cc63438ddf%22%2C%22created_at%22%3A%20%222016-06-24T12%3A36%3A44.800Z%22%2C%22userLanguage%22%3A%20%22zh%22%2C%22env%22%3A%20%22release%22%2C%22version%22%3A%20%227.23.0%22%2C%22daysSinceRegistered%22%3A%20225%2C%22timezone%22%3A%208%2C%22city%22%3A%20%22Suzhou%22%2C%22country%22%3A%20%22China%22%2C%22region%22%3A%20%22Jiangsu%22%2C%22org_subscription%22%3A%20true%2C%22experiments%22%3A%20%5B%0A%20%20%20%20%22all_sharelink.A%22%2C%0A%20%20%20%20%22all_startbutton.C%22%2C%0A%20%20%20%20%22gantt_cohort_timeline.B%22%0A%5D%7D; _gali=589489295e96d2384fc41f00; mp_tbpanel__c=1'

cookies = {}  # 初始化cookies字典变量
for line in c.split(';'):  # 按照字符：进行划分读取
    # 其设置为1就会把字符串拆分成2份
    name, value = line.strip().split('=', 1)
    cookies[name] = value  # 为字典cookies添加内容


def update(data):
    headers = {'content-type': 'application/json'}
    payload = {'content': data}
    response = requests.put(url='https://www.teambition.com/api/posts/589489295e96d2384fc41f00',
                            data=json.dumps(payload), headers=headers, cookies=cookies)
    print(response.text)


def get():
    headers = {
        'upgrade - insecure - requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'}
    response = requests.get(
        'https://www.teambition.com/api/posts/589489295e96d2384fc41f00/activities?_postId=589489295e96d2384fc41f00&_=1486136195044',
        headers=headers,
        cookies=cookies)
    latestResponse = response.json()[0]
    content = latestResponse.get('content').get('content')
    return content
