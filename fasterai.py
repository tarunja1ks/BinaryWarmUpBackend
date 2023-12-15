import langid

def language_detector(text):
    lang, _ = langid.classify(text)
    return lang

if __name__ == "__main__":
    while True:
        input_text = input("Enter text (or type 'exit' to quit): ")
        if input_text.lower() == 'exit':
            break

        detected_language = language_detector(input_text)
        print(f"Detected language: {detected_language}")
