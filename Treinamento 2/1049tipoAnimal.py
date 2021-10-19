vertebra = input()
especie = input()
alimentacao = input()


if vertebra == 'vertebrado' and especie == 'ave' and alimentacao == 'carnivoro':
    print('aguia')
elif vertebra == 'vertebrado' and especie == 'ave' and alimentacao == 'onivoro':
    print('pomba')
elif vertebra == 'vertebrado' and especie == 'mamifero' and alimentacao == 'onivoro':
    print('homem')
elif vertebra == 'vertebrado' and especie == 'mamifero' and alimentacao == 'herbivoro':
    print('vaca')

elif vertebra == 'invertebrado' and especie == 'inseto' and alimentacao == 'hematofago':
    print('pulga')
elif vertebra == 'invertebrado' and especie == 'inseto' and alimentacao == 'herbivoro':
    print('lagarta')
elif vertebra == 'invertebrado' and especie == 'anelideo' and alimentacao == 'hematofago':
    print('sanguessuga')
elif vertebra == 'invertebrado' and especie == 'anelideo' and alimentacao == 'onivoro':
    print('minhoca')   