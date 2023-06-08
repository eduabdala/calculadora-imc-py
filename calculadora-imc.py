def calcular_imc(peso, altura):
  altura_metros = altura / 100  # Converter altura para metros
  imc = peso / (altura_metros ** 2)
  return imc

def nivel_imc(imc):
  if imc < 18.5:
    return "Abaixo do peso"
  elif imc < 25:
    return "Peso normal"
  elif imc < 30:
    return "Sobrepeso"
  elif imc < 35:
    return "Obesidade Grau 1"
  elif imc < 40:
    return "Obesidade Grau 2"
  else:
    return "Obesidade Grau 3"

peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em centímetros: "))

imc = calcular_imc(peso, altura)
nivel = nivel_imc(imc)

print("Seu IMC é: {:.2f}".format(imc))
print("Nível de IMC: ", nivel)
