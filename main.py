from data_hiding import Account

a = Account(12345677356)
print(a.get_cash)
a.set_cash(100)
print(a.get_cash())

a.set_cash(2.34)
print(a.get_cash())

a.set_cash(-23523465928)
print(a.get_cash())

a.set_cash("ala ma kota")
print(a.get_cash())

a.cash
a.cash = 100
