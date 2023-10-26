# Data list seperti pada kegiatan 1 modul 1
random_list = [3.1, 2.7, 'Hello', 1, 'Python', 'world', 5.5, 4, 'AI']

# Filter untuk memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_to_units(num):
    units = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100)
    return {'ratusan': hundreds, 'puluhan': tens, 'satuan': units}

int_units = list(map(map_to_units, int_values))

# Output
print("Data Float:")
print(float_values)
print("Data Int:")
for unit in int_units:
    print(unit)
print("Data String:")
print(string_values)
