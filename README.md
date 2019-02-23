# voice_tic_tac_toe
This is a tic tac toe with voice recognization and text to speech conversion. Written in python.
requires internet connection

Uses google for speech recognization. 
change r.recognize_google to any of your choice.
Options you can use are:
  Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs. These are:

    recognize_bing(): Microsoft Bing Speech
    recognize_google(): Google Web Speech API
    recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
    recognize_houndify(): Houndify by SoundHound
    recognize_ibm(): IBM Speech to Text
    recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
    recognize_wit(): Wit.ai

Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine. The other six all require an internet connection.
get pocketsphinx from https://pypi.org/project/pocketsphinx/


Requirements:
  SpeechRecognition
  pyttsx3
  
  
Install requirements by following command:
  pip install -r requirements.txt
