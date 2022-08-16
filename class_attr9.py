class Cat:
    TOTAL_CATS = 0
    
    @classmethod
    def cats(cls):
        print(f"У нас {cls.TOTAL_CATS} кошек!")
    
    def __init__(self, name=''):
        print('Родилась кошка!')
        if not name:
            name = input('Как назовём?\n')
        self.name = name
        self.__class__.TOTAL_CATS += 1
     
    def __del__(self):
        self.__class__.TOTAL_CATS -= 1
    
    def __str__(self):
        return f"Кошка по имени {self.name}"
    

cat1 = Cat('Багира')

# вызов классового метода от объекта класса
Cat.cats()
# вызов классового метода от объекта экземпляра
cat1.cats()
