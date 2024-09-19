from deep_translator import GoogleTranslator
from langdetect import detect
from tabulate import tabulate

# Створюємо екземпляр перекладача
trans = GoogleTranslator(source='auto', target='en')

# Отримуємо список підтримуваних мов через екземпляр
supported_languages = trans.get_supported_languages(as_dict=True)

def TransLate(source_text: str, target_language: str) -> str:
    translation_result = GoogleTranslator(source='auto', target=target_language).translate(source_text)
    return translation_result

def LangDetect(text: str) -> str:
    detected_language = detect(text)
    return detected_language

def CodeLang(language_code: str) -> str:
    for code, name in supported_languages.items():
        if language_code == name:
            return f"The language code is - {code}"
        elif language_code == code:
            return f"The language name is - {name}"
    return "Language not found"

def LanguageList(output: str = "screen", input_text: str = "") -> str:
    table_rows = []
    for index, (code, name) in enumerate(supported_languages.items(), start=1):
        translated_text = TransLate(input_text, code) if input_text else ""
        table_rows.append([index, name, code, translated_text])

    headers = ["N", "Language", "ISO-639 code"]
    if input_text:
        headers.append("Text")

    table_string = tabulate(table_rows, headers, tablefmt="plain", numalign="left", stralign="left")

    if output == "screen":
        print(table_string)
    elif output == "file":
        with open("languages_list.txt", "w", encoding="utf-8") as file_handle:
            file_handle.write(table_string)
    else:
        return "Error: Unsupported output option"

    return "Ok"
