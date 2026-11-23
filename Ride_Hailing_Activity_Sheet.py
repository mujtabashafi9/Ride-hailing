import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
ride = pd.read_csv("ride_hailing_dataset.csv")
print(ride.head())

# Q1: Average fare by service type
fare_by_service = ride.groupby("service_type")["fare"].mean()
print("Average fare by service type:")
print(fare_by_service.round(2))

# Q2: City with the most trips
trips_by_city = ride["city"].value_counts()
print("Number of trips by city:")
print(trips_by_city)
print("City with the most trips:", trips_by_city.idxmax())

# Q3: Average distance per trip
average_distance = ride["distance_km"].mean()
print("Average distance per trip (km):", round(average_distance, 2))

# Q4: Compare trip ratings by gender
ratings_by_gender = ride.groupby("gender")["trip_rating"].mean()
print("Average trip rating by gender:")
print(ratings_by_gender.round(2))

# Q5: Bar chart of service type vs average fare
plt.figure(figsize=(8, 5))
plt.bar(fare_by_service.index, fare_by_service.values)
plt.title("Average Fare by Service Type")
plt.xlabel("Service Type")
plt.ylabel("Average Fare")
plt.tight_layout()
plt.show()
