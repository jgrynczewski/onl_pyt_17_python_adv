class SingleChoiceQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def ask(self):
        # wyświetli pytanie
        print(self.question)

        # wyświetli odpowiedzi
        available_answers = []
        for answer in zip("abcdefghijklmnoprstuwyz", self.answers):
            available_answers.append(answer[0])
            print(f"{answer[0]}) {answer[1]}")

        # zapyta użytkownika o odpowiedź
        while True:
            answer = input("Podaj odpowiedź: ")
            if answer not in available_answers:
                print("Niedopuszczalna odpowiedź")
            else:
                break

        # wyświetli pustą linię
        print()

        # zwróci odpowiedź
        return answer


class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        result = {}

        # wyświetli tytuł ankiety oraz jedną, pustą linię,
        print(self.title)
        print()

        # dla każdego pytania (obiektu klasy SingleChoiceQuestion) uruchomi jego metodę ask()
        for idx, question in enumerate(self.questions):
            answer = question.ask()
            result[idx] = answer

        # wyświetli napis 'Dziękuję!'
        print("Dziękuję!")

        # zwróci słownik, w którym kluczami będą numery pytań (numerowane od zera),
        # a wartościami wyniki działania metod ask() na obiektach pytań.
        return result


questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
q1 = SingleChoiceQuestion(
    'Matryca',
    ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali']
)
q2 = SingleChoiceQuestion(
    'Rodzaj ekranu',
    ['matowy', 'błyszczący']
)
q3 = SingleChoiceQuestion(
    'Czy polecisz go znajomemu?',
    ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie']
)
questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)

answers = questionnaire.run()

print(answers)
