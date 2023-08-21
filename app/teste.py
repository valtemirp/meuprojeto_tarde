from flask import Flask
from flask_bcrypt import Bcrypt, check_password_hash


app = Flask(__name__)
bcrypt = Bcrypt(app)

pw_hash = bcrypt.generate_password_hash('hunter2')
bcrypt.check_password_hash(pw_hash, 'hunter2') # returns True

print(check_password_hash(pw_hash))

