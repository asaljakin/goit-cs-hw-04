import multiprocessing
import time


def search_keywords(file_path, keywords, queue):
    result = {keyword: [] for keyword in keywords}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            for keyword in keywords:
                if keyword in text:
                    result[keyword].append(file_path)
    except Exception:
        print(f"Файл {file_path} відсутній")
    queue.put(result)
    
def multiprocess_search(file_paths, keywords):
    processes = []
    queue = multiprocessing.Queue()
    result = {}
    for k in keywords:
        result[k] = []

    for file_path in file_paths:
        process = multiprocessing.Process(
            target=search_keywords, args=(file_path, keywords, queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not queue.empty():
        res = queue.get()
        for keyword in res:
            result[keyword].extend(res[keyword])
    
    return result


if __name__ == "__main__":
    
    keywords = ["поток", "взаємодії", "програм", "засоби"]
    file_paths = ["./file_1.txt", "./file_2.txt", "./file_3.txt"]

    start_time = time.time()
    result = multiprocess_search(file_paths, keywords)
    end_time = time.time()

    for k, v in result.items():
        print(f"{k} : {v}")
        
    print(f"Час виконання multiprocessing: {end_time - start_time}")
