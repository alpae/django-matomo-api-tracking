import requests
from celery import shared_task
import logging
from urllib.parse import urlparse, parse_qs

logger = logging.getLogger(__name__)


@shared_task
def send_matomo_tracking(params):
    url = params.get('url')
    user_agent = params.get('user_agent')
    language = params.get('language')

    headers = {'User-Agent': user_agent, 'Accept-Language': language}
    resp = requests.get(url, headers=headers)
    if resp.ok:
        logger.debug("successfully sent tracking request: {}".format(url))
    else:
        logger.warning("sending tracking request failed: {}".format(resp.reason))
        qs = parse_qs(urlparse(url).query)
        logger.warning("url-query-params: {}; User-Agent: {}; language: {}"
                       .format(qs, user_agent, language))
