# Constants
NUM_JOURNEYS = 4
NUM_COACHES_NORMAL = 6
NUM_COACHES_LAST_TRAIN = 8
SEATS_PER_COACH = 80
TICKET_PRICE = 25

# Initialize data structures
passengers_count_up = [0] * NUM_JOURNEYS
revenue_up = [0] * NUM_JOURNEYS
passengers_count_down = [0] * NUM_JOURNEYS
revenue_down = [0] * NUM_JOURNEYS

# Function to display the initial screen
def display_initial_screen():
    print("Electric Mountain Railway - Start of the Day")
    print("\nTrain Journey\tDeparture Time\t\tReturn Time\tSeats Available")
    print("-" * 70)

    for journey in range(NUM_JOURNEYS):
        departure_time = 9 + 2 * journey
        return_time = 10 + 2 * journey
        seats_available = NUM_COACHES_NORMAL * NUM_COACHES_LAST_TRAIN * SEATS_PER_COACH

        print(f"Journey {journey + 1}\t\t{departure_time:02}:00 AM\t\t{return_time:02}:00 AM\t\t{seats_available}")

# Display the initial screen
display_initial_screen()
