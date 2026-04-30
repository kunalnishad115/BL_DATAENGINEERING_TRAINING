# test_sanitize.py
import pytest as p
from task5 import sanitize_input, InputSanitizationError



def test_valid_name():
    assert sanitize_input("Kunal*!") == "Kunal"



def test_payment_text():
    assert sanitize_input("Payment: 100$") == "Payment 100"



def test_empty_cleaned_text():
    with p.raises(InputSanitizationError, match="Cleaned text is empty"):
        sanitize_input("!@#$%")