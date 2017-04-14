import os
import upload
import json
import sys
from Qiniu import Qiniu
from teambition import Teambition


# 查文件列表
def findFileList(dp, suffix):
    apks = []
    tt = os.walk(dp);
    for l in tt:
        for ll in l[2]:
            if (ll.endswith(suffix)):
                apks.append(l[0] + "\\" + ll)
                print("文件的路径是：", l[0] + "\\" + ll)
        break
    return apks


# 查修改时间和大小
def findFileTime(apks):
    fileInfo = []
    for apk in apks:
        fileInfo.append((os.path.getsize(apk), os.path.getmtime(apk)))
    return fileInfo


# 查找最新的文件
def findLatestFileIndex(fileInfo):
    maxIndex = 0
    latestTime = 0
    for index in range(len(fileInfo)):
        if (latestTime <= fileInfo[index][1]):
            maxIndex = index
            latestTime = fileInfo[index][1]
    return maxIndex


# 读取配置
def readConfig():
    f = open("config.json", encoding='utf-8')
    config = json.load(f)
    print(config)
    return config


def main():
    # 读取配置
    config = readConfig()
    # 找到所有满足条件的文件
    files = findFileList(config.get("fileDir"), config.get("acceptFile"))
    # 查找文件信息
    fileInfo = findFileTime(files)
    # 最新文件index
    index = findLatestFileIndex(fileInfo)
    # 上传获得七牛Key
    qiniu = Qiniu(config.get("access_key"), config.get("secret_key"), config.get("bucket_name"))
    key = upload.upload(files[index], qiniu)
    link = config.get("qiniuBaseUrl") + key
    print(link)
    data = ''
    # 获取表格
    teambition = Teambition(config.get("cookies"), config.get("getUrl"), config.get("postId"))
    content = teambition.get()
    # 在表格最后一行加入一行数据
    print(content)
    firstHalfTable = content.split('</tbody>', 1)[0]
    secondHalfTable = content.split('</tbody>', 1)[1]
    type = sys.argv[1]
    print(type)
    testModule = ' <tr><td><a href="%s" target="_blank">%s</a></td><td><br/></td></tr></tbody>'
    releaseModule = ' <tr><td><br/></td><td><a href="%s" target="_blank">%s</a></td></tr></tbody>'
    print(sys.argv[2])
    firstHalfTable = firstHalfTable + (releaseModule if type == "release" else testModule) % (link, sys.argv[2])
    data = firstHalfTable + secondHalfTable
    print(data)
    # 更新teambition
    teambition.update(data)


main()
