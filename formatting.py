msg = "Journey Before Destination" 
print(msg)

msg_upr = msg.upper() # upper case
print(msg_upr)

msg_lwr = msg.lower() # lower case
print(msg_lwr)

msg_title = msg.title() # Title all first letter into capital
print(msg_title)

msg_cap = msg.capitalize() #Capitlize
print(msg_cap)

msg_swp = msg.swapcase() # swap case
print(msg_swp)

msg_cf = msg.casefold() # case fold same as lower
print(msg_cf)

# alignment
print(msg.ljust(100)) #Left alignment

print(msg.rjust(100,'_')) #right alignment

print(msg.center(100)) # center alignment


# alignment with f-strings on padding
print(f"{msg:>50}")

print(f"{msg:<50}")

print(f"{msg:^50}")