import allure
from termcolor import colored
from utils.validation import *
from utils.api import *

"""CRUD new location"""
@allure.epic("Test create location")
class Test_loc():

    def return_value(self):
        res_get: Response = Google_maps_api.get_location(place_id)
        return res_get

    @allure.description("Create new location")
    def test_post_loc(self):
        address = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                },
                "accuracy": 50,
                "name": "Frontlinehouse",
                "phone_number": "(+91)9838933937",
                "address": "29,sidelayout,cohen09",
                "types": [
                    "shoepark",
                    "shop"
                ],
                "website": "http://google.com",
                "language": "French-IN"
            }
        result: Response = Google_maps_api.create_location(address)
        Validation.val_status_code(result, 200)
        Validation.val_json_token(result, ['status', 'place_id', 'scope', 'reference', 'id'])
        Validation.val_json_value(result, 'status', 'OK')
        global place_id
        place_id = result.json().get('place_id')
        ver_res = self.return_value()
        Validation.val_json_value(ver_res, 'address', address.get('address'))

    @allure.description("Return location")
    def test_get_loc(self):
        res_get = self.return_value()
        Validation.val_status_code(res_get, 200)
        Validation.val_json_token(res_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        print('\nGet result:\n', res_get.json())

    @allure.description("Update location")
    def test_put_loc(self):
        address = 'Chernyahovskogo 23A, Ukraine'
        res_put: Response = Google_maps_api.put_location(place_id, address)
        Validation.val_status_code(res_put, 200)
        Validation.val_json_token(res_put, ['msg'])
        Validation.val_json_value(res_put, 'msg', 'Address successfully updated')
        self.test_get_loc()
        ver_res = self.return_value()
        Validation.val_json_value(ver_res, 'address', address)

    @allure.description("Delete location")
    def test_del_loc(self):
        res_del: Response = Google_maps_api.del_location(place_id)
        Validation.val_status_code(res_del, 200)
        Validation.val_json_token(res_del, ['status'])
        Validation.val_json_value(res_del, 'status', 'OK')
        ver_res = self.return_value()
        Validation.val_status_code(ver_res, 404)
        Validation.val_json_value(ver_res, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        print(colored('CRUD new location verifications passed', 'green'))

