import json
data = {"name":"shahriar","age":25,101:"easy"}
with open("read.json","w") as f:
    json.dump(data,f)