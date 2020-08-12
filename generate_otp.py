# Importing random to generate random string sequence
import random
# Importing string library function
import string
# TimestampSigner to add time information with the generated password.
from itsdangerous import TimestampSigner

SECRET_KEY = "kHJmo97vFGbze19GgpLiQm643vcWaP"

def generate_pass(size=6):
    # Takes random choices from ascii_letters and digits
    generate_pass = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(size)])
    return generate_pass

def temp_otp(size=6):
    s = TimestampSigner(SECRET_KEY)
    otp = s.sign(generate_pass(size))
    return otp

if __name__ == '__main__':
    # Driver Code
    otp = temp_otp()
    print(otp.decode())
