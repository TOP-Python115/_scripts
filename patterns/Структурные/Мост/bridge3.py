from abc import ABC, abstractmethod


class Website(ABC):
    def __init__(self, implementation):
        self._implementation = implementation

    def __str__(self):
        return 'User category: {}, Implementation: {}'.format(
            self.__class__.__name__,
            self._implementation.__class__.__name__
        )

    @abstractmethod
    def show_page(self):
        pass


class FreeUser(Website):
    def show_page(self):
        ads = self._implementation.get_ads()
        text = self._implementation.get_excerpts()
        action = self._implementation.call_to_action()
        print(ads, text, action, sep='\n', end='\n\n')


class PaidUser(Website):
    def show_page(self):
        text = self._implementation.get_article()
        print(text, end='\n\n')


class Implementation(ABC):
    @staticmethod
    def get_ads():
        return 'advertise'

    @staticmethod
    def get_excerpts():
        return 'part of the article'

    @staticmethod
    def get_article():
        return """Title
        Full text of the article.
        Date. Signature."""

    @staticmethod
    @abstractmethod
    def call_to_action():
        pass

class RandomArticle(Implementation):
    @staticmethod
    def get_excerpts():
        return 'part of a random article'

    @staticmethod
    def call_to_action():
        return 'Pay $10 for a subscription to get rid of ads.'

class Article(Implementation):
    @staticmethod
    def call_to_action():
        return 'If you want to remove ads you can use the subscription for only $10 monthly.'


page1_free = FreeUser(Article())
page1_paid = PaidUser(Article())
page2_free = FreeUser(RandomArticle())
page2_paid = PaidUser(RandomArticle())

print(page1_free)
page1_free.show_page()

print(page1_paid)
page1_paid.show_page()

print(page2_free)
page2_free.show_page()

print(page2_paid)
page2_paid.show_page()
