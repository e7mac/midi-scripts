import threading

def create_threads(func, arg_list):
	threads = []
	for arg in arg_list:
		thread = threading.Thread(target=func, args=[arg])
		threads.append(thread)
	return threads

def process_parallel(threads, chunk_size):
	chunks = [threads[x:x+chunk_size] for x in xrange(0, len(threads), chunk_size)]
	for chunk in chunks:
		for thread in chunk:
			thread.start()
		for thread in chunk:
			thread.join()
