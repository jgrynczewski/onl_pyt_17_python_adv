email = input("Podaj swój mail:")

splitted_email = email.split('@')
if len(splitted_email) == 2 and splitted_email[0] and splitted_email[1] and splitted_email[1].count('.') == 1:
    print(email)
else:
    print("Niepoprawny mail")
