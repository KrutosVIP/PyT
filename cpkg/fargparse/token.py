"""
@copyright Copyright (c) 2021 Shamus_Rezol <shamus.rezol@mail.ru>. All rights reserved.
MIT License
"""
class FToken(object):
    """Единица лексического разбора; абстрактный базовый класс.

    Токен имеет свой тип T, по которому его можно идентифицировать, и
    свое значение value.

    Для использования вам необходимо определить класс токена и как
    параметр передать его тип.

    class MyToken(FToken, type="MyType"):
    
    В этом классе необходимо переопределить статические методы can_parse
    и parse, принимающие один аргумент - экземпляр FParser.

    Метод can_parse всех дочерник классов будут вызываться в том порядке,
    в котором эти классы объявлены. Например, в следующем примере класс
    TEXT никогда не признается токеном.

    class MyToken(FToken, type="MyType"):
        @staticmethod
        def can_parse(parser):
            return True
        // ...
        
    class TEXT(FToken, type="text"):
        // ...
    """
    T = "unknown"

    def __init__(self, value=None):
        """Конструктор.

        @param value Какое угодно значение токена.
        """
        self.value = value

    def __str__(self):
        """Возвращает интерпретацию токена как строку."""
        return self.T

    _childs = list()
    def __init_subclass__(cls, type: str="unknown"):
        """Инициализирует и регистрирует наследников."""
        super().__init_subclass__()
        cls.T = type
        cls._childs.append(cls)

    @staticmethod
    def can_parse(parser):
        """Проверяет, возможно ли пролексировать этот токен.
        
        @param parser Экземпляр FParser.
        @return Возвращает True, если возможно; иначе, False.
        """
        return False

    @classmethod
    def parse(cls, parser):
        """Лексирует этот токен
@param parser Экземпляр FParser.
        @return Возвращает полученный токен или None.
        """
        raise NotImplementedError()
