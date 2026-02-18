#!/usr/bin/env python3

import argparse
import getpass
import time

from passlib.context import CryptContext
from zxcvbn import zxcvbn
from colorama import Fore, Style, init

init(autoreset=True)

pwd_context = CryptContext(
	schemes=["argon2"],
	deprecated="auto"
)

def hash_password():
	password = getpass.getpass("Enter password to hash: ")
	hashed = pwd_context.hash(password)
	print("\nGenerated hash:\n")
	print(hashed)

def verify_password():
	password = getpass.getpass("Enter password to verify: ")
	stored_hash = input("Paste stored hash: ")
	if pwd_context.verify(password, stored_hash):
		print("\nPassword is correct.")
	else:
		print("\nPassword does NOT match.")

def check_strength():
	password = getpass.getpass("Enter password to analyze: ")
	result = zxcvbn(password)
	score = result["score"]

	if score <=1:
		color = Fore.RED
	elif score == 2:
		color = Fore.YELLOW
	else:
		color = Fore.GREEN
	print(color + "\nStrength score (0-4):" + str(score))
	print("Estimated crack time:",
		result["crack_times_display"]["offline_slow_hashing_1e4_per_second"])
	print("\nFeedback:")
	print(result["feedback"]["warning"])
	for s in result["feedback"]["suggestions"]:
		print("-",s)

def benchmark():
	password = "BenchmarkPassword123!"
	print("\nRunning hash speed test...")
	start = time.time()
	for _ in range(5):
		pwd_context.hash(password)
	end = time.time()
	print(f"Time or 5 hashes: {round(end-start, 2)} seconds")

def main():
	parser = argparse.ArgumentParser(
		description="Password Security Lab Tool"
	)
	parser.add_argument(
	"command",
	choices=["hash", "verify", "strength", "benchmark"],
	help="Choose a function to run"
	)
	args = parser.parse_args()
	if args.command == "hash":
		hash_password()
	elif args.command == "verify":
		verify_password()
	elif args.command == "strength":
		check_strength()
	elif args.command == "benchmark":
		benchmark()

if __name__ == "__main__":
	main()
    
   	
