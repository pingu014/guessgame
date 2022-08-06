import random
import math
lower = int(input("Insira o limite inferior:- "))

upper = int(input("Insira o limite superior:- "))

x = random.randint(lower, upper)
print("\n\tVocê só ",
       round(math.log(upper - lower + 1, 2)),
      " chances de adivinhar o inteiro!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Adivinhe um número:- "))

    if x == guess:
        print("Parabéns você fez isso em ",
              count, " tente")

        break
    elif x > guess:
        print("Você adivinhou muito pequeno!")
    elif x < guess:
        print("Você adivinhou muito alto!")

if count >= math.log(upper - lower + 1, 2):
    print("\nO número é %d" % x)
    print("\tMais sorte da próxima vez!")
