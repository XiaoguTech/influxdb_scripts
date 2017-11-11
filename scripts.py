
import time
import requests

with open('household_power_consumption.txt') as source_file:
    tags = source_file.readline()[:-1].split(';')
    str_format = "house,metric={} value={} {}000000000"

    for line in source_file:
        fields = line[:-1].split(';')
        timestamp = int(time.mktime( time.strptime(fields[0] + ' ' + fields[1], "%d/%m/%Y %H:%M:%S")))
        for index in range(2, len(tags)):
            temp_str = str_format.format(tags[index], fields[index], timestamp)
            print(temp_str)
