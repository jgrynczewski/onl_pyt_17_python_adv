import random


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


class CommandPrompt:
    def __init__(self, buy_commands, sell_commands, wait_commands):
        self.buy_commands = buy_commands
        self.sell_commands = sell_commands
        self.wait_commands = wait_commands
        self.available_commands = buy_commands + sell_commands + wait_commands

    def ask(self):
        while True:
            commands = "/".join(self.available_commands)
            choice = input(f'Decision [{commands}]: ')
            if choice not in self.available_commands:
                print(f"Invalid choice: {choice}")
            else:
                if choice in self.buy_commands:
                    return "buy"
                elif choice in self.sell_commands:
                    return "sell"
                else:
                    return "wait"


class Wallet:
    def __init__(self, pln, usd):
        if not (isinstance(pln, float) and isinstance(usd, float)):
            raise TypeError("Wrong type (should be float)")
        self.pln = pln
        self.usd = usd

    def convert_pln_to_usd(self, usdpln_rate):
        self.usd += self.pln / usdpln_rate
        self.pln = 0

    def convert_usd_to_pln(self, usdpln_rate):
        self.pln += self.usd * usdpln_rate
        self.usd = 0


c = CommandPrompt(
    buy_commands=['b', 'buy'],
    sell_commands=['s', 'sell'],
    wait_commands=['w', 'wait', '']
)


def main(usdpln_rates):
    w = Wallet(100.0, 0.0)

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(w.pln, 2)} PLN, ${round(w.usd, 2)}, rate {usdpln_rate}')
        result = c.ask()

        if result == "buy":
            w.convert_pln_to_usd(usdpln_rate)

        elif result == "sell":
            w.convert_usd_to_pln(usdpln_rate)

    w.convert_usd_to_pln(usdpln_rates[-1])
    print(f'Your result: {w.pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)
