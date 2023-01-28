from logic import *
P, Q, R = vars('p','Q' , 'R')
formula1 = ((P | Q) & ~P) >> Q
# formula1.print_truth_table()
print(formula1.is_tautology())
# formula1.is_contradiction()
# formula1.is_contingency()
# P & Q
# (P & Q).print_truth_table()
# P | Q
# (P | Q).print_truth_table()
# P >> Q
# (P >> Q).print_truth_table()
# P.iff(Q)
# P.iff(Q).print_truth_table()