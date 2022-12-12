# !!! PLEASE READ THE README FILE IN ROOT DIRECTORY BEFORE RUNNING !!!

# This program is designed to compare the top 3 most resource intensive processes
# by utilizing the psutil library. This program will parse all the running processes
# on the current system and sort them from least virtual memory used to most 
# virtual memory used. The program will then append the top 3 most resource intensive 
# processes includeing: Process name, PID, Virtual memory used, and the current OS.
# the program will then write this data to a .csv file to compare with other systems.
# After that the program will also create a bar plot using matplotlib library 
# to analyze data even further. 

# Written by Justin Schadwill


import psutil
import os
import csv
import matplotlib.pyplot as plt

def getListOfProcessSortedByMemory():
    #Get list of running process sorted by Memory Usage

    proc_objects_list = []
    system = os.uname()[0]
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           #print('\nVMS: ', pinfo['vms'])
           # Append dict to list
           proc_objects_list.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    proc_objects_list = sorted(proc_objects_list, key=lambda procObj: procObj['vms'])
    return proc_objects_list

data = getListOfProcessSortedByMemory()[-3:][0]['name'] + str(getListOfProcessSortedByMemory()[-3:][0]['pid']) + str(getListOfProcessSortedByMemory()[-3:][0]['vms']) + os.uname()[0]

# Create csv writer and write to csv file
fields = ['Process name', 'PID', 'Rescources used', 'Operating system']
#rows = data
rows = [
        [getListOfProcessSortedByMemory()[-3:][0]['name'],
        getListOfProcessSortedByMemory()[-3:][0]['pid'],
        getListOfProcessSortedByMemory()[-3:][0]['vms'],
        os.uname()[0]],

        [getListOfProcessSortedByMemory()[-3:][1]['name'],
        getListOfProcessSortedByMemory()[-3:][1]['pid'],
        getListOfProcessSortedByMemory()[-3:][1]['vms'],
        os.uname()[0]],

        [getListOfProcessSortedByMemory()[-3:][2]['name'],
        getListOfProcessSortedByMemory()[-3:][2]['pid'],
        getListOfProcessSortedByMemory()[-3:][2]['vms'],
        os.uname()[0]],
        ]

print(fields)
print(rows)
# Write to csv file
filename = 'most_resource_intensive.csv'
with open('most_resource_intensive.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# DEBUG
#print(getListOfProcessSortedByMemory()[-3:][0]['name'])

# Create bar plot comparing virtual memory
names = [
        getListOfProcessSortedByMemory()[-3:][0]['name'], 
        getListOfProcessSortedByMemory()[-3:][1]['name'], 
        getListOfProcessSortedByMemory()[-3:][2]['name'],
        ]
values = [
        getListOfProcessSortedByMemory()[-3:][0]['vms'], 
        getListOfProcessSortedByMemory()[-3:][1]['vms'], 
        getListOfProcessSortedByMemory()[-3:][2]['vms'],
        ]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.show()




