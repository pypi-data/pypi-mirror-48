# Userpy

An easy app for managing users.

## Installing

---

```python
pip install userpy
```

## Functions

---

**create** - creates a database
**Register** - Check password, hash and insert to the database
**Login** - check login credentials (returns True or Fales)
**password_hash** - hash password
**check_password** - verifys only password (returns True or Fales)

```python
import user_management as um

# creates the database with usernames and hashed passwords
um.create(DataBaseName)

# Registers a user, hashed and inserts to database
um.Register(UserName, Password, Confirm_Password)

# Checks user Authentication credentials
isAuthenticated = um.Login(UserName, Password)

# Returns hashed password
hashed_password = um.password_hash(Password)

# Checks user password
isPasswordValid = um.check_password(Password, Hashed_Password)
```

---

created by ofri kirshen
