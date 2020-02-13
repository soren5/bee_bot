import pprint
import json
import time

def create_report(report, extra):
    pp = pprint.PrettyPrinter(indent=4)
    message = pp.pformat(report)
    extra = pp.pformat(extra)
    todate = time.localtime()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", todate)
    with open('report.json', 'w') as fp:
        json.dump([timestamp,message,extra], fp)

#create_report(["This is an example report"], ["this is additional hidden information"])