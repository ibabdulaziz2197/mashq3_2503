# 10

a = lambda n: "5 ga karrali" if n % 5 == 0 else "5 ga karrali emas"

res = a(10)
print(res)


# 11

a = lambda a, b, c: "Birinchi son eng katta" if a > b and a > c else ("Ikkinchi son eng katta" if b > a and b > c else "Uchinchi son eng katta yoki teng")

res = a(11, 22, 25)
print(res)


# 12
a = lambda age: "adult" if age > 18 else "minor"

res = a(10)
print(res)

# 13
a = lambda n: "positive" if n > 0 else "negative"

res = a(22)
print(res)

# 15
a = lambda a, b: a if abs(a - 10) < abs(b - 10) else b

res = a(10,5)
print(res)

# 16
f = lambda x: x * 2 if x > 50 else x / 2

res = f(5)
print(res)

# 17
f = lambda x: x + 2 if x % 2 == 0 else x - 1

res = f(4)
print(res)

# 18

check_sum = lambda a, b: "Katta" if (a + b) > 100 else "Kichik yoki teng"

res = check_sum(22, 223)
print(res)


# 19
check_even = lambda n: "yes" if n % 2 == 0 else "no"

res = check_even(3)
print(res)

# 20

div_check = lambda x: "Ha" if (x % 3 == 0) ^ (x % 5 == 0) else "Yo'q"

res = div_check(55)
print(res)
