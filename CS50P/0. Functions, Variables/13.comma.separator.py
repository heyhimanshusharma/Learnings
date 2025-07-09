x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

"""The colon : indicates the start of the formatting options, and , is a specifier for a thousands separator. 
When used with numbers, it adds commas to separate thousands."""
print(f"{z:,}")