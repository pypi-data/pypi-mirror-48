# Userspy

An easy app for managing users.

## Installing

---

```python
pip install userspy
```

## Functions

---

**create** - creates a database
**Register** - Check password, hash and insert to the database
**Login** - check login credentials (returns True or Fales)
**password_hash** - hash password
**check_password** - verifys only password (returns True or False)

```python
import userspy

# creates the database with usernames and hashed passwords
userspy.create(DataBaseName)

# Registers a user, hashed and inserts to database
userspy.Register(UserName, Password)

# Checks user Authentication credentials
isAuthenticated = userspy.Login(UserName, Password)

# Returns hashed password
hashed_password = userspy.password_hash(Password)

# Checks user password`
isPasswordValid = userspy.check_password(Password, Hashed_Password)
```

---

created by ofri kirshen
