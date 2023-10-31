def fahrenheit():
    print("Celsius \t\tFahrenheit equivalents")
    for index in range(100):
        fah = (9 / 5) * index + 32
        print(f'{index:}{fah:>20.0f}')


print(fahrenheit())