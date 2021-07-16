from .app.cortex import Cortex

def main():
  cortex = Cortex.new()
  while True:
    request = raw_input("^^: ")
    response = str(chatbot.get_response(request))
    print("Bot: " + response)
try:
  print("Welcome")
  main()
except KeyboardInterrupt:
  print("Program Interrupted")