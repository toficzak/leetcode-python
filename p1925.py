from math import sqrt


def triplets(n):
    result = 0
    for c in range(1, n + 1):
        for a in range(1, n + 1):
            count = c * c - a * a
            if count < 0:
                continue
            b = sqrt(count)
            # print(str(a) + "," + str(c) + ":" + str(b))

            if b > 0 and b.is_integer():
                # print(str(b))
                result += 1
    print(f"result: {result}")
    return result

if __name__ == '__main__':
    # triplets(5)
    triplets(10)
    # triplets(1000)
