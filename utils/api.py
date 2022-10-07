from utils.http_method import Http_method

base = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

"""Methods for location api"""

class Google_maps_api():

    """Create new location"""
    @staticmethod
    def create_location(address):
        post_res = "/maps/api/place/add/json"
        result = Http_method.post(base + post_res + key, address)
        return result

    """Get location"""
    @staticmethod
    def get_location(place_id):
        get_res = "/maps/api/place/get/json"
        result = Http_method.get(base + get_res + key + "&place_id=" + place_id)
        return result

    """Update location"""
    @staticmethod
    def put_location(place_id, address):
        put_res = "/maps/api/place/update/json"
        json_body = {
            "place_id": place_id,
            "address": address,
            "key": "qaclick123"
        }
        result = Http_method.put(base + put_res + key, json_body)
        return result

    """Delete location"""
    @staticmethod
    def del_location(place_id):
        del_res = "/maps/api/place/delete/json"
        json_body = {
            "place_id": place_id
        }
        result = Http_method.delete(base + del_res + key, json_body)
        return result



