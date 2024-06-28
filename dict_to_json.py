import json

class DataClass:
    def __init__(self, value):
        self.value = value


sample_dict = {"key": "value",
               "data_key": DataClass("data_value")}

try:
    with open(r"./sample.json", "w") as fp:
        json.dump(sample_dict, fp, indent=2)
except Exception as e:
    print(e)
    # Object of type DataClass is not JSON serializable

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
    

with open(r"./sample.json", "w") as fp:
    json.dump(sample_dict, fp, indent=2, default=dumper)

