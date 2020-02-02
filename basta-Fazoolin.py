class Business:
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
    
class Franchise:
  def __init__(self,address,menus):
    self.address=address
    self.menus=menus
    
  def available_menus(self,time):
    menu_list=[]
    menu_name=[]
    menu_avai=[]
    for menu in self.menus:
      if menu.start_time <=time<= menu.end_time:
        menu_list.append(menu.items)
        menu_name.append(menu.name)
        menu_avai.append(menu)
        
    return (menu_name, menu_avai, menu_list)
        
  def __repr__(self):
    return "The address is {address}".format(address=self.address)
  
class Menu:
  
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items= items
    self.start_time=start_time
    self.end_time=end_time
    
  def __repr__(self):
    return "The {name} menu is available from {start} till {end}.".format(name=self.name, start=self.start_time, end=self.end_time)
  
  def calculate_bill(self,purchased_items):
    total=0
    for meal in purchased_items:
      total+=self.items[meal]
    return "The total price is {total}.".format(total=total)

###################    
brunch_menu={'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu("brunch",brunch_menu,11,16)
#print(brunch)
#print(brunch.calculate_bill(['pancakes','home fries','coffee']))

early_bird_menu ={'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

early_bird= Menu("early_bird",early_bird_menu,15,18)
#print(early_bird)
#print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

dinner_menu={'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

dinner = Menu("dinner",dinner_menu,17,23)

kids_menu={'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids = Menu("kids", kids_menu,11,21)


flagship_store= Franchise('1232 West End Road',[brunch,early_bird,dinner,kids])
#print(flagship_store)

new_installment=Franchise('12 East Mulberry Street',[brunch,early_bird,dinner,kids])
#print(new_installment)
#print(new_installment.available_menus(17))

first_business = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

arepas_menu={'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas = Menu("Take a'Arepa",arepas_menu,10,20)

arepas_place= Franchise("189 Fitzgerald Avenue",[arepas])

New_arepa = Business("Take a' Arepa", [arepas_place])

print(New_arepa.franchises[0].menus[0])


