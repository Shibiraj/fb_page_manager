import json, requests

class FacebookPageManager(object):
    """ Manages the Facebook Page"""
    API_ENDPOINT = 'https://graph.facebook.com/v2.10'

    def __init__(self, access_token):
        self.access_token = access_token

    def get_page_info(self):
        # returns the page information (first page) fb page owned by the user
        payload = {'access_token': self.access_token}
        url = '{}/me/accounts'.format(self.API_ENDPOINT)
        resp = requests.get(url, params = payload)
        data = json.loads(resp.text)
        if data.get('data'):
            page_info = data.get('data')[0]
            payload = {'access_token': self.access_token, 'fields' : 'single_line_address,phone,is_published,overall_star_rating,emails,about,location'}
            url = '{}/{}/'.format(self.API_ENDPOINT, page_info.get('id'))
            resp = requests.get(url, params = payload)
            data = json.loads(resp.text)
            data.update({'emails' :','.join(data.get('emails', []))})
            page_info.update(data)
            page_info.update({'listed' : True})
        else:
            page_info = {'listed' : False}
        print('Page get info response ', page_info)
        return page_info

    def update_page_info(self, data):
        # updates facebook page information
        location =  '{'+'"city": "{city}", "street": "{street}", "country": "{country}", "zip": "{zip}"'.format(city=data.get('city'), street=data.get('street'), country=data.get('country'), zip=data.get('zip')) + '}'
        payload = {'access_token': data.get('access_token'), 'about' : data.get('about',''),'phone' : data.get('phone',''),'state' : data.get('state',''), 'emails' : '["{}",]'.format(data.get('emails')), 'location' : location}
        url = '{}/{}/'.format(self.API_ENDPOINT, data.get('id'))
        resp = requests.post(url, params = payload)
        print('Page update response ', resp.text)
        return json.loads(resp.text)
