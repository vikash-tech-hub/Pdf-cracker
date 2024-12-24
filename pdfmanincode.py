import pikepdf
from tqdm import tqdm  # Correct import of tqdm

# Read passwords from the wordlist file
passwords = [line.strip() for line in open("wordlist1.txt")]

# Iterate over each password with a progress bar
for password in tqdm(passwords, desc="Decrypting PDF"):
    try:
        # Attempt to open the PDF with the current password
        with pikepdf.open(r"C:\Users\pc\Downloads\vika.pdf", password=password) as pdf:  # Use raw string for the path
            print(f"\n[+] Password found: {password}")
            break  # Exit the loop if the password is found
    except pikepdf.PasswordError:
        # Wrong password, continue trying the next one
        continue
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
