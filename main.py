import orjson
from datetime import datetime

data = {
    "name": "Baga",
    "time": datetime.now()
}

json_data = orjson.dumps(data)
print("JSON (bytes):", json_data)

parsed = orjson.loads(json_data)
print("Обратно в объект:", parsed)