# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

# ordem: lowercase, uppercase, dígitos
# os dígitos: odd (ímpar), even (par)

list_all = input()
list_result = []
list_result.extend(sorted([character for character in list_all if character.isalpha() if character.islower()]))
list_result.extend(sorted([character for character in list_all if character.isalpha() if character.isupper()]))
list_result.extend(sorted([character for character in list_all if character.isdigit() if int(character) % 2 != 0]))
list_result.extend(sorted([character for character in list_all if character.isdigit() if int(character) % 2 == 0]))
print(''.join(list_result))