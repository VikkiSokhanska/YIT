class UserData:
    def __init__(self, data):
        self.gender = data['results'][0]['gender']
        self.name_title = data['results'][0]['name'].get('title', '')
        self.name_first = data['results'][0]['name'].get('first', '')
        self.name_last = data['results'][0]['name'].get('last', '')
        self.street_number = data['results'][0]['location'].get('street', {}).get('number', '')
        self.street_name = data['results'][0]['location'].get('street', {}).get('name', '')
        self.city = data['results'][0]['location'].get('city', '')
        self.state = data['results'][0]['location'].get('state', '')
        self.country = data['results'][0]['location'].get('country', '')
        self.postcode = data['results'][0]['location'].get('postcode', '')
        self.email = data['results'][0]['email']
        self.username = data['results'][0]['login'].get('username', '')
        self.password = data['results'][0]['login'].get('password', '')
        self.dob_date = data['results'][0]['dob'].get('date', '')
        self.age = data['results'][0]['dob'].get('age', '')
        self.registered_date = data['results'][0]['registered'].get('date', '')
        self.phone = data['results'][0]['phone']
        self.cell = data['results'][0]['cell']
        self.id_name = data['results'][0]['id'].get('name', '')
        self.id_value = data['results'][0]['id'].get('value', '')
        self.picture_large = data['results'][0]['picture'].get('large', '')
