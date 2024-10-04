'''
#1
class circle:
    def __init__ (self, radius, color, pi):
        self.radius = radius
        self.color = color
        self.pi = pi
    def getCircum(self):
        getCircum = smart.radius * smart.pi
        return getCircum
smart = circle(5, 'blue', 3.141592653589793)

print (smart.getCircum())

'''
'''
#2
class player:
    def __init__(self, inventory, money, health):
        self.inventory = inventory
        self.money = money
        self.health = health
    def add_Inventory (self):
        for item in self.inventory:
            print({f'skin': '', 'gunskin': ''})
            return item
    def remove_inventory (self, item):
        for item in self.inventory:
            if item == item:
                self.inventory.remove(item)
                return True
        print ("Item not found in inventory")
        return False
    def add_money (self, amount):
        self.money += amount
        return self.money
    def remove_money (self, amount):
        if self.money >= amount:
            self.money -= amount
            return self.money
        print ("Not enough money")
        return False
    def add_health (self, amount):
        self.health += amount
        if self.health > 0:
            self.health = 100
        return self.health
    def remove_health (self, amount):
        if self.health == 0:
            return self.health
        print ("you are dead")
        return False

'''

'''
#3
class mybtchs:
    def __init__(self):
        self.nicebtch = ['btch 1']
        self.funbtch = ['btch 2']
        self.badbtch = ['btch 3']
    def AJmood(self, sick, happy, romantic):
       mood = {'sick': self.nicebtch, 'happy': self.funbtch, 'romantic': self.badbtch}
       if sick:
           print(f"you need {mood['sick'][0]}")
       elif happy:
           print(f"you need {mood['happy'][0]}")
       elif romantic:
           print(f"you need {mood['romantic'][0]}")

feelings = mybtchs()
feelings.AJmood(True,False,False)

AJbtchs = mybtchs()
print ('\nthese r my btchs')
print (f'{AJbtchs.nicebtch[0]} is the nicest')
print(f'{AJbtchs.funbtch[0]} is the most fun')
print(f'{AJbtchs.badbtch[0]} is the baddest out of all of em')

# print ('these r my btchs')
'''