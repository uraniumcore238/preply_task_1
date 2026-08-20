class Foo:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]



class Bar(Foo): # Must be a singleton as well
    ...

class Baz(Bar): # Must be a singleton as well
    ...

foo1 = Foo()
foo2 = Foo()

print(f"foo1: {foo1}")
print(f"foo2: {foo2}")

print(f"id(foo1): {id(foo1)}")
print(f"id(foo2): {id(foo2)}")

print(f"Один объект: {foo1 is foo2}")

print()


bar1 = Bar()
bar2 = Bar()

print(f"bar1: {bar1}")
print(f"bar2: {bar2}")
print(f"id(bar1): {id(bar1)}")
print(f"id(bar2): {id(bar2)}")
print(f"Один объект Bar: {bar1 is bar2}")

print()


baz1 = Baz()
baz2 = Baz()

print(f"baz1: {baz1}")
print(f"baz2: {baz2}")
print(f"id(baz1): {id(baz1)}")
print(f"id(baz2): {id(baz2)}")
print(f"Один объект Baz: {baz1 is baz2}")