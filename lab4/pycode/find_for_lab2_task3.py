

for a_1 in range(-5, 5):
    for a_2 in range(-5, 5):
        for c_1 in range(-5, 5):
            for c_2 in range(-5, 5):
                if (a_1 * c_1 + a_2 * c_2 == 0) and (a_2 * c_1 - a_1 * c_2 == 1):
                    print(a_1)
                    print(a_2)
                    print(c_1)
                    print(c_2)