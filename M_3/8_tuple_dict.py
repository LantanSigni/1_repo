not_empty = (2, 4, 6)
not_empty[0]    # 2
not_empty[1]    # 4
not_empty[2]    # 6

some_dict = {
    "key": "value",
    1: "one",
}

not_empty = {"key": "value"}
not_empty["new_key"] = "new value"
print(not_empty)    # {"key": "value", "new_key": "new value"}
