import threading

threads = []
max_threads = 100
while threads or csv_reader:
    for thread in threads:
        if not thread.is_alive():
            threads.remove(thread)

    while len(threads) < max_threads and csv_reader:
        thread = threading.Thread(target=insert_row, args=("sub",))
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)