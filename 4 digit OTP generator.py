import math, random

print("4 digit OTP Generator")
print()
print("generate otp? y/n")

answer = input()

if answer == "y" :
  def generateOTP() :
    digits = "0123456789"
    OTP = ""

    for i in range(4) :
     OTP += digits[math.floor(random.random() * 10)]

    return OTP

  if __name__ == "__main__" :
    print("OTP of 4 digits: ", generateOTP())
else :
  print("ok")
