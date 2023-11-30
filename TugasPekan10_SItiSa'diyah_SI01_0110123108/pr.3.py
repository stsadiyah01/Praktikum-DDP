def konsonan_saja(string_input):
    konsonan = [ char for char in string_input if char.isalpha() and char.lower() not in ["a","i","u","e","o"]]
    return (konsonan)
hasil = konsonan_saja("Nurul Fikri")
print("Hasilnya adalah",hasil)
