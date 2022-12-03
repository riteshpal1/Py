
# Slicing

name = "Vijay Deenanath chauhan"

m_name = name[6:15]  # middle name
print(m_name)

f_name = name[0:5]
print(f_name) # First name

l_name = name[-7:]
print(l_name) # last name


name ="Aman Pal"
f_name = name[0:4]  
print(f_name)

full_name = name[ : ] # Full name
print(full_name)

rev_name = name[ : :-1] # rev name
print(rev_name)

rev_name = name[-1: : ]
print(rev_name)

even_name = name[ : :2] # even name
print(even_name)

odd_name = name[1: :2] # odd name 
print(odd_name)

message = '''Founded as L&T Information Technology Ltd in December 1996, LTI is a listed subsidiary, 74% owned
by Larsen & Toubro (L&T).[4][5] During 2001–2002 the company's name waschanged from L&T Information Technology
Limited to Larsen & Toubro Infotech Limited and in the same year the company achieved the assessed level of 
Software Engineering Institute's (SEI) Maturity Level 5.[6][7] In 2013–14, L&T Infotech's engineering services
segment and parent Larsen & Toubro's design and engineering division were consolidated under a pure play engineering,
research and development services company called L&T Technology Services.[8][9] In July 2016, L&T Infotech went 
public via an initial public offering (IPO) of ₹1,243 crore (US$184.98 million).[10] L&T Infotech dropped the word 
'Infotech' from its name to reflect the changed business environment and rebranded itself as 'LTI' with a tag line
of 'Let's Solve' in May 2017.[11] In 2022, it was announced that LTI and Mindtree will be merging.[12] The merged
entity will be named LTIMindtree.'''

print("length of message is", len(message))

# first 100 character
print(message[ : 100])

# last 200 character
print(message[-200:])

# every 10th character
print(message[::10])

# all data ecpect first 100 character and last 100 character
print(message[100:-100])