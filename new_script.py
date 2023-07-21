#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
	data=shutil.disk_usage(disk)
	free=data.free/data.total * 100
	return free > 20
def check_cpu_usage():
	data=psutil.cpu_persent(1)
	return data < 7

if not check_disk_usage("/") and not check_cpu_usage():
	print("Error")
else:
	print("No problem")


