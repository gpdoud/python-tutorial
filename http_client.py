# http
import requests
from testApiController.json_response import JsonResponse
class HttpClient:

    def __init__(self, url):
        self.baseurl = url

    def get(self, route=''):
        res = requests.get(f'{self.baseurl}{route}')
        return JsonResponse(self.getHttpCodeMessage(res.status_code), res.json())
    
    def post(self, route='', data=None):
        res = requests.post(f'{self.baseurl}{route}', data, headers={'content-type':'application/json'})
        return JsonResponse(res.status_code, res.json())

    def put(self, route='', data=None):
        res = requests.put(f'{self.baseurl}{route}', data, headers={'content-type':'application/json'})
        return JsonResponse(self.getHttpCodeMessage(res.status_code))
    
    def delete(self, route=''):
        res = requests.delete(f'{self.baseurl}{route}')
        return JsonResponse(self.getHttpCodeMessage(res.status_code))
    
    def getHttpCodeMessage(self, code):
        match code:
            case 200: return "200 OK"
            case 201: return "201 CREATED"
            case 204: return "204 NO CONTENT"

            case 400: return "400 BAD REQUEST"
            case 401: return "401 UNAUTHORIZED"
            case 403: return "403 FORBIDDEN"
            case 404: return "404 NOT FOUND"
            case 405: return "405 METHOD NOT ALLOWED"
            
            case 500: return "500 INTERNAL SERVER ERROR"

            
        