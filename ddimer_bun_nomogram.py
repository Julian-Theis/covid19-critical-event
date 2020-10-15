"""
This is an implementation of the nomogram described in:
    Cheng, Anying, Liu Hu, Yiru Wang, Luyan Huang, Lingxi Zhao, Congcong Zhang, Xiyue Liu et al. "Diagnostic performance of initial blood urea nitrogen combined with D-dimer levels for predicting in-hospital mortality in COVID-19 patients." International journal of antimicrobial agents 56, no. 3 (2020): 106110.

Author: Julian Theis
Date: 10/15/2020
"""

def calculuate_mort_risk(age, dimer, bun):
    points = 0
    if bun > 30:
        points += 100
    elif bun > 0:
        points += (bun/30)*100

    if dimer > 60:
        points += 95
    elif dimer > 0:
        points += (dimer/60)*95

    if age > 90:
        points += 20.323
    elif age > 20:
        points += (age - 20)/(90-20) * 20.323

    """ 
    Points to Mortality Probability Mapping:
    25.285 --> 0.05
    30.570 --> 0.1
    36.270 --> 0.2
    40.104 --> 0.3
    43.316 --> 0.4
    46.114 --> 0.5
    49.016 --> 0.6
    52.124 --> 0.7
    55.855 --> 0.8
    61.762 --> 0.9
    66.943 --> 0.95
    """
    points = points / 10
    if points > 6.6943:
        prob = 0.95
    elif points < 2.5285:
        prob = 0.05
    else:
        prob = -0.0265*(points**3) + 0.3674*(points**2) - 1.3653*points + 1.5874
    return prob

if __name__ == "__main__":
    prob = calculuate_mort_risk(age=45, dimer=0.95, bun=10)