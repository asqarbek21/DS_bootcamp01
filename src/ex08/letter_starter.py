import sys

def greet_by_email(email):
    try:
        with open('employees.tsv', 'r') as f:
            lines = f.read().splitlines()[1:]

        for line in lines:
            name, surname, stored_email = line.split('\t')
            if stored_email.strip().lower() == email.strip().lower():
                print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                return
        print("Email not found.")
    except FileNotFoundError:
        print("employees.tsv not found. Please run names_extractor.py first.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 letter_starter.py <email>")
    else:
        greet_by_email(sys.argv[1])