# Abstrakcja - redukowanie złożoności poprzez chowanie szczegółów


class MailServer:
    def __connect(self):
        print("Connect")

    def __authenticate(self):
        print("Authenticate")

    def __disconnect(self):
        print("Disconnect")

    def send_mail(self):
        self.__connect()
        self.__authenticate()
        print("Send mail")
        self.__disconnect()


m = MailServer()
m.send_mail()
