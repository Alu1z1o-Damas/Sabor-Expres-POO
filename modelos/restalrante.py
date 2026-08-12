class Restaurantes:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurantes()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurantes()

restaurantes = [restaurante_praca, restaurante_pizza]

print(vars(restaurante_praca))