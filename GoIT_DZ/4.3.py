def format_ingredients(items):
    receipt = ''
    a = len(items)
    if len(items) == 1:
        for i in items:
            receipt += i
    else:
        for i in items[0:1]:
            receipt += i
        for i in items[1:-1:]:
            receipt += ', ' + i
        for i in items[a-1:a+1]:
            receipt += ' and ' + i

    return receipt


items = ["2 eggs"]
print(format_ingredients(items))
