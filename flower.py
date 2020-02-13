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

#create_report("test.json", 'reports/', ["This is an example report"], ["this is additional hidden information"])
