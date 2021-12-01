import random
import sys

secret_min = 0
secret_max = 100
secret_number = random.randint(secret_min,secret_max)
num_guesses = 0

def main():
	print(f"I'm thinking of a secret number between {secret_min} and {secret_max}. What is it?")

	for line in sys.stdin:
		if line.rstrip() == 'q':
			print(f"That's ok, I still like you. The number was {secret_number}")
			break
		
		if not try_one_guess(line):
			break

	print("Goodbye.")

def try_one_guess(line):
	global num_guesses
	try: 
		guess = int(line.rstrip())
		num_guesses += 1
		if guess < secret_number:
			print(f"Your guess #{num_guesses} is too LOW.")
			return True
		elif guess > secret_number:
			print(f"Your guess #{num_guesses} is too HIGH.")		
			return True
		else:
			print(f"That's right! It took you {num_guesses} guesses")
			return False
	except ValueError:
		print("Please type an integer, or 'q' to quit")
		return True

if __name__ == "__main__":
  main()