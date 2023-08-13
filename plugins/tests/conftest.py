import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)

@pytest.fixture
def wait_for_airflow() -> requests.Session:
    api_url = f"http://airflow-web:8080/health"
    return assert_container_is_ready(api_url)


def assert_container_is_ready(readiness_check_url) -> requests.Session:
    request_session = requests.Session()
    retries = Retry(
        total=20,
        backoff_factor=0.2,
        status_forcelist=[404, 500, 502, 503, 504],
    )
    request_session.mount("http://", HTTPAdapter(max_retries=retries))
    assert request_session.get(readiness_check_url)
    return request_session