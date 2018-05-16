from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("q")
print(f"Do you like me {user_name}")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)
