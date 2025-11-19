monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Jun"))
print(monthConversions.get("L"))

for key in monthConversions:
    print(key)

for value in monthConversions.values():
    print(value)

for key,value in monthConversions.items():
    print(key,value)