import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('thunderbird_and_whale')

def get_sold_data():
    """
    Get amount of sold books figures input from the user.
    """
    while True:
        print("Please enter the amount of each book sold yesterday.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here: ")
        sold_data = data_str.split(",")

        if valid_data(sold_data):
            print("Thankyou from T&W! This information is valid.")

            break

    return sold_data


def valid_data(values):
    """
    Inside try will convert all string values into integers.
    Alert error message if data cannot be converted into int,
    or if there aren't 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, input valid data.\n")
        return False

    return True


def update_worksheet(data, worksheet):
    """
    Updats the relevant worksheet with the user input data
    """
    print(f"Hold on! just updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")
    print("We can now use this to calculate next weeks orders... \n")
    print("you're a great help! \n")

def calculate_difference_data(sold_row):
    """
    Function to calculate the difference,
    between the amount of books sold,
    and the amount of books ordered

    """
    print("Gathering the difference of sales and orders... \n")
    ordered = SHEET.worksheet("ordered").get_all_values()
    ordered_row = ordered[-1]
    
    difference_data = []
    for ordered, sold in zip(ordered_row, sold_row):
        difference = int(ordered) - sold
        difference_data.append(difference)
    
    return difference_data

def get_last_5_entries_sold():
    """
    Retrieves columns of data from sold worksheet, collecting
    the last 5 entries for each bought book and returns
    as a list.
    """
    sold = SHEET.worksheet("sold")

    columns = []
    for ind in range(1, 7):
        column = sold.col_values(ind)
        columns.append(column[-5:])
    
    return columns

def calculate_ordered_data(data):
    """ 
    Calculate average amount ordered of each book,
    adding 10% to round as half a book cannot be ordered
    """
    print("Calculating data of ordered books...\n")
    new_ordered_data = []

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        ordered_num = average * 1.1
        new_ordered_data.append(round(ordered_num))

    return new_ordered_data

def main():
    """
    Call functions created
    """
    data = get_sold_data()
    sold_data = [int(num) for num in data]
    update_worksheet(sold_data, "sold")
    new_difference_data = calculate_difference_data(sold_data)
    update_worksheet(new_difference_data, "difference")
    sold_columns = get_last_5_entries_sold() 
    ordered_data = calculate_ordered_data(sold_columns)
    print(ordered_data)

print("Welcome to Thunderbird and Whale! \n")
print("We're a cozy bookstore in Forks however we get alot of customers! \n")
print("It can be hard to keep up with orders... \n")
print("Which is why we need your help! \n")
print("We need to know how many orders of books we need everyday! \n")
print("So lets get started! \n")
main()



