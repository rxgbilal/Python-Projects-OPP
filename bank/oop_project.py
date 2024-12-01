from bank_accounts import *

Dave = bankAccount(1000, "Dave")
Sara = bankAccount(1000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.transfer(100, Sara)

jim = interestRewardAcct(1000, "jim")
jim.getBalance()
jim.deposit(100)
jim.transfer(100, Dave)

blaze = Savingsacct(1000, "Blaze")
blaze.getBalance()
blaze.deposit(100)
blaze.transfer(100, Sara)