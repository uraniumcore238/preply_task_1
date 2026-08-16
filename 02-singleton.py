class Foo:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

class Bar(Foo): # Must be a singleton as well
    ...

class Baz(Bar): # Must be a singleton as well
    ...