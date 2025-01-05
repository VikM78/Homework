from fake_math import divide as fake_div
import true_math as tm

result1 = fake_div(69, 3)
result2 = fake_div(3, 0)
result3 = tm.divide(49, 7)
result4 = tm.divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)