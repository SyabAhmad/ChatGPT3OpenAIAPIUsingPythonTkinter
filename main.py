# import tkinter as tk
# from openai import api_key
# import openai
#
# # Create the window and set the title
# window = tk.Tk()
# window.title("GPT Message")
#
# # Create the label and set the text
# label = tk.Label(window, text="")
# label.pack()
#
#
# # Create a function to get a message from the GPT API and set the label text
# def get_message():
#     # Use the GPT API to get a message
#     openai.api_key = "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"
#     prompt = "Write a message to display on the label"
#     model_engine = "text-davinci-002"
#     completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
#                                            temperature=0.5)
#     message = completions.choices[0].text
#
#     # Set the label text
#     label.config(text=message)
#
#
# # Create a button to get a new message
#
# button = tk.Button(window, text="Get Message", command=get_message)
# button.pack()
#
# # Run the main loop
# window.mainloop()

from tkinter import *
import openai
mainWindow = Tk()
#mainWindow.maxsize(height=400, width=420)
# Set the API key

# Use the GPT-3 model to generate text
# completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
# message = completions.choices[0].text
# print(message)

input = Entry(mainWindow, borderwidth=6).grid(row=3, column=3)

def on_click():
    openai.api_key = "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"
    #model_engine = "text-davinci-002"
    # model_engine = "text-ada-001"
    # model_engine = "text-babbage-001"
    # model_engine = "text-curie-001"
    model_engine = "text-davinci-003"
    completions = openai.Completion.create(engine=model_engine, prompt=str(input), max_tokens=4000, n=1, stop=None, temperature=0.6)
    message = completions.choices[0].text
    Label(mainWindow, text=message, wraplength=300).grid(row=4, column=3)

# noinspection PyTypeChecker
Label(mainWindow, text="Open AI Chat GPT Test").grid(row=0, column=2)

Label(mainWindow, text="Enter your Query").grid(row=3, column=2)

Button(mainWindow, text="Show Result", command=on_click).grid(row=3, column=4)
#Button(mainWindow, text="Show Result").grid(row=3, column=4)
mainWindow.mainloop()