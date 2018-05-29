##Calculate the number of confirmations necessary
## To make a 51% attack uneconomical
import math

blocktimeMinutes = 2 # in minutes
attackCostHour = 21000 #$
productCost = 500000 #$
margin = 2.0
baselineConfirmations = 6
print("Set the parameters for your currency, leave empty to choose the defaults")
i = input("\nBlocktime in Minutes(default="+str(blocktimeMinutes)+"):")
if i != "":
	blocktimeMinutes = float(i)
i = input("\nAttack cost per hour(default="+str(attackCostHour)+"):")
if i != "":
	attackCostHour = float(i)
i = input("\nCost of your product(default="+str(productCost)+"):")
if i != "":
	productCost = float(i)
i = input("\nmargin(default="+str(margin)+"):")
if i != "":
	margin = float(i)

print("\nDue to normal fluctuations in the network, it is recommended to wait for a few confirmations regardsless of an attack.")
i = input("Confirmation baseline(default="+str(baselineConfirmations)+"):")
if i != "":
	baselineConfirmations = float(i)

print("\n\n")
print("Note that the numbers provided by this program might not fit your business situation! If an attacker is able to buy multiple products at the same time for example, a attack might still be viable for them.")


recommendedConfirmations = productCost/(attackCostHour*(blocktimeMinutes/60))*margin + baselineConfirmations

print("Recommended number of Confirmations:", int(recommendedConfirmations))
delay = recommendedConfirmations*(blocktimeMinutes/60)
if delay > 1.1:
	print("Delay: ", delay, "h")
else:
	print("Delay: ", delay*60, "min")


