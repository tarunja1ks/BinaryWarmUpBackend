from langdetect import detect, lang_detect_exception
from langdetect.lang_detect_exception import LangDetectException

def detect_language(text):
    try:
        detected_lang = detect(text)
        return detected_lang
    except LangDetectException as e:
        print(f"Error: {e}")
        return None

def main():
    print("Language Detection AI")
    print("Type 'exit' to quit.")

    while True:
        input_text = input("Enter text: ")
        if input_text.lower() == 'exit':
            break

        detected_language = detect_language(input_text)

        if detected_language:
            print(f"Detected language: {detected_language}")
        else:
            print("Language detection failed.")

if __name__ == "__main__":
    main()
