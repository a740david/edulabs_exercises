user=input("time: ")

number_of_employees=int(input("number_of_employees: "))

coffes=["","ESPRESSO","DOPPIO","LUNGO","RISTRETTO","MACCHIATO",
"CORRETTO","CON PANNA","ROMAMO","CAPPUCCINO",
"AMERICANO","CAFELATTE","FLATWHITE","MAROCCHINO","MOCHA",
"BICERIN","BREVE","RAFCOFFEE","MEADRAF","VIENNACOFFEE",
"CHOCILATEMILK","LATTE MACCHIATO","GLACE","FREDDO",
"IRISHCOFFEE","FRAPPE","CAPPUCCINOFREDDO","CARAMELFRAPPE","ESPRESSOLACCINO"]

#bonus1
shift=input("enter shift: ")
if(shift.isdigit()):
   shift=int(shift)
else:
    shift=0

#bonus2

is_remove=input("is_remove: ")
if(is_remove=="Delete"):
 remove=int(input("enter_remove: "))
 updated_list=coffes.pop(remove)
 print("Updated List: ",coffes)
else:
    is_remove=0

time=user.split(':')

if(int(time[0])<24 and int(time[1])<60):
   print( "Person 0 :"+ coffes[int(time[0])+shift])
   name_of_coffe = 0
   coffes_of_employees = 0
   if (number_of_employees > 1):
       for i in range(1,number_of_employees+1):
           coffes_of_employees = (coffes_of_employees + int(time[1]))
           name_of_coffe = coffes[(coffes_of_employees + int(time[0])+shift) % (len(coffes)-1)]
           print( "Person " + str(i)+ " :"+ name_of_coffe)
else:
    print("erorr")