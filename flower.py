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

def get_time_left_message(current_iteration, max_iteration, start_time):
    progress_percentage = float(current_iteration + 1) / float(max_iteration) 
    elapsed_time = time.time() - start_time
    time_estimate = elapsed_time / progress_percentage
    hours_left = int(time_estimate / 60 / 60)
    minutes_left = int(time_estimate % 60)
    seconds_left = int(time_estimate / 60 % 60)
    return str(hours_left) + ':' + str(minutes_left) + ':' + str(seconds_left)
#create_report("test.json", 'reports/', ["This is an example report"], ["this is additional hidden information"])
