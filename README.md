# ConfirmationCalculator
Calculate a recommended number of confirmations for Cryptocurrency-Transactions, based on the cost of the product and the cost of an attack.

## Background
Recently the website [https://www.crypto51.app/](https://www.crypto51.app/) went up, listing the cost of inflicting a 51% attack on a number of popular CryptoCurrencies for one hour.
Such an attack allows an attacker to block all transactions on the network for that time period as well as reverse recent transactions, the latter of which is of importance for merchants and exchanges.

## What is the purpose of this program?
This program aims to provide merchants guidance in choose how long they should wait until they can assume that a transaction they recieved will not be reversed by such an attack.
It is based on the idea that it would be uneconimical for the attacker to invest the resources to reverse a transaction if the cost of those resources is higher than the cost of the product.

## How to run
This program is written in Python3 an such can be run on any Computer with the Python interpreter installed. It comes by default on most Linux Distros.

If you don't have the interpreter installed there are a number of online environments available, such as [repl.it](https://repl.it/languages/Python3).

Just copy the code from the confirmations.py file into the text field of repl.it, press run and follow the commands on the right.
