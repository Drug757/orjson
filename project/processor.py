import orjson
from typing import List
from models import UserProfile

class DataProcessor:
    # Флаги для максимальной производительности и корректности
    SERIALIZE_OPTS = (
        orjson.OPT_SERIALIZE_DATACLASS | 
        orjson.OPT_SERIALIZE_UUID | 
        orjson.OPT_APPEND_NEWLINE  # Добавляет \n после каждого дампа
    )

    @staticmethod
    def save_to_ndjson(data: List[UserProfile], filename: str):
        """Сохраняет список объектов в формате NDJSON."""
        with open(filename, "wb") as f:
            for item in data:
                # Мгновенная сериализация в байты
                f.write(orjson.dumps(item, option=DataProcessor.SERIALIZE_OPTS))

    @staticmethod
    def read_from_ndjson(filename: str) -> List[dict]:
        """Потоковое чтение NDJSON."""
        results = []
        with open(filename, "rb") as f:
            for line in f:
                if line.strip():
                    results.append(orjson.loads(line))
        return results

    @staticmethod
    def fast_serialize_custom(obj):
        """Пример обработки совсем нестандартных типов."""
        # orjson работает молниеносно через default handler
        return orjson.dumps(
            obj, 
            default=lambda x: str(x) if isinstance(x, complex) else None
        )
