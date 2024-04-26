from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
import os
import nltk
import speech_recognition as sr

gif_folder = '/Users/Computer Science/Desktop/AIProject/Gifs'
def split_arabic_text(text):
    # Tokenize the Arabic text into words
    words = nltk.word_tokenize(text)
    return words

def get_gif_file(word, gif_folder):
    # Assuming each word has its gif named with the same word
    gif_file = os.path.join(gif_folder, f"{word}.gif")
    return gif_file

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        recognized_text = recognizer.recognize_google(audio, language='ar')
        return recognized_text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Error during speech recognition: {0}".format(e))

def display_gif_sequence(words, gif_folder):
    # Initialize Tkinter
    root = tk.Tk()
    root.title("ترجمة النص الي لغة اشاره")
    root.geometry("330x330")

    for word in words:
        gif_file = get_gif_file(word, gif_folder)
        if os.path.exists(gif_file):
            # Display the GIF file for the word
            gif = Image.open(gif_file)
            frames = [ImageTk.PhotoImage(frame.convert("RGBA"))  for frame in ImageSequence.Iterator(gif)]
            for frame in frames:
                label = tk.Label(root, image=frame)
                label.pack()
                root.update()
                root.after(10)
                label.destroy()
        else:
            # Split the word into characters and display corresponding GIFs
            for char in word:
                char_gif_file = get_gif_file(char, gif_folder)
                char_gif = Image.open(char_gif_file)
                char_frames = [ImageTk.PhotoImage(frame.convert("RGBA"))  for frame in ImageSequence.Iterator(char_gif)]
                for frame in char_frames:
                    label = tk.Label(root, image=frame)
                    label.pack()
                    root.update()
                    root.after(10)
                    label.destroy()

    root.mainloop()
