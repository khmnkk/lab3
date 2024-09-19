import googletrans
from tabulate import tabulate

available_languages = googletrans.LANGUAGES
google_translator = googletrans.Translator()

def TransLate(src: str, lang: str) -> str:
    result = google_translator.translate(src, dest=lang)
    return result.text

def LangDetect(txt: str) -> str:
    detection = google_translator.detect(txt)
    return detection.lang

def CodeLang(code: str) -> str:
    for language_code, language_name in available_languages.items():
        if code == language_name:
            return f"The language code is - {language_code}"
        elif code == language_code:
            return f"The language name is - {language_name}"
    return "Language not found"

def LanguageList(out: str = "screen", text: str = "") -> str:
    table_data = []
    for index, (language_code, language_name) in enumerate(available_languages.items(), start=1):
        translated_text = TransLate(text, language_code) if text else ""
        table_data.append([index, language_name, language_code, translated_text])

    headers = ["N", "Language", "ISO-639 code"]
    if text:
        headers.append("Text")

    # Форматована таблиця
    table_str = tabulate(table_data, headers, tablefmt="plain", numalign="left", stralign="left")

    if out == "screen":
        print(table_str)
    elif out == "file":
        with open("languages_list.txt", "w", encoding="utf-8") as file_handle:
            file_handle.write(table_str)
    else:
        return "Error: Unsupported output option"

    return "Ok"
