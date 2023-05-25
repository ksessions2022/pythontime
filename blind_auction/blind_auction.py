#!/usr/bin/python3

import os
from art import gavel, winner_face
raffle = {}
are_there_more_bidders = 'yes'
highest_bid = 0

# This function will prompt for bidder name and price and if there are more bidders
def gather_bidder_information():
    global are_there_more_bidders
    while are_there_more_bidders == 'yes':
        bidder_name = input("What is your name?: ")
        bid = float((input("What's your bid?: $")))
        are_there_more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
        add_bids_to_dictionary(bidder_name, bid)
    find_the_largest_bid()

#This function adds bidder and the bid to a dictionary
def add_bids_to_dictionary(name, price):
    raffle[name] = price
    os.system('clear')

def find_the_largest_bid():
    global highest_bid
    for bids_made in raffle:
        if (raffle[bids_made] > highest_bid):
            highest_bid = raffle[bids_made]
    for key, value in raffle.items():
        if value == highest_bid:
            winning_bid = key
    highest_bid = "{:.2f}".format(highest_bid)
    print(f"The winner is {winning_bid} with a bid of ${highest_bid}")
    print(winner_face)

#Start of script
print("Welcome to the secret auction program.")
print(gavel)
gather_bidder_information()