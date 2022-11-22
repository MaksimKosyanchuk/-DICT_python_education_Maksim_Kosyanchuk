"""simplified markdown editor"""


class Markdown:
    """main class"""
    HELP_TEXT = """    Available formatters: plain bold italic header link inline-code ordered-list 
    unordered-list new-line
    Special commands: !help !done"""

    def __init__(self):
        self.main_text = ""

    def my_input(self) -> bool:
        """Возвращает False если надо завершить прогамму"""
        user_choice = input("Choose a formatter: > ")
        match user_choice.lower():
            case "!done":
                self.write_file(self.main_text)
                return False
            case "!help":
                print(self.HELP_TEXT)
            case "header":
                self.main_text += self.header_editing() + "\n"
            case "plain":
                self.main_text += self.plain_editing() + "\n"
            case "new-line":
                self.main_text += "\n"
            case "link":
                self.main_text += self.link_editing() + "\n"
            case "bold":
                self.main_text += self.bold_editing() + "\n"
            case "italic":
                self.main_text += self.italic_editing() + "\n"
            case "inline-code":
                self.main_text += self.code_editing() + "\n"
            case "ordered-list":
                self.main_text += self.ordered_editing() + "\n"
            case "unordered-list":
                self.main_text += self.unordered_editing()
            case _:
                print("Unknown formatting type or command")
        return True

    @staticmethod
    def unordered_editing() -> str:
        """Создает и возвращает строку unordered-list"""
        while True:
            rows_count = input("Number of rows: > ")
            try:
                rows_count = int(rows_count)
            except ValueError:
                print("Enter a integer")
                continue
            if rows_count in range(1, 11):
                text = ""
                for index in range(rows_count):
                    text += "- " + input(f"Row #{index + 1}: > ") + "\n"
                return text
            print("The number of rows should be greater than zero and smaller than 11.")

    @staticmethod
    def ordered_editing() -> str:
        """Создает и возвращает строку ordered-list"""
        while True:
            rows_count = input("Number of rows: > ")
            try:
                rows_count = int(rows_count)
            except ValueError:
                print("Enter a integer")
                continue
            if rows_count in range(1, 11):
                text = ""
                for index in range(rows_count):
                    text += str(index + 1) + ". " + input(f"Row #{index + 1}: > ") + "\n"
                return text
            print("The number of rows should be greater than zero and smaller than 11.")

    @staticmethod
    def code_editing() -> str:
        """Создает и возвращает строку inline-code"""
        text = input("Text: > ")
        return f"`{text}`"

    @staticmethod
    def italic_editing() -> str:
        """Создает и возвращает строку italic"""
        text = input("Text: > ")
        return f"*{text}*"

    @staticmethod
    def bold_editing() -> str:
        """Создает и возвращает строку bold"""
        text = input("Text: > ")
        return f"**{text}**"

    @staticmethod
    def link_editing() -> str:
        """Создает и возвращает строку с ссылкой"""
        label = input("Label: > ")
        link = input("URL: > ")
        return f"[{label}]({link})"

    @staticmethod
    def plain_editing() -> str:
        """Создает и возвращает строку c обчным текстом"""
        text = input("Text: > ")
        return text

    @staticmethod
    def header_editing() -> str:
        """Создает и возвращает строку header"""
        while True:
            header_lvl = input("Level: > ")
            try:
                header_lvl = int(header_lvl)
            except ValueError:
                print("Type a integer!")
            else:
                if header_lvl in range(1, 7):
                    user_text = ""
                    for index in range(header_lvl):
                        user_text += "#"
                    user_text += " " + input("Text: > ")
                    return user_text
                print("Header has 1-6 levels!")

    @staticmethod
    def write_file(text):
        """Сохраняет self.main_text в файл outpud.md, ничего не возвращает"""
        with open("output.md", "w") as file:
            file.write(text)
            file.close()


def main():
    """main func,ничего не возврвщает"""
    markdown = Markdown()
    iterator = True
    while iterator:
        iterator = markdown.my_input()


def lobby():
    """lobby func, ничего не возвращает"""
    print("Markdown Editor by Maks!")
    main()


# Точка входа
if __name__ == "__main__":
    lobby()
