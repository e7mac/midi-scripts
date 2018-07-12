import file_util
import multi_util
from pydub import AudioSegment
import threading
import os

def convert_to_mp3(file_in):
	file_out = file_in.replace(".wav", ".mp3")
	AudioSegment.from_file(file_in).export(file_out, format='mp3')

def convert_to_wav(file_in):
	file_out = file_in.replace(".mid", ".wav")
	comm = 'timidity "' + file_in + '" -Ow -o "' + file_out + '"'
	os.system(comm)

def convert_all_wav_to_mp3():
	threads = multi_util.create_threads(convert_to_mp3, file_util.get_all_files('.wav'))
	multi_util.process_parallel(threads, 20)

def convert_all_mid_to_wav():
	threads = multi_util.create_threads(convert_to_wav, file_util.get_all_files('.mid'))
	multi_util.process_parallel(threads, 100)
		