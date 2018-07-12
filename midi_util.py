import midi
import os
import file_util
import threading

def read_midi_file(filename):
	return midi.read_midifile(filename)

def write_midi_file(pattern, filename):
	midi.write_midifile(filename, pattern)

def adjust_tempo(pattern, fraction):
	for track in pattern:
		for event in track:
			if isinstance(event, midi.events.SetTempoEvent):
				bpm = event.get_bpm()
				event.set_bpm(bpm * fraction)

def change_tempo_of_file(filename, fraction):
	midz = read_midi_file(filename)
	adjust_tempo(midz, fraction)
	write_midi_file(midz, filename)

def slow_down_midi(fraction=0.6):
	threads = []
	for file in file_util.get_all_files('.mid'):
		thread = threading.Thread(target=change_tempo_of_file, args=(file, fraction))
		threads.append(thread)
		thread.start()
	for thread in threads:
		thread.join()
