import os
import threading
import multi_util

def get_all_files(extension):
	all_files = []
	for root, dirs, files in os.walk("."):
		for file in files:
			if file.endswith(extension):
				all_files.append(os.path.join(root, file))
	return all_files

def rename(extension, pattern_in, pattern_out):
	args = []
	for file in get_all_files(extension):
		file_in = file
		file_out = file.replace(pattern_in, pattern_out)
		comm = 'mv "' + file_in + '" "' + file_out + '"'
		args.append(comm)
	threads = multi_util.create_threads(os.system, args)
	multi_util.process_parallel(threads, 100)


def delete_all(extension):
	args = []
	for file in get_all_files(extension):
		comm = 'rm "' + file + '"'
		args.append(comm)
	threads = multi_util.create_threads(os.system, args)
	multi_util.process_parallel(threads, 100)
