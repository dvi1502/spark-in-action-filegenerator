import logging
import logging.config
import os


from datetime import datetime
from time import sleep
from call import PhoneCallBuilder
from call import PhoneCall

from arguments import args_reader as args_reader

# настраиваем журналирование
logging.basicConfig(
    level=logging.DEBUG,
    filename="/tmp/{0}.log".format(__name__),
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)
# logging.config.fileConfig("logconf.ini")


def makedir(npath):
    if not os.path.exists(npath):
        os.makedirs(npath)
    else:
        pass
        # for f in os.listdir(npath):
        #     os.remove(os.path.join(npath, f))

def get_random_time(args):
    """
    тут возвращается генератор с последовательностью случайных задержек
    :param args: dict input arguments
    :return: generator
    """
    from random import randrange
    i = int(args.wait_time + args.wait_time / 2)
    # return randrange(i);
    return (randrange(i) for _ in range(args.duration * 10000))

def stop_time(args):
    """
    :param args: dict input arguments
    :return: значение последнего временного отсчета в текущем цикле
    """
    return datetime.now().microsecond + args.duration * 1000


def start(args) :

    log = logging.getLogger(__name__)

    start_time_ms = datetime.now().microsecond
    stop_time_ms = stop_time(args)

    log.debug("{0} ms --> {1} ms".format(start_time_ms,stop_time_ms))

    while ( datetime.now().microsecond < stop_time_ms ):
        delay = next(get_random_time(args))
        filename = "{0}/{1}_{2}.txt".format(args.pathout,"jazz",datetime.now().microsecond)
        log.debug("[{0}  -  {1} sec]  {2}".format(datetime.now(), delay, filename))

        with open(filename,"w") as rs:
            call = next(PhoneCallBuilder(args))
            rs.write(call.json())

        sleep(delay)



if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.info("Application start ...")
    args = args_reader()
    makedir(args.pathout)
    start(args)
    log.info("Application terminate ...")

