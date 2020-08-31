def test_url_status(url, status, method):
    response = method(url)
    print("status response = ", response.status_code, "type response =", type(response.status_code))
    assert response.status_code == int(status)
