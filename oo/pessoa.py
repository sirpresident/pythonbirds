class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 5


if __name__ == '__main__':
    renzo = Mutante(nome='renzo')
    nixon = Pessoa(renzo, nome='Nixon')
    print(Pessoa.cumprimentar(nixon))
    print(id(nixon))
    print(nixon.cumprimentar())
    print(nixon.nome)
    print(nixon.idade)
    for filho in nixon.filhos:
        print(filho.nome)
    renzo.olhos = 1
    del renzo.olhos
    nixon.sobrenome = 'Azevedo'  # Criando atributo dinamico em tempo de execucao!
    print(nixon.sobrenome)
    del nixon.filhos
    print(nixon.__dict__) # os atributos de instancia ficam presentes no __dict__
    print(renzo.__dict__)
    print(nixon.sobrenome)
    print(Pessoa.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(nixon.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), renzo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), renzo.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Homem))
    print(isinstance(renzo, Pessoa))
    print(renzo.olhos)
# O metodo é uma função que pertence a uma classe, e portanto sempre está conectado a um objeto!