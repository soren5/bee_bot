from slack import WebClient
import secret
import json
import sys
import schedule
import time

NAME = "Pink Bee"
CHANNEL = "#misc"
FILE_PATH = ""

class Bee:
    """Constructs the onboarding message and stores the state of which tasks were completed."""
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, report, up_date):
        self.channel = CHANNEL
        self.username = NAME 
        self.timestamp = ""
        self.up_date = up_date
        self.report = report

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "blocks": [
                self.DIVIDER_BLOCK,
                *self._get_introduction_block(),
                *self._get_timestamp_block(),
                *self._get_report_block(),
                self.DIVIDER_BLOCK,
            ],
        }

    def _get_introduction_block(self):
        text = (
            "Hello, I am " + self.username)
        return self._get_task_block(text)

    def _get_timestamp_block(self):
        text = ("This report was created at " + str(self.up_date))
        return self._get_task_block(text)

    def _get_report_block(self):
        text = (str(self.report))
        return self._get_task_block(text)


    @staticmethod
    def _get_task_block(text):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
        ]

def send_report():
    client = WebClient(token=secret.bot_token)
    timestamp = ""
    report = ""
    try:
        with open(FILE_PATH, "r") as fp:
            report_dict = json.load(fp)
            timestamp= report_dict[0]
            report = report_dict[1]
    except:
        print(FILE_PATH + " does not exist, sending test report")
        timestamp = 'This is a test timestamp'
        report = 'This is a test report'
    bee = Bee(report, timestamp)

    # Get the onboarding message payload
    message = bee.get_message_payload()

    # Post the onboarding message in Slack
    response = client.chat_postMessage(**message)

    # Capture the timestamp of the message we've just posted so
    # we can use it to update the message after a umeser
    # has completed an onboarding task.
    bee.timestamp = response["ts"]
    assert response["ok"]

if __name__ == "__main__": 
    #send_test_report()
    FILE_PATH = sys.argv[1]
    send_report()
    schedule.every().hour.do(send_report)
    while True:
        schedule.run_pending()
        time.sleep(60)
