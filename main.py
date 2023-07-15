
numero_principal = int(input('Tabuada de: '))
print()
multiplicador = 1
multiplicador_limite = int(input('Multiplicador limite: '))
print()

for tabuada in range(multiplicador_limite):
  resultado = numero_principal * multiplicador
  print(f'{numero_principal} X {multiplicador} = {resultado}')
  multiplicador += 1
  