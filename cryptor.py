import random


def encrypt(text: str) -> list:
	encrypted_text = ''
	key = []
	for letter in text:
		random_num = random.randint(1, 99)
		new_letter = chr(ord(letter) + random_num)
		encrypted_text += new_letter
		key.append(random_num) 
	return [encrypted_text, key]


def decrypt(text_key: list) -> str:
	encrypted_text, key = text_key[0], text_key[1]
	decrypted_text = ''
	for letter in encrypted_text:
		new_letter = chr(ord(letter) - key[0])
		key.pop(0)
		decrypted_text += new_letter
	return decrypted_text