username = input("Enter Username: ")
email = input("Enter email: ")
pwd = input('Enter Password: ')
cpwd = input("Confirm Password: ")

if len(username) > 0 and username.isalnum():
  if len(email) > 0 and '@' in email:
    if len(pwd) >= 4:
      if pwd == cpwd:
        print('Registration Successful')
      else: print('Password do not match')
    else:
      print("Password must be at least 4 characters")
  else:
    print('Invalidd email')
else:
  print("userrname is invalid")