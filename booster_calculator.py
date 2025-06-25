def add_seventy_percent(value):
    return value + (value * 0.70)


def get_float_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            return None
        try:
            return float(user_input)
        except ValueError:
            print("⚠️ Please enter a valid rational number (e.g., 12, 3.5, 0.25).")


def main():
    print("📈 Welcome to the 70% Booster Calculator!")
    print("----------------------------------------")

    while True:
        number = get_float_input("Enter a number (or type 'exit' to quit): ")
        if number is None:
            print("👋 Goodbye! Thanks for using the calculator.")
            break

        result = add_seventy_percent(number)
        print(f"✅ Original: {number:.2f} | With +70%: {result:.2f}\n")


if __name__ == "__main__":
    main()