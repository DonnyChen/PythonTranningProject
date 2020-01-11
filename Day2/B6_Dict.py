import datetime

birthday = datetime.datetime.strptime("2019-02-05", "%Y-%m-%d").date()
print(birthday)

dict_a = {"name": "jack",
    "position":'M',
    "birthday":birthday}

print(dict_a)
print(dict_a["birthday"])

print(sorted(dict_a))

dict_b = {}

dict_b["id"] = 1
dict_b["type"] = "M"
dict_b["salary"] = 500

dict_b.update({"mobile":124455})

print(dict_b.keys(), dict_b.values(), dict_b.items())

print("工号:%(id)s，职位类型: %(type)s, 工资: %(salary)d" % dict_b)