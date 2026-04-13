print("🌡️ Temperature Converter")

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"✅ {c}°C = {f}°F")

    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print(f"✅ {f}°F = {c}°C")

    elif choice == '3':
        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice! Try again.")
