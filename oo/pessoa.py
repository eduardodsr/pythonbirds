class Pessoa:
    olhos = 2 # atributo default (ou atributo de classe)

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod # para acessar dados da própria classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    eduardo = Pessoa(nome='Eduardo')
    luciano = Pessoa(eduardo, nome='Luciano')
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
    print(luciano.__dict__) # atributos de instância __dict__ de um objeto
    print(eduardo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(eduardo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(eduardo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
