import os
import upload
import teambition


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
        print(os.path.getsize(apk))
        print(os.path.getmtime(apk))
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


def main():
    # 找到所有满足条件的文件
    apks = findFileList('C:\\Users\\Boateng17\\PycharmProjects\\ApplicationRelease', '.py')
    # 查找文件信息
    fileInfo = findFileTime(apks)
    # 最新文件index
    index = findLatestFileIndex(fileInfo)
    # 上传获得七牛Key
    key = upload.upload(apks[index])
    link = "http://oksuo7fcu.bkt.clouddn.com/" + key
    print(link)
    data = ''
    # 获取表格
    content = teambition.get()
    # 在表格最后一行加入一行数据
    print(content)
    firstHalfTable = content.split('</tbody>', 1)[0]
    secondHalfTable = content.split('</tbody>', 1)[1]
    module = '<tr><td>%s</td><td>%s</td></tr></tbody>'

    firstHalfTable = firstHalfTable + module % ('new', link)
    data = firstHalfTable + secondHalfTable
    print(data)
    # 更新teambition
    teambition.update(data)


if __name__ == '__main__':
    main()
