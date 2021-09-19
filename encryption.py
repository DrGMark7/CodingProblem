my_string = input("Enter 5 characters: ").lower()
import string   
house = "abcdefghijklmnopqrstuvwxyz"
reverse_letters = house[::-1] #zyxwvutsrqpomnlkjihgfedcba
rep_dict = dict(zip(house, reverse_letters))
reverse_string = ''.join(map(rep_dict.get, my_string))
print ('Encryption is',reverse_string,)