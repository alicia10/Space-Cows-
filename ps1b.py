###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
check = True
def spaceship_weights(egg_weights, memo):
    for i in egg_weights:
        memo[i] = {i:1}
    return memo
def cadena(suma, target_weight, memo):
    values = []
    second = []
    cadena = str(suma) + ' ('
    for i in memo[target_weight]:
            suma+= memo[target_weight][i]
            second.append(memo[target_weight][i])
            values.append(i)
    if len(values) == 1:
        cadena = str(second[0]) + ' (' + str(second[0]) + ' * ' + str(values[0]) + ' = ' + str(target_weight)+ ')'
        return cadena
    else:
        for i in range (len(values)):
            cadena += str(second[i]) + ' * ' + str(values[i]) + ' + '
    cadena = cadena[:-2]
    cadena += '= ' + str(target_weight) + ')'
    return cadena
def dp_make_weight(egg_weights, target_weight, memo):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here

    memo = spaceship_weights(egg_weights, memo)
    spaceship = {}
    suma=0
    
    try:
        valor = memo[target_weight]
        return cadena(suma, target_weight, memo)
    except:
        eggs = 0
        copy = target_weight
        while copy > 0:
            eggs = int(copy/max(egg_weights))
            if eggs >= 1:
                spaceship[max(egg_weights)] = eggs
                copy = copy%max(egg_weights)
                suma += eggs
            egg_weights = egg_weights[:-1]
            if copy in memo:
                for i in memo[copy]:
                    if i in spaceship:
                        spaceship[i] += memo[copy][i]
                    else:
                        spaceship[i]= memo[copy][i]
                    suma += memo[copy][i] 
                break
        memo[target_weight] = spaceship
        return cadena(suma, target_weight, memo)
    
# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    memo = {}
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n, memo))
    print()
