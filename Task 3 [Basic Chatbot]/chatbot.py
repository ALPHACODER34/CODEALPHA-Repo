import tkinter as tk
from tkinter import scrolledtext, END
import nltk
from nltk.chat.util import Chat, reflections

class ChatGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ChatBot")
        
        self.chatbot = Chat(self.get_patterns(), reflections)
        
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.master, width=40, height=10, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.master, width=40)
        self.entry.pack(padx=10, pady=10)

        self.btn_send = tk.Button(self.master, text="Send", command=self.send_message)
        self.btn_send.pack(padx=10, pady=10)

    def send_message(self):
        user_input = self.entry.get()
        self.display_message(f"You: {user_input}\n", color='black')
        
        response = self.chatbot.respond(user_input)
        self.display_message(f"ChatBot: {response}\n", color='green')

        self.entry.delete(0, END)

    def display_message(self, message, color='black'):
        self.text_area.tag_config(color, foreground=color)
        self.text_area.insert(tk.END, message, color)
        self.text_area.yview(tk.END)


    def get_patterns(self):
        # Define chat patterns and responses here
        patterns = [
           (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
        (r'how are you', ['I am good, thank you!', 'I am doing well. How about you?']),
        (r'(.*) your name', ['I am a chatbot created with NLTK.', 'You can call me ChatBot.']),
        (r'what can you do', ['I can answer questions, provide information, and have casual conversations.']),
        (r'who created you', ['I was created by OpenAI using NLTK.']),
        (r'where are you from', ['I exist in the digital world, so I don’t have a physical location.']),
        (r'tell me a joke', ['Sure, here’s one: Why did the computer keep its drink on the windowsill? Because it wanted a cold drink!']),
        (r'how old are you', ['I don’t have an age. I’m just a computer program.']),
        (r'what is your purpose', ['My purpose is to assist and chat with users.']),
        (r'thank you', ['You’re welcome!', 'Anytime!', 'Glad I could help.']),
        (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a great day!']),
        ]
        return patterns

def main():
    nltk.download('punkt')
    root = tk.Tk()
    chat_gui = ChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
