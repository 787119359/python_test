import threading
import time ,datetime

loops = [4,2]
date_time_format = '%y-%m-%d %H:%M:%S'


def date_time_str(date_time):
    return datetime.datetime.strftime(date_time,date_time_format)


def loop(n_loop,n_sec):
    print(f'线程({n_loop})开始任务:{date_time_str((datetime.datetime.now()))},先休眠({n_sec})秒')
    time.sleep(n_sec)
    print(f'线程({n_loop})休眠结束,结束于:{date_time_str((datetime.datetime.now()))}')


def main():
    print(f'所有线程开始执行:{date_time_str(datetime.datetime.now())}')
    threads = []
    for i in range(len(loops)):
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in  range(len(loops)):
        threads[i].start()

    for i in range(len(loops)):
        threads[i].join()

    print(f'所有线程执行结束:{date_time_str(datetime.datetime.now())}')


if __name__ == '__main__':
    main()