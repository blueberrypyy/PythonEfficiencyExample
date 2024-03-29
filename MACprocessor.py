# !!! PLEASE READ THE README FILE IN ROOT DIRECTORY BEFORE RUNNING !!!

# This program will take a set of data in JSON format as if it were a RESTful API
# request, and process the MAC addresses and determine if each MAC address is either
# 'online' or 'offline'. The program will then tally up the number of online dvices
# vs. the number of offline devices and return the results after the processes ar complete
#The goal of this program is to minimize runtime, minimize resource usage, and generalize 
#the methods and processes.
 

# Written by Justin Schadwill


from multiprocessing import Process, Queue
import multiprocessing
import json

print('\nCPU count:', multiprocessing.cpu_count(), '\n')

rest_api_request = [
        {'main':{
            'MAC': '58:DE:7F:6A:18:8B',
            'status': 'online', 
            }},
        {'main':{
            'MAC': 'DE:A5:7D:4B:21:47',
            'status': 'offline', 
            }},
        {'main':{
            'MAC': '9B:26:2C:D6:63:63',
            'status': 'offline', 
            }},
        {'main':{
            'MAC': '66:BB:B1:9B:30:0D',
            'status': 'online', 
            }},
        {'main':{
            'MAC': 'F0:4B:30:08:8B:AB',
            'status': 'online', 
            }},
        {'main':{
            'MAC': '44:59:9B:EB:35:6D',
            'status': 'online', 
            }},
        {'main':{
            'MAC': 'E6:47:77:98:85:E9',
            'status': 'offline', 
            }},
        {'main':{
            'MAC': 'C1:77:CA:6A:18:8B',
            'status': 'online', 
            }},
        ]


def parse_data(data, queue):
    # Parse the data to determine the number of 'online' and 'offline' items
    online_count = 0
    offline_count = 0
    for item in data:
        if item['main']['status'] == 'online':
            online_count += 1
        elif item['main']['status'] == 'offline':
            offline_count += 1
    # Put the results in the queue
    queue.put((online_count, offline_count))

# Create the queue
queue = Queue()

# Split the data into chunks
chunk_size = 2
num_chunks = len(rest_api_request) // chunk_size
data_chunks = [rest_api_request[i * chunk_size:(i + 1) * chunk_size] for i in range(num_chunks)]

# Create a process for each chunk of data
processes = []
for chunk in data_chunks:
    p = Process(target=parse_data, args=(chunk, queue))
    processes.append(p)
    p.start()

# Wait for all processes to finish
for p in processes:
    p.join()

# Get the results from the queue
results = []
while not queue.empty():
    results.append(queue.get())

# Print the number of 'online' and 'offline' items
online_count = sum([r[0] for r in results])
offline_count = sum([r[1] for r in results])
print(f"Number of online Devices: {online_count}")
print(f"Number of offline Devices: {offline_count}")


