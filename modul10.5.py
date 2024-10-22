import multiprocessing
from datetime import datetime

def read_info(name):
    al_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            al_data.append(file.readline())

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # start_time = datetime.now()
    # for filename in filenames:
    #     read_info(filename)
    # end_time = datetime.now()
    # print(end_time - start_time)

    start_time = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(end_time - start_time)
