medida = float(input('Digite uma distancia em Metros:'))
cm = medida * 100
mm = medida * 1000
mt = medida * 1 #Teste erro
print('A medida de {:.0f} metros corresponde a: \n{:.0f} Centimetros \n{:.0f} milimetros: e\n{:.0f} metros'.format(medida, cm, mm, mt))