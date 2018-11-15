import numpy as np

def coin_em(flipSets, thetaA=None, thetaB=None, iterate=10):
    thetaA = thetaA
    thetaB = thetaB
    thetas = [(thetaA, thetaB)]

    for c in range(iterate):
        print("%d::\t%0.2f %0.2f" % (c, thetaA, thetaB))
        headsA, tailsA, headsB, tailsB = eStep(flipSets, thetaA, thetaB)
        thetaA, thetaB = mStep(headsA, tailsA, headsB, tailsB)

    thetas.append((thetaA,thetaB))
    return thetas, (thetaA,thetaB)

def eStep(flipSets, thetaA, thetaB):
    headsA, tailsA = 0,0
    headsB, tailsB = 0,0
    for trial in flipSets:
        likelihood_A = coinLikelihood(trial, thetaA)
        likelihood_B = coinLikelihood(trial, thetaB)
        p_A = likelihood_A / (likelihood_A + likelihood_B)
        p_B = likelihood_B / (likelihood_A + likelihood_B)
        headsA += p_A * trial.count("H")
        tailsA += p_A * trial.count("T")
        headsB += p_B * trial.count("H")
        tailsB += p_B * trial.count("T")

    return headsA, tailsA, headsB, tailsB

def mStep(headsA, tailsA, headsB, tailsB):

    thetaA = headsA / (headsA + tailsA)
    thetaB = headsB / (headsB + tailsB)
    return thetaA, thetaB

def coinLikelihood(roll, bias):

    numHeads = roll.count("H")
    flips = len(roll)
    return pow(bias, numHeads) * pow(1-bias, flips-numHeads)


def main():
    flipSets = ["HTTTHHTHTH", "HHHHTHHHHH", "HTHHHHHTHH", "HTHTTTHHTT", "THHHTHHHTH"]

    print("the set of coin flips is as follows: HTTTHHTHTH HHHHTHHHHH HTHHHHHTHH HTHTTTHHTT THHHTHHHTH" )
    theta1 = input("input likelihood for coin a, values ranging from 0 to 1 \n")
    theta2 = input("input likelihood for coin b, values ranging from 0 to 1 \n")

    coin_em(flipSets, float(theta1), float(theta2), iterate =10)

main()
