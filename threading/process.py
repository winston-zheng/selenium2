# -*- coding: UTF-8 -*-
from time import sleep,ctime
import multiprocessing

#创建超级播放器
def super_player(file_,time):
    for i in range(2):
        print ('Start playing: %s! %s' %(file_,ctime()))
        sleep(time)

#播放文件与播放时长
lists = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []
files = range(len(lists))

#创建线程
for file_,time in lists.items():   #返回可遍历的(键, 值) 元组数组。
    t = multiprocessing.Process(target=super_player,args=(file_,time))
    threads.append(t)

if __name__ == '__main__':
    #启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

print ('end: %s' %ctime() )
