# An array version.
# Better for "standalone entries" 
array_example_1 = ["bob", "frank", "joe"]
array_example_2 = ["9436196", "1234567", "7654321"]

# Another array version.
# Have to enter each one separately and in order.
array_example = ["bob","9436196","frank","1234567","joe","7654321"]

# Dictionary version.
# Better for "pair entries".
# Overkill for "single entries".
dictionary_example = {
    "bob" : "9436196",
    "frank" : "1234567",
    "joe" : "7654321" 
}

# INSERT
# Array insert example.
array_example.append("bobby")
array_example.append("7457384")

# dictionary insert example.
dictionary_example["bobby"] = "7457384"


# UPDATE
# Array update example.
array_example[-2] = "robert"
array_example[-1] = "6457384" 

dictionary_example.update({"bobby" : "6457384"})
# Updating a dictionary key is a bit different.
dictionary_example["robert"] = dictionary_example.pop("bobby")

print(dictionary_example)


# REMOVE
array_example.remove("robert")
array_example.remove("6457384")

print(array_example)