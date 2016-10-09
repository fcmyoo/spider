from multiprocessing import Pool
from one.teacherCode.channel_extact import channel_list
from one.teacherCode.pages_parsing import get_links_from


def get_all_links_from(channel):
    for i in range(1, 100):
        get_links_from(channel, i)


if __name__ == '__main__':
    pool = Pool()
    # pool = Pool(processes=6)
    pool.map(get_all_links_from, channel_list.split())
