import time
from generator import generate_fake_users
from processor import DataProcessor

def main():
    COUNT = 50_000
    FILENAME = "large_data.ndjson"

    print(f"--- Генерация {COUNT} объектов ---")
    users = generate_fake_users(COUNT)

    # Тест записи
    start = time.perf_counter()
    DataProcessor.save_to_ndjson(users, FILENAME)
    write_time = time.perf_counter() - start
    print(f" Запись {COUNT} строк в NDJSON: {write_time:.4f} сек")

    # Тест чтения
    start = time.perf_counter()
    loaded_data = DataProcessor.read_from_ndjson(FILENAME)
    read_time = time.perf_counter() - start
    print(f" Чтение {COUNT} строк: {read_time:.4f} сек")
    
    print(f"\nИтого: обработано {len(loaded_data)} записей.")
    print(f"Пример данных: {loaded_data[0]['username']} | Роль: {loaded_data[0]['role']}")

if __name__ == "__main__":
    main()
