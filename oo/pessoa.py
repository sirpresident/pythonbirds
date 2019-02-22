class Pessoa:
    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='renzo')
    nixon = Pessoa(renzo, nome='Nixon')
    print(Pessoa.cumprimentar(nixon))
    print(id(nixon))
    print(nixon.cumprimentar())
    print(nixon.nome)
    print(nixon.idade)
    for filho in nixon.filhos:
        print(filho.nome)
