#!/usr/bin/python3

import psutil
import os

# Retrieve CPU times
cpu_times = psutil.cpu_times()

# Access individual fields
user_time = cpu_times.user
system_time = cpu_times.system
idle_time = cpu_times.idle
iowait = cpu_times.iowait
sysinfo = os.uname()
# Access Disk info
disk_stat = psutil.disk_partitions()
#device = disk_stat.device
#fstype = disk_stat.fstype

# Print os name

print(f"OS: {sysinfo.sysname}")
# Print the values
print("_______CPU STAT________")
print(f"User time: {user_time}")
print(f"System time: {system_time}")
print(f"Idle time: {idle_time}")
print(f"iowait: {iowait}")
print("_______________________")
print("______DISK STAT_______")
#print(f"Device: {device}")
#print(f"Filesystem: {fstype}")
for disk in disk_stat:
    print(f"Disk: {disk.device}")
    print(f"FS: {disk.fstype}")
    print(f"MountPoint: {disk.mountpoint}")
    print("------------------------")
   
