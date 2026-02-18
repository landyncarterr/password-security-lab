# Password Security Lab (Python)

## Overview

Password Security Lab is a defensive security tool built in Python to demonstrate secure password handling practices.
This project focuses on **password hashing, verification, strength analysis, and benchmarking** using modern security standards.

The goal of this project is educational — to understand how secure authentication works, not to break passwords.

---

## Features

* 🔐 Hash passwords using Argon2
* ✅ Verify passwords against stored hashes
* 🧠 Analyze password strength
* ⏱ Benchmark hashing speed
* 🎨 Colored terminal output for readability

---

## Why This Matters (Security Concepts)

Instead of storing plain text passwords, modern systems store **hashed passwords**.
This protects users if a database is leaked.

This project demonstrates:

* Slow hashing (Argon2)
* Secure verification methods
* Password strength evaluation
* Defensive security practices

---

## Installation

Clone or download the project, then:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install passlib[argon2] zxcvbn colorama
```

---

## Usage

### Hash a password

```bash
python pslab.py hash
```

### Verify a password

```bash
python pslab.py verify
```

### Check password strength

```bash
python pslab.py strength
```

### Run benchmark

```bash
python pslab.py benchmark
```

---

## Example Output

Strength results are color-coded:

* Red = weak password
* Yellow = moderate
* Green = strong

---

## Disclaimer

This tool is intended for **educational and ethical cybersecurity learning only**.
It is designed to demonstrate defensive password security concepts.

---

## Author

Landyn Carter

