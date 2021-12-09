from app.models.address_model import AddressModel
from app.models.state_model import StateModel
from app.configs.database import db


def create_address(address_data):
    street = address_data["street"].title()
    street_number = address_data["street_number"]
    city = address_data["city"]
    uf = address_data["uf"].upper()
    uf_id = StateModel.query.filter_by(uf=uf).first().id
    zip_code = address_data["zip_code"]

    address = AddressModel(street=street, street_number=street_number, city=city, uf_id=uf_id, zip_code=zip_code)
    db.session.add(address)
    db.session.commit()
    return address.id

def update_adress(address_data):
    
    for i in address_data:
        if type(i) != str: raise TypeError
    data = {}
    if 'uf' in address_data: data['uf'] = address_data['uf'].upper()
    if 'street_number' in address_data: data['street_number'] = address_data['street_number'].title()
    if 'city' in address_data: data['city'] = address_data['city']
    if 'zip_code' in address_data: data['zip_code'] = address_data['zip_code']
    if 'uf' in address_data:
        data['uf'] = address_data['uf'].upper()
        uf_id = AddressModel.uf_id = StateModel.query.filter_by(uf=data['uf']).first_or_404().id
    db.session.commit()

    
# {
#         "uf":"RJ",
#         "street":"rua b",
#         "street_number":"3",
#         "city":"Rezende",
#         "zip_code":"12345679"
#       
#     }
    ...

