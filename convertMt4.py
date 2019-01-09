# !/usr/bin/python
# coding=utf-8

print "转换开始";

# <TICKER>,<DTYYYYMMDD>,<TIME>,<OPEN>,  <HIGH>, <LOW>, <CLOSE>,<VOL>
# EURUSD,   20010102,   230100, 0.9507, 0.9507, 0.9507, 0.9507,   4
# EURUSD,   20010102,   230200, 0.9506, 0.9506, 0.9505, 0.9505,   4
openArray = []
hightArray = []
lowArray = []
closeArray = []
# 写文件
f15 = open('/app/test/EURUSD15.txt', 'w')


def isMinute15(day, hour, minute, openValue, hightValue, lowValue, closeValue):
    key15 = day + hour + '15'
    key30 = day + hour + '30'
    key45 = day + hour + '45'
    timeKey = day + hour + minute
    global lastDay
    global lastTime
    if timeKey < key15:
        lastDay = day
        lastTime = hour + '00'
    elif timeKey >= key15 and timeKey < key30:
        lastDay = day
        lastTime = hour + '15'
    elif timeKey >= key30 and timeKey < key45:
        lastDay = day
        lastTime = hour + '30'
    elif timeKey >= key45:
        lastDay = day
        lastTime = hour + '45'
    openArray.append(openValue)
    hightArray.append(hightValue)
    lowArray.append(lowValue)
    closeArray.append(closeValue)


def lineKeyBulid(day, hour, minute):
    key00 = day + hour + '00'
    key15 = day + hour + '15'
    key30 = day + hour + '30'
    key45 = day + hour + '45'
    timeKey = day + hour + minute
    if timeKey < key15:
        return day + hour + '00'
    elif timeKey >= key15 and timeKey < key30:
        return day + hour + '15'
    elif timeKey >= key30 and timeKey < key45:
        return day + hour + '30'
    elif timeKey >= key45:
        return day + hour + '45'


def cleararray():
    global openArray
    global hightArray
    global lowArray
    global closeArray
    openArray = []
    hightArray = []
    lowArray = []
    closeArray = []


# 读取文件
lineKey = ""
mainKey = ""
lastTime = ""
lastDay = ""
i = 1
with open('/app/test/EURUSD.txt', 'r') as f:
    # print f.read()
    for line in f.readlines():
        data = line.strip()
        # print data
        i += 1
        print i
    if data.__contains__('<'):
        f15.write(data + '\n')
    elif len(data):
        dataArray = data.split(',')
        name = dataArray[0]
        day = dataArray[1]
        time = dataArray[2]
        hour = time[0:2]
        minute = time[2:4]
        openValue = dataArray[3]
        hightValue = dataArray[4]
        lowValue = dataArray[5]
        closeValue = dataArray[6]
        four = dataArray[7]
        lineKey = lineKeyBulid(day, hour, minute)

        if mainKey == '':
            isMinute15(day, hour, minute, openValue, hightValue, lowValue, closeValue)
            mainKey = lineKey
        elif mainKey == lineKey:
            isMinute15(day, hour, minute, openValue, hightValue, lowValue, closeValue)
        elif mainKey != lineKey:
            mainKey = ''
            closeLen = len(closeArray)
            writeLine = str(name) + ',' + str(lastDay) + ',' + str(lastTime) + ',' + str(openArray[0]) + ',' + str(
                max(hightArray)) + ',' + str(min(lowArray)) + ',' + str(closeArray[closeLen - 1]) + ',' + "4" + '\n'
            f15.write(writeLine)
            cleararray()
            isMinute15(day, hour, minute, openValue, hightValue, lowValue, closeValue)
    elif not len(data):
        print len(data)
        writeLine = str(name) + ',' + str(lastDay) + ',' + str(lastTime) + ',' + str(openArray[0]) + ',' + str(
            max(hightArray)) + ',' + str(min(lowArray)) + ',' + str(closeArray[closeLen - 1]) + ',' + "4" + '\n'
        f15.write(writeLine)
        cleararray()
        isMinute15(day, hour, minute, openValue, hightValue, lowValue, closeValue)

f15.close()
print "转换结束"
