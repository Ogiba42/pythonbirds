class Pessoa:
    def cumprimentar(self):
        return 'Olá'

    def diga_oi(self):
        return 'Oi galera'

    def __init__(self, nome=None, idade=28):
        self.idade = idade
        self.nome = nome

if __name__ == '__main__':
    p = Pessoa('Giba')
    print(p.cumprimentar())
    print(p.diga_oi())
    print(p.nome)
    print(p.idade)