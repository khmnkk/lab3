from pack1.mod1 import TransLate,LangDetect,LanguageList,CodeLang

text = input("Write some text to translete #>> ")
lang = input("Write the language to translate to #>> ")
code = input("Write the name or the code of the language #>> ")
print("The program is working")
print(TransLate(text,lang))
print(LangDetect(text))
print(CodeLang(code))
print(LanguageList("screen",text))
