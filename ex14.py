from sys import argv
script, user_name, title = argv
prompt = '>'

print(f"Hi {title} {user_name}! im the {script}")
print(f"Do you like me {user_name}?")

likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer u got")
computer = input(prompt)

print(f"""
alright so u said {likes} about likeing me
and you live in {lives}
and you have a {computer}
noice
""")

