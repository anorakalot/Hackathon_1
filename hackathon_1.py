import requests
from requests.auth import HTTPDigestAuth
import json

def start():
	print "\nAPP INVENTORY THINGS IS A GOO!:"
	print "hello what would you like to do"
	print "you run a virtual shop "
	print """
	1. Check a single item
	2. Check all inventory items
	3. Delete all items (for testing purposes tell the programmer before you push this button!!!!!!)
	4. Get stock of an item
	5. Get all stocks
	"""

	choice = raw_input("...")
	
	
	if choice == '1':
		find_item()
	
	elif choice == '2':
		find_all_item()
	
	elif choice == '3':
		delete_items()
		
	elif choice == '4':
		get_stock_of_item()
		
	elif choice == "5":
		get_all_stocks()
	else:
		print "sorry that was not a valid command this will now restart"
		start()
	
	
