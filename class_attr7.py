class Cat:
    TOTAL_CATS = 0
    
    def __init__(self, name=''):
        print('Родилась кошка!')
        if not name:
            name = input('Как назовём?\n')
        self.name = name
        Cat.TOTAL_CATS += 1
     
    def __del__(self):
        Cat.TOTAL_CATS -= 1
    
    def __str__(self):
        return f"Кошка по имени {self.name}"
    

cat1 = Cat('Багира')
cat2 = Cat('Мурзик')
print(Cat.TOTAL_CATS, end='\n\n')

del cat1
print(Cat.TOTAL_CATS)
