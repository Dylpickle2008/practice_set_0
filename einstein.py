#Creates a program that calculates E=MC^2 round 300000000 kg
def main():
    mass = float(input())                       #converts mass input into simpelest decimal
    convert(mass)                               #function convert(below) the mass

def convert(kg):
    converted_kg = round(kg * (300000000 ** 2))               #converts mass to converted factor          
    print(f"{converted_kg}:.0f")                          #prints converted kg with rounded off value   


main()