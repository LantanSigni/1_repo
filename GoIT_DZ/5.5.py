def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    country_dict = {
        'UA': [],
        'JP': [],
        'TW': [],
        'SG': []
    }
    for phone_number in list_phones:
        clean_number = sanitize_phone_number(phone_number)
        if clean_number.startswith('81'):
            country_dict["JP"].append(clean_number)
        elif clean_number.startswith('886'):
            country_dict["TW"].append(clean_number)
        elif clean_number.startswith('65'):
            country_dict["SG"].append(clean_number)
        else:
            country_dict["UA"].append(clean_number)

    return country_dict
