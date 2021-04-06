"""
@copyright Copyright (c) 2021 Shamus_Rezol <shamus.rezol@mail.ru>. All rights reserved.
MIT License
"""
from .tokens import *

class FParser(object):
    """Парсер строк аргументов.
    """

    def __init__(self, arguments: str):
        self._tokens = list()

        self.data = arguments
        self.index = -1
        self.char = None
        if len(arguments) != 0:
            self.advance()
            self._parse()
            self._dispose()

    def advance(self, n: int=1):
        """Продвижение вперед.

        Продвигает переменные вперед; переход к следующему символу.

        @param n На сколько символов продвинуться.
        """
        self.index += n

        if self.index >= 0 and self.index < len(self.data):
            self.char = self.data[self.index]
        else:
            self.char = None

    def eat(self, victim: str):
        """Поедает ключевую фразу.

        Если ожидаемая и фактическая фраза расходятся, то вызывается
        синтаксическое исключение.
        """
        for char in victim:
            if self.char != char:
                raise SyntaxError("Unexcepted syntax error.")
            self.advance()

    def peek(self):
        """Предпросмотр следующего символа.

        @return Возвращает следующий символ или None.
        """
        self.advance()
        ch = self.char
        self.advance(-1)
        return ch

    def parse_by_condition(self, condition):
        """Получает ключевую фразу.

        Ключевая фраза состоит из любых символов, добавляемых, если
        функция condition возвращает истину (True).

        Пример использования смотрите в коде FParser.parse_keyword.

        @param condition Функция-условие, отвечающая за остановку ключевой фразы. Для этого должна вернуть False.

        @return Возвращает ключевую фразу.
        """
        keyword = str()
        while self.char != None and condition() == True:
            keyword += self.char
            self.advance()
        return keyword

    def parse_keyword(self):
        """Получает ключевое слово.

        @return Возвращает ключевое слово.
        """
        def _():
            return not self.char.isspace()
        return self.parse_by_condition(_)

    def _parse(self):
        while self.char != None:
            index = self.index
            for token_cls in FToken._childs:
                if token_cls.can_parse(self):
                    self._tokens.append(token_cls.parse(self))
                    break;
            if index == self.index:
                '''
                Что произошло?
                 - был вызван token_cls.parse, но он ни шиша не сделал.
                 - ни один token_cls.can_parse не вернул True.
                Что делать?
                 - Вызовем абстрактное исключение лексирования.
                '''
                print(self._tokens)
                raise SyntaxError(f"Неверный синтаксис на позиции {self.index + 1}")

    def _dispose(self):
        self.index = None
        self.char  = None
        self.data  = None
        # Примечание: self._tokens удаляется при getter'е свойства result.

    @property
    def result(self):
        """Выдает результат лексирования.

        Анализирует полученные токены и превращает их в конечный результат.
        """
        if '_result' in dir(self):
            return self._result
        result = list()
        require_param = False
        for token in self._tokens:
            if token == None:
                continue # whitespaces и другой мусор.

            if require_param == True:
                if not isinstance(token, FTParam):
                    break # Go to raise
                result[len(result) - 1].append(token.value)
                require_param = False
                continue

            if isinstance(token, FTParam):
                result.append(token.value)
            elif isinstance(token, (FTBigFlag, FTFlag)):
                if token.value in ("w", "Num"):
                    result.append([str(token), ])
                    require_param = True
                else:
                    result.append(str(token))
            else:
                '''
                Программист добавил токены, но не добавил способ их
                обработки в конечный результат.
                '''
                raise NotImplementedError()
        if require_param == True:
            raise Exception("Флаг с параметром не имеет параметра.")

        _tokens = None
        self._result = result
        return result