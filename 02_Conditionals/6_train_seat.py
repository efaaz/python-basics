"""Problem: Train seat selector
Prompt the user to enter a seat type: sleeper, AC, general, or luxury (case-
insensitive). Use match/case (pattern matching) to print a short description
for each seat type. If the input doesn't match any known type, print an
"Invalid seat type" message.
"""

seatType = input("Enter your seat type (sleeper/AC/general/luxury): ")
match seatType:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "AC":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")
