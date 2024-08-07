from inspect import isgenerator

# використовуємо умову для завершення генератора
def generate_cube_numbers(end):
    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            return
        yield cube
        n += 1

# тестуємо функцію
def test_generate_cube_numbers():
    gen = generate_cube_numbers(1)
    assert isgenerator(gen), 'test0:gen should be a generator'
    assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
    assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
    assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'


test_generate_cube_numbers()

print("all done")
