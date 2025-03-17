# Well-Tools

from Config.Util import *
from Config.Config import *

try:
    import bcrypt
    import hashlib
    import base64
    from hashlib import pbkdf2_hmac
except Exception as e:
    ErrorModule(e)

Title(f"Password Encrypted")
try:
    Slow(f"""{encrypted_banner}
 {BEFORE}01{AFTER}{white} BCRYPT
 {BEFORE}02{AFTER}{white} MD5
 {BEFORE}03{AFTER}{white} SHA-1
 {BEFORE}04{AFTER}{white} SHA-256
 {BEFORE}05{AFTER}{white} PBKDF2 (SHA-256)
 {BEFORE}06{AFTER}{white} Base64 Decode
    """)

    choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Encryption Method -> {reset}")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        ErrorChoice()

    password = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Password to Encrypt -> {white}")

    def EncryptPassword(choice, password):
        encrypt_methods = {
            '1': lambda p: bcrypt.hashpw(p.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            '2': lambda p: hashlib.md5(p.encode('utf-8')).hexdigest(),
            '3': lambda p: hashlib.sha1(p.encode('utf-8')).hexdigest(),
            '4': lambda p: hashlib.sha256(p.encode('utf-8')).hexdigest(),
            '5': lambda p: pbkdf2_hmac('sha256', p.encode('utf-8'), "this_is_a_salt".encode('utf-8'), 100000).hex(),
            '6': lambda p: base64.b64encode(p.encode('utf-8')).decode('utf-8')
        }
        
        try:
            return encrypt_methods.get(choice, lambda p: None)(password)
        except Exception as e:
            print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Error during encryption: {e}")
            return None

    encrypted_password = EncryptPassword(choice, password)
    if encrypted_password:
        print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Encrypted Password: {white}{encrypted_password}{reset}")
        Continue()
        Reset()

except Exception as e:
    Error(e)
