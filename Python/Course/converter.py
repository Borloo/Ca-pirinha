##TP echauffement##

input_speed = float(input("Veuillez entrer une vitesse en km/h : "))
KMH_TO_MPH = 1.609
miles_speed = input_speed / KMH_TO_MPH
rounded_miles_speed = round(miles_speed, 2)

print(f'{input_speed} km/h = {rounded_miles_speed} m/h')

#Autre méthode pour arrondir
print(f'{input_speed} km/h = {miles_speed:.2f} m/h')
