from sendgrid import SendGridAPIClient
from datetime import datetime, timedelta
import json

# SENDGRID_API_KEY will come from system/os environment (security reason)
sg = SendGridAPIClient()


def how_spammed(str_date):
    dt = datetime.strptime(str_date, '%Y-%m-%d')
    response = sg.client.suppression.spam_reports.get(query_params={
        'start_time': int(dt.timestamp()),
        'end_time': int((dt + timedelta(days=1)).timestamp())
    })
    return len(json.loads(response.body))


if __name__ == '__main__':
    print(how_spammed('2014-5-5'))
    print('You had {} spam reports in 2016-01-01'.format(how_spammed('2016-01-01')))
    print('Check your results')
