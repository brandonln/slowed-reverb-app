from pydub import AudioSegment
from pysndfx import AudioEffectsChain
import numpy as np
from array import array


def change_speed(audio, speed=1.0):
	out = audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate*speed)})
	return out.set_frame_rate(audio.frame_rate)

filename = str(input())

audio = AudioSegment.from_mp3(filename)

audio = change_speed(audio, speed=0.861)

samples = audio.get_array_of_samples()
npsamples = np.array(samples)

fx = (AudioEffectsChain().reverb(reverberance=70))

npsamples = fx(npsamples)

samples = array(audio.array_type, npsamples)

audio = audio._spawn(samples)

outputname, _, format = filename.partition('.')
outputname = outputname + "_snr" + '.' + format

audio.export(outputname, format=format, bitrate="320k")
