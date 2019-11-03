"" не знаю как это дело будет работать)
"" по идее должно первую букву каждого слова переводить в верхний регистр, а все остальные в нижний
"" шифт+ф10 чет не запускается в пайчарме

def capitalize_words(UserInput):
    result = []
    if type(UserInput) == str:
        UserInput = UserInput.title()
    result = UserInput.title();
    return result;



