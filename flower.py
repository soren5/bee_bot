import pprint
import json
import time
import os

def create_report(filename, dirname, report, extra):
    pp = pprint.PrettyPrinter(indent=4)
    message = pp.pformat(report)
    extra = pp.pformat(extra)
    todate = time.localtime()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", todate)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(dirname + filename, 'w') as fp:
        json.dump([timestamp, message, extra], fp)

def get_progress_data(current_iteration, max_iteration, start_time):
    progress_data = {}
    progress_percentage = float(current_iteration + 1) / float(max_iteration) 
    time_elapsed = float(time.time() - start_time)
    time_estimate = float(time_elapsed) / progress_percentage
    hours_elapsed = int(time_elapsed / 60 / 60)
    minutes_elapsed = int(time_elapsed % 60)
    seconds_elapsed = int(time_elapsed / 60 % 60)
    hours_left = int(time_estimate / 60 / 60)
    minutes_left = int(time_estimate % 60)
    seconds_left = int(time_estimate / 60 % 60)
    progress_data['progress_percentage'] = str(progress_percentage)
    progress_data['time_elapsed'] = str(hours_elapsed) + ':' + str(minutes_elapsed) + ':' + str(seconds_elapsed)
    progress_data['time_left'] = str(hours_left) + ':' + str(minutes_left) + ':' + str(seconds_left)
    return progress_data
#create_report("test.json", 'reports/', ["This is an example report"], ["this is additional hidden information"])
