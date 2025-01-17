import random
import matplotlib.pyplot as plt

# Get user input for the auction parameters such as the numbers of bidders participating, the base price of the land, increasing price every round
num_bidders = int(input("Enter the number of bidders: "))
base_price = int(input("Enter the base price of the land: "))
increment = int(input("Enter the price increment per round: "))

# Generate bidders with user-defined or default strategies
print("\nStrategies: aggressive, cautious, bluffer, steady")
bidders = []
for i in range(num_bidders):
    strategy = input(f"Enter strategy for Bidder {i + 1}: ").strip().lower()
    budget = random.randint(base_price + 20000, base_price + 300000)
    bidders.append({"id": i + 1, "budget": budget, "strategy": strategy})

# Simulate the auction
def simulate_auction(base_price, increment, bidders):
    current_price = base_price
    active_bidders = bidders.copy()
    price_history = [current_price]  # To track price evolution
    rounds = 0  # Count the number of rounds

    print("\nStarting Auction:")
    while len(active_bidders) > 1:
        rounds += 1
        print(f"\nRound {rounds}:")
        
        for bidder in active_bidders.copy():
            if current_price > bidder["budget"]:
                print(f"Bidder {bidder['id']} has withdrawn (Budget: {bidder['budget']}).")
                active_bidders.remove(bidder)
                continue
            
            # Apply bidding strategies
            if bidder["strategy"] == "aggressive":
                current_price += increment
            elif bidder["strategy"] == "cautious" and random.random() > 0.5:
                current_price += increment
            elif bidder["strategy"] == "bluffer" and random.random() > 0.8:
                current_price += increment * random.randint(2, 4)  # Bluffing causes sudden spikes
            elif bidder["strategy"] == "steady":
                current_price += increment
            
            print(f"Bidder {bidder['id']} bids {current_price} (Budget: {bidder['budget']}).")

        # Remove bidders who exceed their budget
        active_bidders = [b for b in active_bidders if current_price <= b["budget"]]
        price_history.append(current_price)

    # Determine the winner
    if active_bidders:
        winner = active_bidders[0]
        print(f"\nWinner: Bidder {winner['id']} with a final bid of {current_price}.")
        return winner, current_price, price_history
    else:
        print("\nNo winner: All bidders withdrew.")
        return None, current_price, price_history

# Run the auction
winner, final_price, price_history = simulate_auction(base_price, increment, bidders)

# Visualize the auction price progression
plt.figure(figsize=(10, 6))
plt.plot(range(len(price_history)), price_history, marker="o", color="b", label="Bid Price")
plt.title("Auction Price Progression")
plt.xlabel("Rounds")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()
