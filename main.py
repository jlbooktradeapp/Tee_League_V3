# This is the second versions of Tee Leagues
# This is the backend for any future front end deployment

import gspread
import schedule
import pymongo
import csv



# Connecting Python to SGA Data Sheet

sa = gspread.service_account(filename="service_account.json")
sh = sa.open("Sunnyvale Player Stats 2023")

# Setting Each Data and Extrap Sheet to variables for Front Sheet and each player

sga_totals = sh.worksheet("All SGA Total Stats")

john_data = sh.worksheet("John Stats Entry Data")
john_data_pulled = john_data.get_all_records()
john_extrap = sh.worksheet("John Stats Extrapolation")

colin_data = sh.worksheet("Colin Stats Entry Data")
colin_data_pulled = colin_data.get_all_records()
colin_extrap = sh.worksheet("Colin Stats Extrapolation")

chris_data = sh.worksheet("Chris Stats Entry Data")
chris_data_pulled = chris_data.get_all_records()
chris_extrap = sh.worksheet("Chris Stats Extrapolation")

cam_data = sh.worksheet("Cam Stats Entry Data")
cam_data_pulled = cam_data.get_all_records()
cam_extrap = sh.worksheet("Cam Stats Extrapolation")

austin_data = sh.worksheet("Austin Stats Entry Data")
austin_data_pulled = austin_data.get_all_records()
austin_extrap = sh.worksheet("Austin Stats Extrapolation")

jeff_data = sh.worksheet("Jeff Player Stat Entry")
jeff_data_pulled = jeff_data.get_all_records()
jeff_extrap = sh.worksheet("Jeff Stat Extrapolation")

justin_data = sh.worksheet("Justin Stats Entry Data")
justin_data_pulled = justin_data.get_all_records()
justin_extrap = sh.worksheet("Justin Stats Extrapolation")

kevin_data = sh.worksheet("Kevin Stats Entry Data")
kevin_data_pulled = kevin_data.get_all_records()
kevin_extrap = sh.worksheet("Kevin Stats Extrapolation")

moffa_data = sh.worksheet("Moffa Stats Entry Data")
moffa_data_pulled = moffa_data.get_all_records()
moffa_extrap = sh.worksheet("Moffa Stats Extrapolation")

ian_data = sh.worksheet("Ian Stat Entry Data")
ian_data_pulled = ian_data.get_all_records()
ian_extrap = sh.worksheet("Ian Stat Extrapolation")

sean_data = sh.worksheet("Sean Stat Entry Data")
sean_data_pulled = sean_data.get_all_records()
sean_extrap = sh.worksheet("Sean Stat Extrapolation")

import csv

r = 0
players = ["John", "Colin", "Chris", "Cam", "Austin", "Kevin", "Jeff", "Justin", "Ian", "Sean", "Moffa"]
players_data = [john_data_pulled, colin_data_pulled, chris_data_pulled, cam_data_pulled, austin_data_pulled, kevin_data_pulled, jeff_data_pulled, justin_data_pulled, ian_data_pulled, sean_data_pulled, moffa_data_pulled]
column_headers = ["Timestamp", "Date of Match Played", "Type of Match", "League Members Present to Validate Score",
                  "Course Played", "Par of Course Played", "Your Total Score", "+/- Par (Score-Par)",
                  "Win? (Score-SGA Handicap)", "Number of Pars", "Number of Birdies", "Number of Eagles",
                  "Number of 25+ Foot Putts", "Number of Chip In's", "Number of Balls Lost", "Email Address"]


for player in players:
    player_data = players_data[r]  # Replace this with your function to retrieve the data set for each player
    total_rounds = len(players_data)
    print(total_rounds)

    filename = f"{player}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=column_headers)
        writer.writeheader()
        for round_data in player_data:
            writer.writerow(round_data)
        print(r)
    if r < total_rounds:
        r = r + 1
    else:
        break

def advanced_stats(filename, advanced_filename):
    wins = 0
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Type of Match'] == 'Exhibition' and row['Win? (Score-SGA Handicap)'] == 'TRUE':
                wins += 1
    with open(advanced_filename, 'w', newline='') as f:
        fieldnames = ['Exhibition Wins']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Exhibition Wins': wins})

for player in players:
    filename = f"{player}.csv"
    advanced_filename = f"{player}_advanced.csv"
    advanced_stats(filename, advanced_filename)

exwinstotal = 0

for player in players:
    filename = f"{player}_advanced.csv"
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row
        for row in reader:
            exwinstotal = int(row[0])

            if player == 'John':
                print(f"John Wins {exwinstotal}")
                sga_totals.update('G2', exwinstotal)
            elif player == 'Colin':

                print(f"Colin Wins {exwinstotal}")
                sga_totals.update('G3', exwinstotal)
            elif player == 'Chris':
                print(f"Chris Wins {exwinstotal}")
                sga_totals.update('G4', exwinstotal)
            elif player == 'Cam':
                print(f"Cam Wins {exwinstotal}")
                sga_totals.update('G5', exwinstotal)
            elif player == 'Austin':
                print(f"Austin Wins {exwinstotal}")
                sga_totals.update('G6', exwinstotal)
            elif player == 'Kevin':
                print(f"Kevin Wins {exwinstotal}")
                sga_totals.update('G9', exwinstotal)
            elif player == 'Jeff':
                print(f"Jeff Wins {exwinstotal}")
                sga_totals.update('G7', exwinstotal)
            elif player == 'Justin':
                print(f"Justin Wins {exwinstotal}")
                sga_totals.update('G8', exwinstotal)
            elif player == 'Ian':
                print(f"Ian Wins {exwinstotal}")
                sga_totals.update('G11', exwinstotal)
            elif player == 'Sean':
                print(f"Sean Wins {exwinstotal}")
                sga_totals.update('G12', exwinstotal)
            elif player == 'Moffa':
                print(f"Moffa Wins {exwinstotal}")
                sga_totals.update('G10', exwinstotal)




