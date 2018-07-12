import midi_util
import audio_util
import file_util

print("Cleaning up filenames")
file_util.rename('.png', '.png.png', '.png')
file_util.rename('.mid', '.midi.mid', '.mid')
file_util.rename('.PNG', '.PNG', '.png')
print("DONE")

print("Slowing down MIDI Files")
midi_util.slow_down_midi()
print("DONE")
print("Rendering all MIDI to WAV")
audio_util.convert_all_mid_to_wav()
print("DONE")

print("Converting WAV to MP3 - this takes a while")
audio_util.convert_all_wav_to_mp3()	
print("DONE")
print("Deleting all WAV files")
file_util.delete_all(".wav")
print("DONE")
