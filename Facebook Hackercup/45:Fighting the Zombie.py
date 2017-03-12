import math

def fact(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def combination(n,r):
    return fact(n)/(fact(n-r) * fact(r))

def comb(n,r):
    digit = n
    numerator = 1
    for _ in range(r):
        numerator *= digit
        digit -= 1
    denominator = fact(r)
    return  numerator//denominator
def hackercup():
    T = int(input())
    for i in range(T):
        H, S = input().split(" ")
        H = int(H)
        spells = input().split(" ")
        probabilities = []
        for spell in spells:
            add = False
            if '+' in spell:
                add = True
                spell = spell.split("+")
            else:
                spell = spell.split("-")
            spell = spell[0].split("d") + spell
            spell.pop(2)
            if len(spell) == 2:
                spell.append(0)
            for j in range(len(spell)):
                spell[j] = int(spell[j])
            if not add:
                spell[2] = -1 * spell[2]
            minimum_possible = 1 * spell[0] + spell[2]
            total_ways = math.pow(spell[1], spell[0])
            coeffs = expandPoly(spell[0], spell[1])
            res = 0
            if H-minimum_possible >=0:
                for j in coeffs[H-minimum_possible:]:
                    res += j
            probabilities.append(getProbability(res, total_ways))
        print("Case #" + str(i+1) + ": " + str(format(round(sorted(probabilities)[-1], 6), ".6f")))


def getProbability(num_of_success_ways, total_ways):
    return num_of_success_ways/int(total_ways)


def getCoeff(n, k, no_of_sides):

    if(k/no_of_sides >= 1):
        coefficient = 0
        for j in range(int(k/no_of_sides)+1):
            coefficient += (int(math.pow(-1, j)) * comb(n, j) * comb((n+k-1)-(no_of_sides*j), n-1))
    else:
        j = 0
        coefficient = (int(math.pow(-1, j)) * comb(n, j) * comb((n + k - 1) - (no_of_sides * j), n - 1))
    return coefficient

def expandPoly(dieRollCount, noOfSides):
    coefficients = []
    noOfCoefficients = (dieRollCount*(noOfSides - 1))+1
    coefficients.append(1)
    for i in range(1, noOfCoefficients):
        coefficients.append(int(getCoeff(dieRollCount, i, noOfSides)))
    return coefficients

if __name__ == '__main__':
    hackercup()