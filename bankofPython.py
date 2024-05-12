class addAccount():
    def __init__(self,accountNumbers,password):
        self.accountNumbers=accountNumbers
        self.password=password
        self.money=0
    def aboutAccount(self):       
        print(f'Əziz istifadəçi sizin hesabinizda {self.money} Azn pul var.')   
    def addMoney(self,money):
        self.money+=money
        print(f'Əziz istifadəçi sizin hesabiniza {money} Azn elave olundu.Toplam mebleg {self.money}')  
    def withdraw(self,money):
        self.money-=money
        print(f'Əziz istifadəçi sizin hesabinizdan {money} Azn çıxarıldı.Toplam mebleg {self.money}') 
        
class Credits(addAccount):
    def __init__(self,accountNumbers, password):
        super().__init__(accountNumbers,password)
    def getLoan(self,amount):
        self.loan=amount
        monthMoney=amount/12
        print(f'Istediyiniz {amount} azn mebleg verildi. Ayliq {monthMoney} azn odemeli olacaqsiniz')
    def payLoan(self,a):
        self.loan-=a
        print(f'Lazım olan ödənişdən artıq olan {int(-self.loan)} azn məbləğ geri qaytarıldı. Borcunuz : 0 azn') if self.loan<=0 else  print(f'Ödədiyiniz {a} azn məbləğ kreditdən çıxıldı . Qalıq borc : {self.loan}')
        
user1=addAccount(3640817598474185,1903)
user1.aboutAccount()
user1.addMoney(750)
user1.addMoney(320)
user1.withdraw(457)
kredit=Credits(1212343456567878,1999)
kredit.getLoan(1200)
kredit.payLoan(200)
kredit.payLoan(1500)