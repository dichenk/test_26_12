'''1'''
def to_camel_case(text):
    return re.split('_|-', text)[0] + ''.join([word.title() for word in re.split('_|-', text)[1:]])

'''2'''
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

'''3'''
count_bits = lambda: bin(n).count('1')
## в коде ничего не нужно исправлять

'''4'''
def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int ,str(n))))

'''5'''
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
