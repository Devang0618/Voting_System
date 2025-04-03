import matplotlib.pyplot as plt

def display_menu():
    print("\nVote for your favorite party:")
    for i, party in enumerate(parties, 1):
        print(f"{i}. {party}")
    print("0. Exit and show results")

def cast_vote():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(parties):
                votes[parties[choice - 1]] += 1
                print(f"Vote casted for {parties[choice - 1]}!\n")
            else:
                print("Invalid choice! Try again.\n")
        except ValueError:
            print("Please enter a valid number!\n")

def show_results():
    print("\nElection Results:")
    for party, count in votes.items():
        print(f"{party}: {count} votes")
    
    # Visualization using matplotlib
    plt.bar(votes.keys(), votes.values(), color=['blue', 'red', 'green', 'orange'])
    plt.xlabel("Parties")
    plt.ylabel("Number of Votes")
    plt.title("Election Results Visualization")
    plt.show()

# List of parties
parties = ["Party A", "Party B", "Party C", "Party D"]
votes = {party: 0 for party in parties}  # Initialize votes

# Start voting
cast_vote()

# Show results
show_results()
