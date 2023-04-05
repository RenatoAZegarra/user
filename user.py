class User:
    def __init__(self,first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {'Yes' if self.is_rewards_member else 'No'}")
        print(f"Gold Card Points: {self.gold_card_points}")
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Error: Not enough points to spend.")
        else:
            self.gold_card_points -= amount

# Create a user instance and call the display_info method
user1 = User("Brandon", "Roy", "broy@gmail.com", 30)
user1.display_info()
print("----------------")

# Call the enroll method on the user instance
user1.enroll()

# Create two more instances of the User class
user2 = User("Jane", "Smith", "janeS@gmail.com", 25)
user3 = User("Bob", "List", "boblist@gmail.com", 40, True, 500)

# Have the first user spend 50 points
user1.spend_points(50)

# Have the second user enroll and spend 80 points
user2.enroll()
user2.spend_points(80)

# Call the display_info method on all the users
user1.display_info()
print("----------------")
user2.display_info()
print("----------------")
user3.display_info()
print("----------------")

# Try to re-enroll the first user (bonus)
user1.enroll()
print("----------------")

# Try to spend more points than available for the third user (bonus)
user3.spend_points(700)
print("----------------")
