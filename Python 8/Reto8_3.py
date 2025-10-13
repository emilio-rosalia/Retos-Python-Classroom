def bisiesto (year):
    """
    :param year: int - year of the date.
    :return: bool - True if the year is leap, False otherwise.
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
    
print("Contador de años bisietos")
year_1 = ''
while year_1.isdigit() == False:
    year_1 = input("Escribe un año: ")
year_1= int(year_1)

year_2 = int(input(f"Escribe otro año mayor que {year_1}: "))
count = 0 # Contador de años bisiestos
for i in range(year_1, year_2 + 1):
    if bisiesto(i):
        count += 1

print(f"Entre {year_1} y {year_2} hay {count} años bisiestos.")