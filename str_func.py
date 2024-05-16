def str_upper(word):
    """Функция принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return word.upper()

def words_title(words_str):
    """Функция делает заглавными первые буквы каждого слова в строке,
       поступившей на вход функции."""
    return ' '.join([word.title() for word in words_str.split()])