def change_to_dict_del_some_fields(value: str):
    pairs = value.split('&')

    data = {}
    for pair in pairs:
        key, value = pair.split('=')
        data[key] = value
    
    if '_save' in data:
        del data['_save']
    
    if 'post' in data:
        del data['post']

    if 'csrfmiddlewaretoken' in data:
        del data['csrfmiddlewaretoken']

    return data