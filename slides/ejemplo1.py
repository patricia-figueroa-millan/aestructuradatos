import timeit

n = 100000000

tiempo_append = timeit.timeit(
    "datos.append(0)",
    setup=f"datos = list(range({n}))",
    number=1000
)

tiempo_insert = timeit.timeit(
    "datos.insert(0, 0)",
    setup=f"datos = list(range({n}))",
    number=1000
)

print(f"append:    {tiempo_append:.6f} s")
print(f"insert(0): {tiempo_insert:.6f} s")