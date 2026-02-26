#####################################
####author:Anzilz1972
####date: 2026-2-24
#####################################

first_name = 'eric'
last_name = 'chang'

msg = f"Hello {first_name.title()}, would you like to learn some Python today?"
print(msg)

print(f"{first_name.lower()} {last_name.lower()}")
print(f"{first_name.upper()} {last_name.upper()}")
print(f"{first_name.title()} {last_name.title()}")

great_man = 'chair mao'
proverb = 'Ten thousand years is too lang,seize the hour'
print(f'{great_man.title()} once said,"{proverb}"')

famous_person = 'robert herrick'
msg = f'{famous_person.title()} once said, "No Pains,no gains"'
print(msg)

aperson = '  \t\nrobert herrick\n\t  '
print(f'++{aperson}++')
print(f'++{aperson.lstrip()}++')
print(f'++{aperson.rstrip()}++')
print(f'++{aperson.strip()}++')

file_name = 'python_notes.txt'
print(file_name.removesuffix('.txt'))

favorite_num = 9
msg = f"{favorite_num} is my luckey number!"
print(msg)











