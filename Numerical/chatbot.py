from chatterbot import chatbot
from chatterbot.trainers import ListTrainer

chatbot = Chatbot('Edureka')
trainer = ListTrainer(chatbot)
trainer.train(['hi, can I help you find a course', 'sure I'd love to find you a course', 'your course have been selected'])

response = chatbot.get_response("I want a course")
print(response)