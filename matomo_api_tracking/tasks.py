import requests
from celery import shared_task


@shared_task
def send_matomo_tracking(params):
    url = params.get('url')
    user_agent = params.get('user_agent')
    language = params.get('language')

    headers = {'User-Agent': user_agent, 'Accept-Language': language}
    requests.get(url, headers=headers)