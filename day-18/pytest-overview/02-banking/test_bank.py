# test_bank.py

import pytest
from bank import BankAccount, InsufficientFundsError, NegativeAmountError

@pytest.fixture
def alice_account():
    return BankAccount("Alice", 100.0)

@pytest.fixture
def bob_account():
    return BankAccount("Bob", 50.0)

def test_initial_balance():
    acc = BankAccount("John", 200)
    assert acc.balance == 200

def test_negative_initial_balance():
    with pytest.raises(NegativeAmountError):
        BankAccount("Negative", -10)

def test_deposit(alice_account):
    alice_account.deposit(50)
    assert alice_account.balance == 150

def test_deposit_negative(alice_account):
    with pytest.raises(NegativeAmountError):
        alice_account.deposit(-20)

def test_withdraw_success(alice_account):
    alice_account.withdraw(30)
    assert alice_account.balance == 70

def test_withdraw_insufficient_funds(alice_account):
    with pytest.raises(InsufficientFundsError):
        alice_account.withdraw(200)

def test_withdraw_negative(alice_account):
    with pytest.raises(NegativeAmountError):
        alice_account.withdraw(-5)

def test_transfer_success(alice_account, bob_account):
    alice_account.transfer_to(bob_account, 30)
    assert alice_account.balance == 70
    assert bob_account.balance == 80

def test_transfer_insufficient_funds(alice_account, bob_account):
    with pytest.raises(InsufficientFundsError):
        alice_account.transfer_to(bob_account, 1000)
