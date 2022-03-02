'''01- Exercicios Equação de  primeiro grau 
Para calcular as raízes de uma equação de segundo grau, siga as instruções abaixo:
1. Peça que o usuário digite o valor dos coeficientes do polinômio (a, b, c) e armazene-os em variáveis;
2. Crie uma função que receba os três coeficientes do polinômio e retorne:
2.1. Duas raízes reais, caso o Delta seja maior do que zero
2.2. Uma raiz real, caso o Delta seja igual a zero
2.3. Duas raízes complexas, caso o Delta seja menor do que zero
3. Ao retornar essas raízes, imprima-as no console;
4. Ao imprimir na tela, pergunte se o usuário deseja continuar;
5. Caso o usuário deseje continuar, retorne ao passo 1;
6. Caso o usuário não deseje continuar, envie uma mensagem ao usuário e encerre o programa '''

# Resolução

print('Digite três valores para o coeficientes do polinômio')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
