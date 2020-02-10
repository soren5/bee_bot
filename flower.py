import pprint
import json
import time

def create_report(report):
    pp = pprint.PrettyPrinter(indent=4)
    message = pp.pformat(report)
    todate = time.localtime()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", todate)
    with open('report.json', 'w') as fp:
        json.dump([timestamp,message], fp)

create_report(["as"])