class Tree:
    """Фабрика."""

    class Oak:
        pass

    class Pine:
        pass

    class Maple:
        pass

    @classmethod
    def get_tree(cls, kind: str):
        return cls.__dict__[kind.title()]()


t1 = Tree.get_tree('oak')
print(t1)
t2 = Tree.get_tree('maple')
print(t2)
