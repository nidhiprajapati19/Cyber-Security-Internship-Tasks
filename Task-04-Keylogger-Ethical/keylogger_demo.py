from datetime import datetime

print(" Ethical Keylogger Demo")
print("This program will log ONLY what you type voluntarily.")
print("No background logging or spying is performed.\n")

consent = input("Do you agree to log your input? (yes/no): ").lower()

if consent != "yes":
    print("Consent not given. Program exited.")
    exit()
  
user_text = input("\nEnter text to log: ")

time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a") as file:
    file.write(f"[{time_stamp}] {user_text}\n")

print("\n Input logged successfully!")
print(" Saved in file: log.txt")
print(" Logged ethically for educational purpose only.")
