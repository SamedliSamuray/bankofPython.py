class AddAccount:
    def __init__(self,name,surname,account_number, password):
        self.money = 0
        self.name = name
        self.surname = surname
        self.account_number = account_number
        self.password = password

    def about_account(self):
        print(f'{self.name} {self.surname} , hesabınızda {self.money} AZN pul var')

    def add_money(self, money):
        self.money += money
        print(f'{self.name} {self.surname} ,hesabınıza {money} AZN əlavə olundu. Toplam balans :  {self.money} AZN')

    def withdraw(self, money):
        if money <= self.money:
            self.money -= money
            print(f'{self.name} {self.surname} ,hesabınızdan {money} AZN pul çəkildi.. Toplam balans: {self.money} AZN')
        else:
            print("Yetərsiz vəsait. Əməliyyat ləğv edildi.")

class Credits:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print("Hesab uğurla əlavə edildi.")

    def get_loan(self, account, amount):
        account.add_money(amount)
        self.creditMoney=0
        self.moneyMonth=amount/12
        self.creditMoney+=amount
        print(f"{account.name} {account.name} ,siz {amount} AZN məbləğində kredit götürmüsünüz.Ayliq odenis minimal olaraq {self.moneyMonth} Azn. İndi ümumi balansınız: {account.money} AZN")

    def pay_loan(self, account, amount):
        if amount <= account.money:
            account.withdraw(amount)
            self.creditMoney-=amount
            print(f"{account.name} {account.surname} ,siz kreditinizin {amount} AZN-ni ödəmisiniz. Qalan kredit borcunuz: {self.creditMoney} AZN. Balansiniz {account.money} AZN")
        else:
            print("Yetərsiz vəsait. Əməliyyat ləğv edildi.")

user1 = AddAccount('Samuray','Samedli',3640817598474185, 1903)

user1.about_account()
user1.add_money(750)
user1.add_money(320)
user1.withdraw(457)

credit = Credits()
credit.add_account(user1)
credit.get_loan(user1, 1200)
credit.pay_loan(user1, 200)

user2 = AddAccount('Necip','Uysal',1111111111111111, 1999)
user2.about_account()
user2.add_money(1340)
user2.add_money(100)
user2.withdraw(800)
credit.add_account(user2)
credit.get_loan(user2, 2400)
credit.pay_loan(user2, 200)