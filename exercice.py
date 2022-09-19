#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return number * -1 if number < 0 else number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    return [pre + suffixe for pre in prefixes]


def prime_integer_summation() -> int:
    primes = [2, 3, 5]
    n = 6
    while len(primes) < 100:
        is_prime = True
        for i in range(2, n//2):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
        n += 1
    return sum(primes)

def factorial(number: int) -> int:
    result = number
    for i in range(number-1, 0, -1):
        result *= i
    return result

def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    result = []
    for group in groups:
        if len(group) <= 3 or len(group) >= 10:
            result.append(False)
            continue
        elif 25 in group:
            result.append(True)
            continue
        else:
            for element in group:
                if element > 70:
                    if 50 in group:
                        result.append(False)
                        break
                    else:
                        result.append(True)
                elif element < 18:
                    result.append(False)
                    break
                elif element == group[-1]:
                    result.append(True)


    return result


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]

    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

