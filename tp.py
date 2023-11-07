import math
import database

def intinput(question=""):
    answer = input(question)
    try:
        answer = int(answer)
        return answer
    except:
        pass
    return

class Trading_Post:
    def __init__(self, user):
        self.db = database.Db(user)
        self.data = self.db.get_file()

    def main(self):
        print("Welcome To The Trading Post!", end=" ")
        while True:
            print("How can I help you?")
            print("[0] Food\n[1] Weapons\n[2] Items\n[3] Leave")
            answer = intinput()
            if answer == 0:
                self.food()
            if answer == 1:
                self.weapons()
            if answer == 2:
                self.items()
            if answer == 3:
                print("Thanks for shopping by! Come back soon!")
                break
            self.db.save_file(self.data)

    def food(self):
        db = self.db
        data = self.data
        print("""TP-->Food:
              [0] Bread $5
              [1] Cake  $10""")
        answer = intinput()
        if answer == 0:
            sure = intinput("Buy Bread?\n[0] Yes\n[1] No\n")
            if sure == 0:
                amount = intinput("How many loaves? (Number)  ")
                cost = amount * 5
                if data['money'] >= cost:
                    db.add_item(f"bread x{amount}")
                    data['money'] -= cost
                    print(f"You bought {amount} loaves of bread for {cost} dollars.")
                else:
                    print("You don't have enough money!")
                if answer == 1:
                    sure = intinput("Buy 1 Cake?\n[0] Yes\n[1] No")
                    if sure == 0:
                        cost = 10
                        if data['money'] >= cost:
                            db.add_item(f"Cake x1")
                            data['money'] -= cost
                            print("You bought 1 cake for 10 dollars.")
                        else:
                            print("You don't have enough money!")
            return	
    def weapons(self):
        db = self.db
        data = self.data
        print("""TP--->Weapons:
              [0] Club $30
              [1] Axe $50""")
        answer = intinput()
        if answer == 0:
            sure = intinput("Buy Club?\n[0] Yes\n[1] No\n")
            if sure == 1:
                return
            cost = 30
            if data["money"] >= cost:
                db.add_item("Club x1")
                data["money"] -= cost
                print("You bought a club")
            else:
                print("You don't have enough money!")

    def items(self):
        print("Sorry! This feature is unavailiable on the demo version.")
        return

if __name__=='__main__':
    tp = Trading_Post('Dalton')
    tp.main()
