# Python Program for simple OTP generator
# ver 2

import random as r

print("6 digit OTP Generator")
print()
print("generate otp? y/n")

answer = input()
if answer == "y" :
  def otpgen() :
    otp = ""
    for i in range(6):
      otp+=str(r.randint(0,9))
    print("Your OTP is: ")
    print(otp)

  otpgen()
else :
  print("ok")
