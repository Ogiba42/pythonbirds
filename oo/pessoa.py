class Pessoa:
    def cumprimentar(self):
        return 'Olá'

    def diga_oi(self):
        return 'Oi galera'

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

if __name__ == '__main__':
    gilberto = Pessoa(nome='Giba')
    sophia = Pessoa(gilberto, nome='Sophia')
    print(gilberto.nome)
    print(gilberto.idade)
    for filho in sophia.filhos:
        print(filho.nome)

    print(sophia.nome)