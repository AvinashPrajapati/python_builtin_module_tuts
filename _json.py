

# import json
# # json.
# # print(json)

# ########dumbs and loads  -> for data variable 'not for file write'

# # sample_set = {1,2, 2}
# sample_dict = {
#     "key":"value",
#     "id":1,
# }  # json in python
# # print(type(sample_dict))
# # print("dict::", sample_dict.get('id'))

# sample_json_str = json.dumps(sample_dict)

# print(type(sample_json_str))
# print("str::",sample_json_str)

# sample_json = json.loads(sample_json_str)
# print(type(sample_json))
# print("dict::", sample_json)




########## dump and load
import json

### dump : if you want to write dict/json data in a .json file

data = {
    "name":"avinash",
    "age":23,
}


# with open("data.json", "w") as f:
#     json.dump(data, f)


with open("data.json", "r") as f:
    data = json.load(f)
data['name'] = "ravi"

with open("data.json", "w") as f:
    json.dump(data, f)

f.close()

