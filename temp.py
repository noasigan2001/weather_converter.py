def celsius_to_fahrenheit(celsius):
  return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) / 5

def classify_temperature(celsius):
  if celsius < 0:
    return "Below Freezing"
  elif celsius < 15:
   return "Cold"
  elif celsius < 25:
    return "Warm"
  else:
    return "Hot"

def main():
 try:
  temp = float(input("Enter temperature: "))
 except ValueError:
   print("Enter a valid number")
   return

 unit = input("Enter unit: (C or F): )").strip().upper()

 if unit == "C":
  celsius = temp
  fahrenheit = celsius_to_fahrenheit(temp)
 elif unit == "F":
  fahrenheit = temp
  celsius = fahrenheit_to_celsius(temp)
 else:
    print("Enter a valid unit")
    return
 print(f"{celsius:.1f} C / {fahrenheit:.1f} F")
 print(classify_temperature(celsius))
if __name__ == "__main__":
     main()


 