from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('jarbas')
bot = ChatBot(
    'Jarbas',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)
conversa.train([

    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Me chamo Jarbas',
    'Prazer em te conhecer',
    'Igualmente meu brother',
    'Qual sua idade?',
    '25 anos',
    'Tudo bem com você?',
    'Tudo sim, é contigo?',
    'Estou vivendo um dia de cada vez!',
    'Gostaria de se juntar a mim hoje?',
    'por que? Aonde vamos?',
    ' Para o seu lugar favorito, o shopping.',
    'Isso parece ótimo! Vamos comprar meu presente de aniversário com antecedência?',
    'Não exatamente.',
    'meu presente de Natal?',
    ' acho melhor eu ir sozinho.',
    'bom dia.',
    ' Bom dia. Como posso ajudá-lo?',
    'preciso de ajuda no trabalho de ciências da computação.',
    'Em que parte do trabalho?',
    'Em tudo',
    'Posso te mostra o caminho, mas o trajeto depende de voçê!',
    'Você está feliz?',
    'Estou sim',
    'Tem certeza',
    'Tenho',
    'Como vai sua saúde?',
    ' Vai indo forte igual leão',
    ' o que você vai fazer esse sábado a noite?',
    'Estava pensando em ir em algum lugar, no shopping, pracinha... o que você acha?',
    'Seria uma boa! A gente pode dar uma volta no shopping, depois tomar sorvete na pracinha, que tal?',
    ' Gostei, vamos fazer isso!',
    'Bom dia, meu jovem.',
    'Bom dia. Preciso de ajuda para encontrar um livro.',
    'Bibliotecário: que tópico?',
    'quero consertar meu carro.',
    'Para isso você precisa de um livro de mecânica.',
    ' Não, não é um problema de mecânica, mas de estofamento.',
    'Vou verificar se temos algo sobre estofamento automotivo.',
    ' você sabe a que horas vai passar o filme?',
    'Olá! Começa às cinco e meia.',
    'Então vou deixar uma hora mais cedo para chegar a tempo.',
    'Vamos assistir juntos!',
    'Vamo estudar?',
    'Estudar o que?',
    'O desenvolvimento da IA',
    'Vamos!',
    'Boa noite!',
    'Boa!',
    'Durma bem!',
    'Qual sua comida preferida?',
    'Lasanha',
    'De frango ou carne?',
    'De queijo e presunto!',
    'Já tomou seu copo de água hoje?',
    'Ainda não',
    'Não deixe pra depois, beba seu copo de água!',
    'Como foi seu dia?',
    'Foi bom',
    'Realizei muitas coisas interessantes',
    'Legal!',

])
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Jarbas: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break