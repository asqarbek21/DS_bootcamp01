import sys

def extract_to_tsv(path):
    try:
        with open(path, 'r') as infile:
            emails = infile.read().splitlines()

        with open('employees.tsv', 'w') as outfile:
            outfile.write("Name\tSurname\tE-mail\n")
            for email in emails:
                if '@' not in email or '.' not in email:
                    continue
                name, surname = email.split('@')[0].split('.')
                name = name.title()
                surname = surname.title()
                outfile.write(f"{name}\t{surname}\t{email}\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 names_extractor.py <emails_file>")
    else:
        extract_to_tsv(sys.argv[1])