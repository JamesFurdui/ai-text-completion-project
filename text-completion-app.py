import cohere

co = cohere.Client(api_key="5J12uSSPqZyY5JRiy1beWFq4vnTk1Tq20ShcH6Mg")

max_tokens = 100
temperature = 0.7
raw_prompting = False
presence_penalty = 0.0


def modifyAIModel():
    global max_tokens, temperature, raw_prompting, presence_penalty

    while True:
        print("\nWhat would you like to modify?")
        print("1. Max tokens (1-500)")
        print("2. Temperature (0.0-1.0)")
        print("3. Presence penalty (0.0-1.0)")
        print("4. Toggle raw prompting")
        print("5. Back to main menu")

        try:
            user_input = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if user_input == 1:
            try:
                value = int(input("Enter the max tokens (1-500): "))
                if 1 <= value <= 500:
                    max_tokens = value
                    print(f"Max tokens set to {max_tokens}.")
                else:
                    print("Value must be between 1 and 500.")
            except ValueError:
                print("Invalid input. Must be an integer.")
        elif user_input == 2:
            try:
                value = float(input("Enter temperature (0.0-1.0): "))
                if 0.0 <= value <= 1.0:
                    temperature = value
                    print(f"Temperature set to {temperature}.")
                else:
                    print("Temperature must be between 0.0 and 1.0.")
            except ValueError:
                print("Invalid input. Must be a float.")
        elif user_input == 3:
            try:
                value = float(input("Enter presence penalty (0.0-1.0): "))
                if 0.0 <= value <= 1.0:
                    presence_penalty = value
                    print(f"Presence penalty set to {presence_penalty}.")
                else:
                    print("Value must be between 0.0 and 1.0.")
            except ValueError:
                print("Invalid input. Must be a float.")
        elif user_input == 4:
            raw_prompting = not raw_prompting
            status = "enabled" if raw_prompting else "disabled"
            print(f"Raw prompting has been {status}.")
        elif user_input == 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def callAIModel(user_input):
    try:
        response = co.generate(
            model="command",
            prompt=user_input,
            max_tokens=max_tokens,
            temperature=temperature,
            raw_prompting=raw_prompting,
            presence_penalty=presence_penalty,
        )
        print(response.generations[0].text)
    except cohere.CohereError as e:
        print(f"Error generating text: {e}")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. Prompt the AI")
        print("2. Modify AI settings")
        print("3. Exit")

        try:
            choice = int(input("Enter choice (1–3): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        if choice == 1:
            user_prompt = input("Enter your prompt: ")
            callAIModel(user_prompt)
        elif choice == 2:
            modifyAIModel()
        elif choice == 3:
            print("Thank you for using the AI model! Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

main()
