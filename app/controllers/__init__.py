from app.exc.exc import BadRequestError


def filter_by_uf(republics, uf):
    if not uf: return republics
    
    return [i for i in republics if i.address.uf == uf.upper()]


def verification(data,keys):
    missing_keys=[]
    value_incorrect = []
    for key,value in keys.items():
            if not key in data:
                missing_keys.append(key)
            if (key in data) and (value != type(data[key])):
                value = str(value)
                teste = value.replace("class ", "").replace("<", "").replace(">", "")
                print(teste)
                value_incorrect.append(f"correct value for {key} : {teste}")
    if missing_keys: raise BadRequestError(f'Required keys not found: {missing_keys}')
    if value_incorrect: raise BadRequestError(f'Required correct values: {value_incorrect}')
