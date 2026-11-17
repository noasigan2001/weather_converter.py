import requests


def check_api(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("passed", url)

        else:
            print("failed", url, response.status_code)
    except requests.RequestException as error:
        print("error", url, error)
urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/status/404",
        "https://httpbin.org/status/500",
 ]


for url in urls:
    check_api(url)

