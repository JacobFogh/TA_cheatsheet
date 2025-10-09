from bank_account import OverdraftAccount

my_account = OverdraftAccount(0, 500)
returned1 = my_account.get_balance()
my_account.deposit(1000)
returned2 = my_account.get_balance()
returned3 = my_account.withdraw(1300)
returned4 = my_account.get_balance()
returned5 = my_account.withdraw(500)
returned6 = my_account.get_balance()

expected1 = 0
expected2 = 1000
expected3 = 1300
expected4 = -300
expected5 = 0
expected6 = -300

if ((returned1 == expected1) and (returned2 == expected2) and
        (returned3 == expected3) and (returned4 == expected4) and
        (returned5 == expected5) and (returned6 == expected6)):
    print(f"Test for task 10 passed")
else:
    print(f"Test for task 10 failed because it yielded:")
    print(repr(returned1), repr(returned2), repr(returned3), repr(returned4), 
            repr(returned5), repr(returned6))
    print("instead of:")
    print(repr(expected1), repr(expected2), repr(expected3), repr(expected4), 
            repr(expected5), repr(expected6))
