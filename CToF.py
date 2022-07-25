
result = input("what's the temperature?")
if result.isdigit():
    celsius = int(result)
else:
    print("I can't understand you...")
    exit()

farenheit = celsius * (9/5) + 32

print("{}°C equals {}°F".format(celsius, farenheit))