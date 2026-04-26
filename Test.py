import csv
import random
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)

# Sample data
first_names = ["Emma", "Liam", "Ava", "Noah", "Sophia", "Mason", "Isabella", "Ethan", "Mia", "Alexander"]
last_names = ["Johnson", "Smith", "Brown", "Davis", "Wilson", "Taylor", "Martinez", "Anderson", "Thomas", "Lee"]
genders = ["Male", "Female"]
countries = ["USA", "Canada", "UK", "Australia", "Germany", "Mexico", "France", "Italy", "Japan", "Brazil"]
movie_genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Thriller", "Sci-Fi", "Documentary", "Fantasy"]
devices = ["Phone", "TV", "Computer"]
second_screen_options = ["Yes", "No"]

# Function to generate random date
def random_date(start_year=2017, end_year=2023):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# CSV header
header = [
    "First Name", "Last Name", "Age", "Gender", "Country of Residence",
    "Favorite Movie Genre", "Least Favorite Movie Genre", "Hours of Netflix per Month",
    "Device", "Date Subscribed", "Ever Unsubscribed", "Date Unsubscribed",
    "Date Resubscribed", "Uses Second Screen"
]

# Generate 100 entries
rows = []
for _ in range(100):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    age = random.randint(18, 50)
    gender = random.choice(genders)
    country = random.choice(countries)
    fav_genre = random.choice(movie_genres)
    least_genre = random.choice([g for g in movie_genres if g != fav_genre])
    hours_netflix = random.randint(5, 100)
    device = random.choice(devices)
    
    # Generate subscription date first
    date_subscribed = random_date()
    
    ever_unsubscribed = random.choice(["Yes", "No"])
    
    if ever_unsubscribed == "Yes":
        # Unsubscribed date must be after subscription date
        date_unsubscribed = random_date(start_year=date_subscribed.year, end_year=2023)
        # Resubscribe date must be after unsubscribed date
        date_resubscribed = random_date(start_year=date_unsubscribed.year, end_year=2023)
        date_unsubscribed_str = date_unsubscribed.strftime("%Y-%m-%d")
        date_resubscribed_str = date_resubscribed.strftime("%Y-%m-%d")
    else:
        date_unsubscribed_str = ""
        date_resubscribed_str = ""
    
    uses_second_screen = random.choice(second_screen_options)
    
    rows.append([
        first_name, last_name, age, gender, country, fav_genre, least_genre, hours_netflix,
        device, date_subscribed.strftime("%Y-%m-%d"), ever_unsubscribed,
        date_unsubscribed_str, date_resubscribed_str, uses_second_screen
    ])

# Write to CSV
with open("netflix_users_100.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("CSV file 'netflix_users_100.csv' created successfully!")