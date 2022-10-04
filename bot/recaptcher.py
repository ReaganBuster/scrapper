from pydub import AudioSegment
import sys
import os
import speech_recognition as sr

class Recaptcher():
     def mp3_to_text():

        path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "audio.mp3"))
        path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))

        filename = path_to_mp3

        sound = AudioSegment.from_mp3(filename)
        sound.export(path_to_wav, format="wav")

        file_audio = sr.AudioFile(path_to_wav)

        r = sr.Recognizer()

        with sr.AudioFile(file_audio) as source:

            audio = r.record(source)

        try:

            return r.recognize_google(audio)

        except sr.UnknownValueError:

            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:

            print("Could not request results from Google Speech Recognition service; {0}".format(e))

            sys.exit()

        

        # text = mp3_to_text(path_to_wav)

        # print(text)

    # This will convert the MP3 file audio.mp3 to text and print it to the console. You can also save the text to a file by writing it to a file instead of printing it:

    # filename = "audio.mp3"

    # text = mp3_to_text(file_audio)

    # with open("output.txt", "w") as f:

    #     f.write(text)