import populate_data

users = populate_data.create_users()
names = [x.username for x in users]
pws = [x.password for x in users]
media = populate_data.create_topics()

username = ""

while username not in names:
    username = input("Enter your username:\n")

password = pws[names.index(username)].strip()  # gets rid of whitespace

pw = ""
while pw != password:
    pw = input("Enter password:\n")

print("Logged in successfully!")
print("Media available "+media[0].name)
