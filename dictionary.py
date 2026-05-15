our_first_dictionary = {}
print(type(our_first_dictionary))

our_first_dictionary['first_key'] = 'first_value'
print(our_first_dictionary)
print(our_first_dictionary['first_key'])

an_extra_key_value_dict = {"extra_key": "extra_value", "another_extra_key": "another_extra_value"}
print(an_extra_key_value_dict)
our_first_dictionary.update(an_extra_key_value_dict)
print(our_first_dictionary)
del our_first_dictionary["another_extra_key"]
print(our_first_dictionary)