import gspread
from google.oauth2.service_account import Credentials

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
    print("Please enter the amount of each book sold yesterday.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

    def validate_data(values):
    """
    Used to convert all string values into integers.
    If strings cannot be converted into int, 
    or if there aren't exactly 6 values,
    with raise error message
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values are required, you input {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try inputing the correct data.\n")


get_sold_data()