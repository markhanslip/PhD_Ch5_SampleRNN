import Recorder
from Filters import OnsetsFilter, AmpFilter
from PitchExtraction import PitchAnalyser

from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio

import time
import random
import os

from functools import reduce

loudness_thresh = 50

############################ INTERACTIVE LOOP ###################################

pitch_thresh = 60

while True:

    rec = Recorder.Recorder(channels=1)
    with rec.open('./infer.wav', 'wb') as recfile:
        recfile.record(duration=1.5)
    time.sleep(0.05)
    rec.resample_audio()
    time.sleep(0.05)
    rec.truncate_pad()
    time.sleep(0.05)

    filter2 = AmpFilter(in_file='./infer.wav', threshold=15.0)
    result = filter2.get_mean_amp()

    if result==0: # ie no input above thresh
        print('no input detected')
    if result==1: # ie strong signal detected

        filter1 = OnsetsFilter(in_file='./infer.wav', threshold=2)
        filter1.get_freqs()
        filter1.freqs_to_MIDI()
        filter1.get_onsets()

        pitch = filter1.return_mean_pitch()
        if pitch != 0:
            if pitch <= pitch_thresh:
                print('low reg detected')
                folder = "/home/m4rk/Documents/PhD_Oct_2022/SampleRNN_interactive/curated_samps/Low"
                filelist = os.listdir(folder)

            if pitch > pitch_thresh:
                print('mid-upper reg detected')
                folder = "/home/m4rk/Documents/PhD_Oct_2022/SampleRNN_interactive/curated_samps/MedHi"
                filelist = os.listdir(folder)

            pa = PitchAnalyser('infer.wav')

            pa.load_audio()
            pa.get_freqs()
            pa.freqs_to_MIDI()
            pa.get_onsets()
            non_zeros = pa.remove_zeros_for_pitches_only()
            if len(non_zeros) > 0:

                pa.float2int()
                first, my_last, num_pitches = pa.return_outputs()

                print("my last pitch:", my_last)

                sub_filelist = []
                num_samps = random.choice([1, 2, 3, 4])

                for i in range(num_samps):
                    sub_filelist.append(random.choice(filelist))

                sub_filelist = sorted(sub_filelist)

                sub_filelist = reduce(lambda l, x: l.append(x) or l if x not in l else l, sub_filelist, [])
                print("sub filelist for sample playback:", sub_filelist)

                first_pitches_samples_dict = {}

                for generated_sample in sub_filelist:

                    pa = PitchAnalyser(os.path.join(folder, generated_sample))

                    pa.load_audio()
                    pa.get_freqs()
                    pa.freqs_to_MIDI()
                    pa.get_onsets()
                    pa.remove_zeros_for_pitches_only()
                    non_zeros = pa.remove_zeros_for_pitches_only()
                    if len(non_zeros) > 0:
                        pa.float2int()
                        first, my_last, num_pitches = pa.return_outputs()
                        first_pitches_samples_dict[first] = generated_sample

                print("first_pitches_samples_dict:", first_pitches_samples_dict)

                diffs = {}
                for first_pitch_of_sample, filepath in zip(first_pitches_samples_dict.keys(), first_pitches_samples_dict.values()):
                    diffs[abs(first_pitch_of_sample-my_last)] = filepath
                    print("diff:", abs(first_pitch_of_sample-my_last), "filepath:", filepath)

                print("diffs:", diffs)

                first_sample = diffs[min(diffs.keys())]
                print("first sample is", first_sample)

                # first sample is one whose first pitch is closest to my last ala point-to-point interaction
                # first_sample_index = diffs.index(min(diffs))

                snd = AudioSegment.from_file(os.path.join(folder, first_sample))

                sub_filelist.remove(first_sample)

                print("filelist after samp 1 removed:", sub_filelist)

                if len(sub_filelist) > 0:
                    for wavfile in sub_filelist:
                        new_snd = AudioSegment.from_file(os.path.join(folder, wavfile))
                        snd = snd.append(new_snd, crossfade=75)

                snd = snd.fade_in(75).fade_out(75)
                _play_with_simpleaudio(snd)
                time.sleep(num_samps*1.5) # for space, think it suits the vibe

            else:
                pass
