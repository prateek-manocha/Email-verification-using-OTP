import re
from generate_otp import temp_otp
from send_mail import send_email
from itsdangerous import TimestampSigner

SECRET_KEY = "kHJmo97vFGbze19GgpLiQm643vcWaP"

def validate_email(email):
	if len(email) > 7:
		if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
			return True
	return False

if __name__ == "__main__":
    sender_email = input("Type your email address and press enter: ")
    password = input("Type your password and press enter:")
    receiver_email = input("Type reciever's email address and press enter: ")
    if validate_email(sender_email) and validate_email(receiver_email):
        s = TimestampSigner(SECRET_KEY)
        otp = temp_otp()
        message = f"""\nThis message is sent from Python for Email Id Verification, by prateek-manocha.\n\
The OTP is {s.unsign(otp).decode()}"""
        send_email(sender_email, password, receiver_email, message)
        print("Verification email sent succesfully.")
