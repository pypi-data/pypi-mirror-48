# pySpeechAlien

Speech analysis tool - modified version of [Shahabks/my-voice-analysis](https://github.com/Shahabks/my-voice-analysis).

pySpeechAlien can analyze .wav audio files to determine gender, mood, number of syllables, number of pauses, duration of speech, speech rate, etc.

## Getting Started

To get this project up and running on your local machine, follow the below instructions.

There have been reported issues with running this program in Python 3, so if you run into issues, please use Python 2.7. pySpeechAlien is developed and tested in Python 2.7.16.

Install pySpeechAlien using pip (may need to use pip2).
```
pip install pySpeechAlien
```
Upgrade to the latest version using pip (may need to use pip2).
```
pip install -U pySpeechAlien
```
Download myspsolution.praat and speech_analysis.py, and move them to the folder containing your .wav audio files. Inside speech_analysis.py, replace the following with the path of the folder containing your .wav audio files.
```
location = r"/Users/arpansahoo/Documents/GitHub/pySpeechAlien"
```
Then, inside speech_analysis.py, replace the following with the name of the audio file you would like to analyze (exclude the .wav extension).
```
file_name = "erica"
```
Then, just run the following to run the analysis. You may need to specify python2.
```
python speech_analysis.py
```
