class Pessoa:
    olhos = 2 # atributo default (ou atributo de classe)

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod # para acessar dados da própria classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

# Criação da Herança, herdar todos os atributos da classe Pai
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar() # Sobrescrita de Método
        return f'{cumprimentar_da_classe}. Aperto de mão'

    # super() - vai acessar os elementos da classe Pai de Homem.

class Mutante(Pessoa):
    olhos = 3 # Sobrescrita de Atributo (classes filhas podem sobrescrever atributos de classes pai)


if __name__ == '__main__':
    eduardo = Mutante(nome='Eduardo')
    luciano = Homem(eduardo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho' # criação do atributo dinâmico
    del luciano.filhos # remover o atributo filhos
    luciano.olhos = 1
    del luciano.olhos
    print(eduardo.__dict__) # atributos de instância __dict__ de um objeto
    print(luciano.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(eduardo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(eduardo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa ('Anonimo')
    print(isinstance(pessoa, Pessoa)) # Objeto Pessoa eh do tipo pessoa?
    print(isinstance(pessoa, Homem)) # A pessoa eh um Homem?
    print(isinstance(eduardo, Pessoa)) # eduardo pertence ao tipo Pessoa
    print(isinstance(eduardo, Homem)) # eduardo eh do tipo Homem
    print(eduardo.olhos)
    print(luciano.cumprimentar())
    print(eduardo.cumprimentar())