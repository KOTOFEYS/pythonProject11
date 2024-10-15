import time
from threading import Thread
from datetime import datetime

start_time_funk = datetime.now()

def write_words(word_count, file_name):

    with open(file_name,'w', encoding='utf-8') as file:
        for i in range(1, 1 + word_count):
            time.sleep(0.1)
            file.write(f'Какое-то слово №{i}\n')
        print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time_funk = datetime.now()
diff_time_funk = end_time_funk - start_time_funk
print(diff_time_funk)

start_time_thr = datetime.now()

thr_fist = Thread(target=write_words, args=(10,'example5.txt'))
thr_second = Thread(target=write_words, args=(30,'example6.txt'))
thr_third = Thread(target=write_words, args=(200,'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100,'example8.txt'))

thr_fist.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_fist.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

end_time_thr = datetime.now()
diff_time_thr = end_time_thr - start_time_thr
print(diff_time_thr)


