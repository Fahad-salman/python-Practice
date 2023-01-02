def calculate(a):
    if '%' in a:
        z = a.split('%')
    res = float(z[0]) / 100 
    return float(res)

print(calculate('85%'))