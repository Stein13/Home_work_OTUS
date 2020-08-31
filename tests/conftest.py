import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru/sfhfhfhfhfhfhfhfh",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )

    parser.addoption(
        "--status",
        default="404",
        help="Status code"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status(request):
    return request.config.getoption("--status")


@pytest.fixture
def method(request):
    m = request.config.getoption("--method")
    if m == "get":
        return requests.get