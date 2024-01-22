def sanitize_phone_number(phone):
    exclude = r'[(, ,),-,+]'
    clean_phone = phone.strip()
    clean_phone = clean_phone.replace('(', '').replace(')', '').replace(
        '-', '').replace('+', '').replace(' ', '')
    return clean_phone
