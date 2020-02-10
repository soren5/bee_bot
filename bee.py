from slack import WebClient
import secret
import json
import sys
import schedule
import time

NAME = "Pink Bee"
CHANNEL = "#misc"
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
                *self._get_introduction_block(),
                *self._get_timestamp_block(),
                self.DIVIDER_BLOCK,
                *self._get_report_block(),
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
    with open("report.json", "r") as fp:
        report_dict = json.load(fp)
        timestamp= report_dict[0]
        report = report_dict[1]
    print(timestamp)
    print(report)
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
    #schedule.every().day.at("08:00").do(send_report)
    """
    schedule.every(1).minutes.do(send_report)
    while True:
        schedule.run_pending()
        time.sleep(1)
    """
    send_report()