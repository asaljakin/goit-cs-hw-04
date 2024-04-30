import threading
import time


def search_keywords(file_path, keywords, result):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            for keyword in keywords:
                if keyword in text:
                    result[keyword].append(file_path)
    except Exception:
        print(f"Файл {file_path} відсутній")


def threaded_search(file_paths, keywords):
    threads = []
    result = {}
    
    for k in keywords:
        result[k] = []

    for file_path in file_paths:
        thread = threading.Thread(
            target=search_keywords, args=(file_path, keywords, result)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

if __name__ == "__main__":
    
    keywords = ["поток", "взаємодії", "програм", "засоби"]
    file_paths = ["./file_1.txt", "./file_2.txt", "./file_3.txt"]

    start_time = time.time()
    result = threaded_search(file_paths, keywords)
    end_time = time.time()
    
    for k, v in result.items():
        print(f"{k} : {v}")

    print(f"Час виконання threading: {end_time - start_time}")
