def is_anagram(s1, s2):
    # Remove all white spaces from the strings and convert them to lowercase
    
    # s1 = s1.replace(" ", "").lower()
    # s2 = s2.replace(" ", "").lower()

    # Check if the lengths of the strings are equal
    if len(s1) != len(s2):
        return "no"

    # Convert the strings to lists and sort them
    s1_list = sorted(list(s1))
    s2_list = sorted(list(s2))

    # Compare the sorted lists
    if s1_list == s2_list:
        return "yes"
    else:
        return "no"
    

print(is_anagram("build","dubli"))    
print(is_anagram("beast","yeast"))   


# s1="beast"
# s1_list = sorted(list(s1))
# print(s1_list)