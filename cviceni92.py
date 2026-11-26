from sixth import download_url_and_get_all_hrefs
from unittest.mock import MagicMock
import requests


def test_download_url_and_get_all_hrefs():
    data = '<html><body><a id="1" href="https://www.jcu.cz">odkaz</a><div><a href="http://ef.jcu.cz/kontakty">kontakty</a></div></body></html>'

    requests.get = MagicMock()
    requests.get.return_value.status_code = 200
    requests.get.return_value.content = data.encode('utf-8')

    href = download_url_and_get_all_hrefs('xxx')

    assert href == ['https://www.jcu.cz', 'http://ef.jcu.cz/kontakty']
    