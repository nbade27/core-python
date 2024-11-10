"""
    keys are always unique in dictionaries

"""

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

# we can get value based on keys in below two ways

print(monthConversions["Nov"])
print(monthConversions.get("Oct"))
print(monthConversions.get("Luv"))

