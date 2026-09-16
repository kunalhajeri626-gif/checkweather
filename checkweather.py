degree=int(input("Enter the degree :"))
if degree <=20:
    print("Cold Weather")
elif degree > 20 and degree <=38:
    print("Normal weather")
else:
    print("Hot Weather")
fahrenheit = (degree * 1.8) + 32
print("The temperature value is ",fahrenheit, "F")