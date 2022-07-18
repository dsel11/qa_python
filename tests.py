from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_new_book('Библия')
        assert len(collector.get_books_rating()) == 1

    def test_default_rating_new_book_add(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        assert collector.get_book_rating('Библия') == 1

    def test_set_book_rating_in_collection(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.set_book_rating('Библия', 5)
        assert collector.get_book_rating('Библия') == 5

    def test_set_book_rating_in_collection_out_range(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.set_book_rating('Библия', 100)
        assert collector.get_book_rating('Библия') == 1

    def test_set_book_rating_not_in_collection(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.set_book_rating('Новый завет', 7)
        assert collector.get_book_rating('Новый завет') is None

    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_new_book('Ветхий завет')
        collector.set_book_rating('Библия', 5)
        assert len(collector.get_books_with_specific_rating(5)) == 1

    def test_get_books_with_specific_rating_out_range(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_new_book('Ветхий завет')
        collector.set_book_rating('Библия', 5)
        assert len(collector.get_books_with_specific_rating(100)) == 0

    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        assert len(collector.get_books_rating()) == 1

    def test_add_book_in_favorites_in_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_book_in_favorites('Библия')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_in_books_rating(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Библия')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_in_books_rating_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_book_in_favorites('Библия')
        collector.add_book_in_favorites('Библия')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_book_in_favorites('Библия')
        collector.delete_book_from_favorites('Библия')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_book_in_favorites('Библия')
        collector.delete_book_from_favorites('Новый завет')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        collector.add_book_in_favorites('Библия')
        collector.add_new_book('Новый завет')
        collector.add_book_in_favorites('Новый завет')
        assert len(collector.get_list_of_favorites_books()) == 2

    def test_get_list_of_favorites_books_no_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Библия')
        assert len(collector.get_list_of_favorites_books()) == 0

