"""
COMP.CS.100 The Python program.
Creator: hassan2
Student id number: tuni.fi:H281750
"""

study_benefit = float (input ('Enter the amount of the study benefits: '))
benefit_raise = float (study_benefit + (study_benefit * 0.0117))
another_raise = float (benefit_raise + (benefit_raise * 0.0117))



txt = 'If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be {0} euros \nand if there was another index raise, the study \nbenefits would be as much as {1} euros'

print (txt.format (benefit_raise, another_raise))
