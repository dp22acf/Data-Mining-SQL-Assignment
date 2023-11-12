# -*- coding: utf-8 -*-
"""
@author: Durga
"""

import pandas as pd
import random
import string
from datetime import datetime, timedelta


# Number of samples
n = 1000


# Nominal data: customer ids Generate 1000 random unique ID values
customer_id = random.sample(range(2200001, 3300021), n)


# List of first names and last names,address_id
first_names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Frank",
    "Grace",
    "Henry",
    "Ivy",
    "Jack",
]
last_names = [
    "Smith",
    "Johnson",
    "Brown",
    "Lee",
    "Garcia",
    "Davis",
    "Martinez",
    "Jackson",
    "Lopez",
    "Hill",
]
address_id_set = [
    "A123",
    "B234",
    "C345",
    "D456",
    "E567",
    "F678",
    "G789",
    "H890",
    "I901",
    "J012",
]
address_data = {
    "Address_ID": [
        "A123",
        "B234",
        "C345",
        "D456",
        "E567",
        "F678",
        "G789",
        "H890",
        "I901",
        "J012",
    ],
    "Address": [
        "123 Main St, Springfield, IL 62701",
        "456 Elm St, Rivertown, CA 90210",
        "789 Oak St, Lakeside, TX 75001",
        "101 Pine St, Mountainview, AZ 85001",
        "202 Cedar St, Seaville, FL 33101",
        "303 Maple St, Greentown, OH 44301",
        "404 Birch St, Hilltop, NY 10001",
        "505 Walnut St, Lakeshore, PA 19001",
        "606 Cherry St, Woodland, WA 98601",
        "707 Spruce St, Hillcrest, CO 80201",
    ],
    "City": [
        "Springfield",
        "Rivertown",
        "Lakeside",
        "Mountainview",
        "Seaville",
        "Greentown",
        "Hilltop",
        "Lakeshore",
        "Woodland",
        "Hillcrest",
    ],
    "PostCode": [
        "IL 62701",
        "CA 90210",
        "TX 75001",
        "AZ 85001",
        "FL 33101",
        "OH 44301",
        "NY 10001",
        "PA 19001",
        "WA 98601",
        "CO 80201",
    ],
}
policy_provider = ["BUPA", "Aviva", "AXA PPP", "WPA", "Saga"]
policy_status = ["Active", "Closed"]

# Nominal Data: Generate 1000 random names
random_names = [
    random.choice(first_names) + " " + random.choice(last_names) for i in range(n)
]

# Ordinal Data: Generate 1000 random address_ids
random_address_ids = [random.choice(address_id_set) for i in range(n)]


#
# Function to generate a random address ID
def generate_address_id(length=10):
    # Pool of characters to choose from (alphanumeric)
    characters = (
        "1001",
        "1002",
        "1003",
        "1004",
        "1005",
        "1006",
        "1007",
        "1008",
        "1009",
        "1010",
    )
    address_id = "".join(random.choice(characters) for _ in range(1))
    return address_id


# Function to generate a random policy number
def generate_policy_number(length=8):
    # Pool of characters to choose from (letters and digits)
    characters = string.ascii_uppercase + string.digits
    policy_number = "".join(random.choice(characters) for _ in range(length))
    return policy_number


# Nominal Data: Generate 100 random policy numbers
num_policy_numbers = n
policy_numbers = [generate_policy_number() for _ in range(num_policy_numbers)]


# Ratio Data: Generate 100 random ages between 18 and 65
random_ages = [random.randint(18, 65) for _ in range(n)]


# Nominal Data: Function to generate a random phone number
def generate_phone_number():
    # Generate a random 10-digit phone number
    phone_number = "07"  # Country code (assuming it's the United States)
    phone_number += "".join(
        random.choices("0123456789", k=8)
    )  # Generate 9 random digits
    return phone_number


# Generate 10 random phone numbers
num_phone_numbers = n
phone_numbers = [generate_phone_number() for _ in range(num_phone_numbers)]


# List of gender options
genders = ["Male", "Female", "Other", "Prefer not to say"]

# Nominal Data: Generate 10 random gender values
random_genders = [random.choice(genders) for _ in range(n)]


# Create DataFrame
df_customer = pd.DataFrame(
    {
        "CustomerID": customer_id,
        "AddressID": random_address_ids,
        "PolicyNumber": policy_numbers,
        "Customer_Name": random_names,
        "Age": random_ages,
        "Phone_Number": phone_numbers,
        "Gender": random_genders,
    }
)

# Example index
df_customer.set_index("CustomerID")

# df_customer_information = df[['Customer ID', 'Address_ID', 'Policy_Number', 'Customer_Name', 'Age', 'Phone_Number', 'Gender']]

# Save the DataFrame to a CSV file with the specified file path
df_customer.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Durga\Customer_table.csv",
    index=False,
)


df_address = pd.DataFrame(address_data)


# Save the DataFrame to a CSV file with the specified file path
df_address.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Durga\Address_table.csv",
    index=False,
)


# Generate 1000 random providernames
random_providers = [random.choice(policy_provider) for i in range(n)]


random_policy_status = [random.choice(policy_status) for i in range(n)]

# Function to generate a random date within a specific range
def generate_random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


# Define start and end dates
start_date = datetime(2000, 1, 1)
end_date = datetime(2045, 12, 31)

# Number of random date pairs to generate
num_pairs = n

# Interval Data: Generate random begin and end dates
begin_dates = [generate_random_date(start_date, end_date) for _ in range(num_pairs)]
end_dates = [generate_random_date(begin_date, end_date) for begin_date in begin_dates]

# Create a DataFrame
data = {"Begin Date": begin_dates, "End Date": end_dates}
df_policy = pd.DataFrame(
    {
        "PolicyNumber": policy_numbers,
        "PolicyProvider": random_providers,
        "Policy Sataus": random_policy_status,
        "Begin_Date": begin_dates,
        "End Date": end_dates,
    }
)

# Save the DataFrame to a CSV file with the specified file path
df_policy.to_csv(
    r"C:\Users\manoj\OneDrive\Documents\SQL Assigment - Durga\Policy_table.csv",
    index=False,
)
