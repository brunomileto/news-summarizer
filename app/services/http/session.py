import requests


class HttpSession:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        self.session = requests.Session()

    def fetch_url(self, url, timeout=10):
        try:
            pass
        except Exception as e:
            raise Exception(f"Error occurred while fetching URL {url}: {e}")

    def is_url_valid(self, url):
        try:
            response = self.session.get(url, headers=self.headers)
            return response.status_code == 200
        except Exception:
            return False
