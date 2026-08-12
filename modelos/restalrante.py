class Restaurantes:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = nome
        self.ativo = False

restaurante_praca = Restaurantes('Praça', 'Gourmet')
restaurante_pizza = Restaurantes('Pizza Express', 'Italiano')

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))
print(vars(restaurante_pizza))