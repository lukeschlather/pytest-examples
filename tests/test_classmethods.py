class Base:
    def some_method():
        return "Base"

    @classmethod
    def class_method(cls,):
        return cls.some_method()


class Derived(Base):
    def some_method():
        return "Derived"


def test_derived_class_method():
    assert Derived.class_method() == "Derived"
