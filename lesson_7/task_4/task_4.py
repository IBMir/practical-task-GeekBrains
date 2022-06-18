import os


def file_sizes(directory):
    folder_statistics = {
        100: 0,
        1000: 0,
        10000: 0,
        100000: 0
    }
    for dirpath, dirnames, filenames in os.walk(directory):
        for i in filenames:
            file_information = os.stat(f'{dirpath}\\{i}').st_size
            if 0 <= file_information <= 100:
                folder_statistics[100] += 1
            elif 100 < file_information <= 1000:
                folder_statistics[1000] += 1
            elif 1000 < file_information <= 10000:
                folder_statistics[10000] += 1
            elif 10000 < file_information <= 100000:
                folder_statistics[100000] += 1
    return folder_statistics

if __name__ == '__main__':
    print(file_sizes(r'directory'))

