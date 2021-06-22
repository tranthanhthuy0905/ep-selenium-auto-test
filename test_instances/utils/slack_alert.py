import os
import time
from datetime import date, datetime
import requests
import json
import sys

SLACK_URL = 'https://hooks.slack.com/services/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'
SLACK_HEADER = {
    'Content-Type': 'application/json'
}


class APIRetry:
    '''
    Ref:
        https://www.codementor.io/@dobristoilov/python-class-decorator-part-ii-with-configuration-arguments-rv73o8pjn
        https://towardsdatascience.com/are-you-using-python-with-apis-learn-how-to-use-a-retry-decorator-27b6734c3e6
        https://medium.com/@vadimpushtaev/decorator-inside-python-class-1e74d23107f6
    '''
    def __init__(self, exception, total_tries=5, initial_wait=0.5, backoff_factor=2, *args, **kwargs):
        self.exception = exception
        self.total_tries = total_tries
        self.initial_wait = initial_wait
        self.backoff_factor = backoff_factor

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            _tries, _delay = self.total_tries + 1, self.initial_wait
            while _tries >1:
                try:
                    return func(*args, **kwargs)
                except self.exception as e:
                    _tries -= 1
                    self.api_status_logger(_tries, e, *args)
                    if _tries == 1:
                        self.api_status_logger(_tries, e, *args)

                if not _tries == 1:
                    time.sleep(_delay)
                    _delay *= self.backoff_factor
        return wrapper

    def api_status_logger(self, tries, exception_obj=None, *args):
        LOG_DIR = os.getcwd() + '/api_monitor/errors'
        date_today = datetime.now().strftime('%Y-%m-%d')
        log_file = os.path.join(LOG_DIR, f'{date_today}.txt')
        if tries == 1:
            msg = 'API called failed. No retries left'
            print(msg)
            print('Exception:', exception_obj)
        else:
            msg = f'Api called failed. Tries: {tries}'
            print(msg)
            print('Exception:', exception_obj)
        os.makedirs(LOG_DIR, exist_ok=True)

        logging_msg = '\t'.join([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            msg,
            str(exception_obj),
            str(args[0])
        ])

        self.log_to_file(log_file, logging_msg)
        print('------------------------------')

    def log_to_file(self, file_path, message):
        try:
            with open(file_path, 'a+') as f:
                f.write(message)
                f.write('\n')
        except Exception as e:
            print('Error logging error to error file.', e)
            pass


class APIService:

    @staticmethod
    @APIRetry(Exception, total_tries=5, initial_wait=2)
    def logger_api_post(data):
        print('Post url {0}, data={1}'.format(SLACK_URL, data))
        # proxies = {
        #     "http": "http://10.50.44.23:3128",
        #     "https": "http://10.50.44.23:3128",
        # }
        try:
            print("\nBLOCK: ", json.dumps(data))
            r = requests.post(SLACK_URL, data=json.dumps(data), headers=SLACK_HEADER)
        except ConnectionRefusedError as cre:
            raise Exception('Connection refused error:', str(cre))
        except Exception as e:
            raise Exception('Something\'s wrong with the request:', str(e))

        if not r.status_code == 200:
            print('Error calling post {0}'.format(SLACK_URL))
            raise Exception('API called failed with status code:', r.status_code)
        print('SUCCESS. Code:', r.status_code)
        return r.text


if __name__ == '__main__':
    start_time = sys.argv[1]
    print('start_time: ', start_time)
    f = open('error_message/report_{start_time}.txt'.format(start_time=start_time), 'r')
    details = f.read()
    f.close()
    if 'ERROR' in details:
        info = "*{part}*\n*{type}*\n*Details*:\n{details}\n*Timestamp*: {timestamp}"\
            .format(part='COMPUTER ENGINE',
                    type='TEST INSTANCES',
                    details='\n'.join(details.split('\n')[:11] + details.split('\n')[-5:]),
                    timestamp=start_time)
        data = {
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":warning: :warning: :warning:\n*ALERT  ENGINEERING  PLATFORM*\n"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": info
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":link: <https://console.engineering.vng.vn/|*EP console*>"
                    }
                }
            ]
        }
        api = APIService()
        api.logger_api_post(data)
    else:
        pass
