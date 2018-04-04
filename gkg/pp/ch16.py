# Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new
# password. Include your run-time code in a main method.

import random as rn


class PassWordGenerator:
    """
    A class to generate passwords
    """

    def __init__(self, strength):
        self.strength = strength
        self.string = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    def generatePassword(self):
        password = "".join(rn.sample(self.string, self.strength))
        return password


pwdGen = PassWordGenerator(10)
print(pwdGen.generatePassword())