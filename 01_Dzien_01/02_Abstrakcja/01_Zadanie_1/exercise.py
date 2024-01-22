import random


random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


def main(usdpln_rates):
    wallet_pln = 100.0
    wallet_usd = 0.0

    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(wallet_pln, 2)} PLN, ${round(wallet_usd, 2)}, rate {usdpln_rate}')
        while True:
            choice = input('Decision [b/s/w/buy/sell/wait]: ')
            if choice not in ('b', 's', 'w', 'buy', 'sell', 'wait', ''):
                print(f'Invalid choice: {choice}')
            else:
                break
        if choice in ('k', 'buy'):
            wallet_usd += wallet_pln / usdpln_rate
            wallet_pln = 0
        elif choice in ('s', 'sell'):
            wallet_pln += wallet_usd * usdpln_rate
            wallet_usd = 0

    wallet_pln += wallet_usd * usdpln_rate
    wallet_usd = 0
    print(f'Your result: {wallet_pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)
