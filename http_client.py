# http
import requests
from testApiController.json_response import JsonResponse
class HttpClient:

    def __init__(self, url):
        self.baseurl = url

    def get(self, route=''):
        res = requests.get(f'{self.baseurl}{route}')
        jsonresp = JsonResponse(res.status_code, res.json())
        return jsonresp