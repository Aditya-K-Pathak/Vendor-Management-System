import requests

class VendorManagementTestCase:

    def __init__(self):

        self.URL = 'http://127.0.0.1:8000/'
        self.TOKEN = '0903c19195d23cc273ec87b63aa128e977b5c825'

        if not self.TOKEN:
            response = requests.post(self.URL + 'api/user/', data = {
                'username': 'Aditya2874',
                'password': 'Password'
            })
            TOKEN = response.json().get('token')
    
    def create_vendor(self) -> str:
        url = self.URL + 'api/vendors/'
        vendor_data = {
            'vendor_name': 'Aditya Pathak',
            'contact_number': 8840207363,
            'address': 'India'
        }
        response = requests.post(url, headers = {'Authorization': f'Token {self.TOKEN}'}, data = vendor_data)
        return response.json()['vendor_code']
    
    def get_all_vendors(self) -> dict:
        url = self.URL + 'api/vendors/'
        response = requests.get(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.json()
    
    def get_one_vendor(self, vendor_code: str) -> dict:
        url = self.URL + f'api/vendors/{vendor_code}/'
        response = requests.get(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.json()
    
    def update_vendor(self, vendor_code: str) -> dict:
        url = self.URL + f'api/vendors/{vendor_code}/'
        vendor_data = {
            'vendor_name': 'Aditya Pathak',
            'contact_number': 8840207363,
            'address': 'India',
            'new_orders': '{"Apple":1}'
        }
        response = requests.put(url, headers = {'Authorization': f'Token {self.TOKEN}'}, data = vendor_data)
        return response.json()
    
    def delete_vendor(self, vendor_code: str):
        url = self.URL + f'api/vendors/{vendor_code}/'
        response = requests.delete(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.status_code

class PurchaseOrderTestCase:

    def __init__(self):

        self.URL = 'http://127.0.0.1:8000/'
        self.TOKEN = '0903c19195d23cc273ec87b63aa128e977b5c825'

        if not self.TOKEN:
            response = requests.post(self.URL + 'api/user/', data = {
                'username': 'Aditya2874',
                'password': 'Password'
            })
            TOKEN = response.json().get('token')
    
    def create_purchase_order(self, vendor_code: str) -> int:
        url = self.URL + 'api/purchase_orders/'
        po_data = {
            'vendor_code': vendor_code,
            'order_status': 'Pending',
            'items': '{"item1": 1, "item2": 1}',
            'quantity': 2
        }
        response = requests.post(url, headers = {'Authorization': f'Token {self.TOKEN}'}, data = po_data)
        return response.status_code
    
    def get_all_purchase_orders(self) -> dict:
        url = self.URL + 'api/purchase_orders/'
        response = requests.get(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.json()
    
    def get_one_purchase_order(self, po_id: int) -> dict:
        url = self.URL + f'api/purchase_orders/{po_id}/'
        response = requests.get(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.json()
    
    def update_purchase_order(self, po_id: int) -> dict:
        url = self.URL + f'api/purchase_orders/{po_id}/'
        po_data = {
            'order_status': 'Completed'
        }
        response = requests.put(url, headers = {'Authorization': f'Token {self.TOKEN}'}, data = po_data)
        return response.json()
    
    def delete_purchase_order(self, po_id: int):
        url = self.URL + f'api/purchase_orders/{po_id}/'
        response = requests.delete(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.status_code

class PerformanceMetricsTestCase():

    def __init__(self):

        self.URL = 'http://127.0.0.1:8000/'
        self.TOKEN = '0903c19195d23cc273ec87b63aa128e977b5c825'

        if not self.TOKEN:
            response = requests.post(self.URL + 'api/user/', data = {
                'username': 'Aditya2874',
                'password': 'Password'
            })
            TOKEN = response.json().get('token')

    def get_performance_metrics(self, vendor_code: str) -> dict:
        url = self.URL + f'api/vendors/{vendor_code}/performance/'
        response = requests.get(url, headers = {'Authorization': f'Token {self.TOKEN}'})
        return response.json()