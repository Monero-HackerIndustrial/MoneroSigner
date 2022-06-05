import monero

from monero.seed import Seed

s = Seed()

# from wordlists https://github.com/monero-project/monero/tree/master/src/mnemonics

phrase = s.phrase

print(f"The seed Phrase:")
print(f"{phrase}")


# Generating Seeds from hex strings
hex = monero.seed.generate_random_hex()
s = Seed(hex)
phrase = s.phrase

print(f"The seed Phrase:")
print(f"{phrase}")


#Generating with random bytes from system
import os
hex = os.urandom(32)

phrase = s.phrase

print(f"The seed Phrase:")
print(f"{phrase}")

# Generating from dice rolls. This is simulated dice rolls
import random
import hashlib


dice_rolls = ""

for i in range(0,99):
    #This is not truly random. This is to simulate dicerolls
    #DONT USE IN PROD
    dice_rolls += str(random.randint(0,5))

#Generated 32 bytes of entropy
entropy_bytes = hashlib.sha256(dice_rolls.encode()).digest()

hex = entropy_bytes

phrase = s.phrase

print(f"The seed Phrase:")
print(f"{phrase}")
