#!/usr/bin/env python3

from sys import argv
from Crypto.Cipher import AES

import item_lists
from sorting import sort_items

key = b"\x5c\xeb\x9d\x0a\xeb\xb9\x5a\xc0\x27\x0b\x0a\xf6\x75\x3d\xfc\x0e\xe3\xe6\x8b\xb6\x94\x79\x02\x0f\x24\x30\xe2\xea\x00\x2b\xd4\xc9"


def finish(message):
	print(message)
	input("Press Enter to quit.")
	raise SystemExit


def is_valid_save(file):
	with open(file, 'rb') as f:
		header = f.read(8)

	return header == b'D001\x00\x00\x00\x00'


def find_save():
	print("TODO: Find Save.")


def decrypt_save(file):
	with open(file, 'rb') as f:
		text = f.read()
	
	cipher = AES.new(key, AES.MODE_ECB)
	dec = cipher.decrypt(text[8:])

	return dec.decode()


def encrypt_data(data):
	cipher = AES.new(key, AES.MODE_ECB)
	padding = ' ' * (16 - (len(data) % 16))
	enc = cipher.encrypt(bytearray(data + padding, 'utf-8'))

	return b"D001\x00\x00\x00\x00" + enc


def write_file(file, data):
	with open(file, 'wb') as f:
		f.write(data)
	print("Written to", file)


if __name__ == "__main__":
	if len(argv) > 1:
		written = False
		for file in argv[1:]:
			if is_valid_save(file):
				data = decrypt_save(file)
				data = sort_items(data)
				data = encrypt_data(data)
				#write_file(file.rsplit(".", 1)[0] + "_sorted.dat", data)
				write_file(file, data)
				written = True
			else:
				print(file, "isn't a valid Minecraft Dungeons save.")
		if written:
			finish("Sucess!")
		else:
			finish("Nothing written.")
	else:
		find_save()
		#TODO
		finish("Sucess!")
