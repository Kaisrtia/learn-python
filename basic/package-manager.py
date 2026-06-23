# python -m venv .venv
# .venv\Scripts\activate (window)
# source .venv/bin/activate (ubuntu)
# pip install cowsay

import cowsay
name = "Hoang Trung"
cowsay.cow(f"Hello, {name}!")
cowsay.trex(f"Hello, {name}!")