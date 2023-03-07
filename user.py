class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        print("User already a member")
        return False

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"Current point value - {self.gold_card_points}")
            return self
        print ("Not enough points")

User_1 = User("Chase", "Matherly", "email@gmail.com", 25)
User_1.enroll()
User_2 = User("Mario", "Mario", "mario@email.com", 45)
User_3 = User("Luigi", "Mario", "luigi@email.com", 40)

User_1.spend_points(50)
User_2.enroll()
User_2.spend_points(80)

User_1.display_info()
User_2.display_info()
User_3.display_info()

User_1.enroll()
User_3.spend_points(40)