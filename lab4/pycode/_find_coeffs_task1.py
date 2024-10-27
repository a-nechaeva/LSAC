a = 1

for a_0 in range(-5, 5):
    for a_1 in range(-5, 5):
        for a_2 in range(-5, 5):
            if a_2 != 0:
                b = a_1 / a_2
                c = a_0 / a_2


                def _discr():
                    return (b ** 2 - 4 * a * c) ** 0.5


                x_1 = (-b - _discr()) / (2 * a)
                x_2 = (-b + _discr()) / (2 * a)

                if x_1.real > 0 or x_2.real > 0:
                    print("a_2 = ", a_2)
                    print("a_1 = ", a_1)
                    print("a_0 = ", a_0)
                    print("x_1 = ", x_1)
                    print("x_2 = ", x_2)
                    break
