import functions

phonebook = functions.generate_phonebook(50000)
ez_numbers = []
request_data = functions.print_user_interface()
functions.handle_user_request(phonebook, ez_numbers, request_data["mode"], request_data["numbers_amount"])
