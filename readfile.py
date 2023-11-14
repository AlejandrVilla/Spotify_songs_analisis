import csv

def read_data(path):
    data = []
    # utf-8 prevents an error
    with open(path, "r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            song_dict = {key:value for key,value in iterable}
            data.append(song_dict)
    # print(len(data), "datos")
    return data