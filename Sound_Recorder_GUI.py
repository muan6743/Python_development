import pip
pip.main(['install', 'sounddevice'])
import sounddevice as sd 
import soundfile as sf 
from tkinter import *


def Voice_rec(): 
	fs = 48000
	
	# seconds 
	duration = 5
	myrecording = sd.rec(int(duration * fs), 
						samplerate=fs, channels=2) 
	sd.wait() 
	
	# Save the recording as a FLAC file with the correct sampling rate
	return sf.write('my_Audio_file.flac', myrecording, fs) 


master = Tk() 

# Create a label with the text "Voice Recorder:" and add it to the window

Label(master, text=" Voice Recoder : "
	).grid(row=0, sticky=W, rowspan=5) 

# Create a button that starts the voice recording when clicked

b = Button(master, text="Start", command=Voice_rec) 
b.grid(row=0, column=2, columnspan=2, rowspan=2, 
	padx=5, pady=5) 

mainloop()
