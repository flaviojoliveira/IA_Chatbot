from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Botzinho')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de computação?', 'Sim, eu programo em Python!', 'Amo tecnologia!', 'Como foi seu dia?' ]

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Botzinho: ', resposta)
    else:
        print('Botzinho: Ainda não sei responder esta pergunta')
