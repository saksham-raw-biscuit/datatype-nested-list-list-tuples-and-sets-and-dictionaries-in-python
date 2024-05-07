# The multiple assignment trick (technically called tuple unpacking) is a shortcut that lets you assign multiple variables with the values in a list in one line of code.

address = ['Nepal', 'No.3', 'Kathmandu',44600]

# variable in LHS must be equal to len(RHS)
country,province_no,district,zipcode = address 
# this is te multiple assignment technique
#size store cat[0]
#color store cat[1]
#disposition store ca[2]

print(f"Country: {country}\nProvince:  {province_no}\nDistrict: {district}\nZip-Code: {zipcode}")

