def get_fullname(first_name, last_name, middle_name=''):
    if last_name:
        if middle_name:
            get_fullname = f"{first_name} {middle_name} {last_name}"
        else:
            get_fullname = f"{first_name} {last_name}"
    else:
        get_fullname = first_name

    return get_fullname
