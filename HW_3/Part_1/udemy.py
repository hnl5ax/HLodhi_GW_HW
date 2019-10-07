import os
import csv

udemy_csv = os.path.join("..","Resources", "web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
length = []
review_percent = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        # YOUR CODE HERE
        title.append(row[1])
        # Add price
        # YOUR CODE HERE
        price.append(row[4])
        # Add number of subscribers
        # YOUR CODE HERE
        subscribers.append(row[5])
        # Add amount of reviews
        # YOUR CODE HERE
        reviews.append(row[6])
        # Determine percent of review left to 2 decimal places
        # YOUR CODE HERE
        percent = round(int(row[6])/ int(row[5]), 2)
        review_percent.append(percent)
        # Get length of the course to just a number
        # YOUR CODE HERE
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))
# Zip lists together
# YOUR CODE HERE
zipped_data = zip(title,price, subscribers, reviews, review_percent, new_length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    # YOUR CODE HERE
    writer.writerows(zipped_data)