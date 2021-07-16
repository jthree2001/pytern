from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

class Cortex:
  def __init__(self):
    # NOTE(Michael): Will need to create some sort of saving and loading funtionality if I want it to stay trained and have it's own mind
    self.chatbot = ChatBot('Pytern')

  def create_trainer():
    # Create a new trainer for the chatbot
    return self.trainer = ChatterBotCorpusTrainer(chatbot)

  def train(file_name):
    self.trainer.train(file_name)

  def input(text_input):
    self.chatbot.get_response(text_input)
  
  def repeat(text_input):
    # print("Python is " + x)