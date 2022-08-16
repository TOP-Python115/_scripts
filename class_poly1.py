# DRY — Don't Repeat Yourself — Не Повторяйся

class Place:
    """Базовый класс для жилых помещений"""
    def __init__(self, name: str, 
                       area: float) -> None:
        self.name = name
        self.area = area
    
    def __str__(self) -> str:
        return (f"Объект {self.__class__.__name__}:\n"
                f"{self.name}\n"
                f"Площадь: {self.area:.2f} кв.м")

class Room(Place):
    """Реализация комнаты"""
    pass

class Apartment(Place):
    """Реализация квартиры"""
    def __init__(self, name: str, 
                       area: float, 
                       rooms: int) -> None:
        super().__init__(name, area)
        self.rooms = rooms
    
    def __str__(self) -> str:
        return (f"Объект {self.__class__.__name__}:\n"
                f"{self.rooms} комнат\n"
                f"{self.name}\n"
                f"Площадь: {self.area:.2f} кв.м")

class House(Place):
    """Реализация дома"""
    def __init__(self, name: str, 
                       area: float, 
                       floors: int,
                       rooms: int) -> None:
        super().__init__(name, area)
        self.floors = floors
        self.rooms = rooms

    def __str__(self) -> str:
        return (f"Объект {self.__class__.__name__}:\n"
                f"{self.floors} этажей, "
                f"{self.rooms} комнат\n"
                f"{self.name}\n"
                f"Площадь: {self.area:.2f} кв.м")


places = (
    Room('Комната с видом на парк', 12.5),
    Room('Чулан под лестницей', 2.34),
    Room('Мансарда', 20.8),
    Apartment('Квартира в спальном районе', 60.1, 2),
    Apartment('Бывший барак', 54.2, 3),
    Apartment('Центральная', 101.0, 4),
    House('Домик в деревне', 80, 2, 1),
    House('Круглогодичный коттедж', 140.5, 4, 2),
    House('Особняк в стиле ретро', 300, 7, 3),
)

for place in places:
    print('='*30)
    print(place.__str__(), end='\n\n')
