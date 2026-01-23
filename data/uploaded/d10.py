
# # Functions with outputs

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs. "
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# # formated_string = format_name("AnGElA", "Yu")
# formated_string = format_name("", "")
# print(formated_string)

# print(len("Angela"))



# any year any month given  find number of days
# if leap year february 29 days
# TODO 1: check leap year or not
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100:
            if year % 400:
                return True
            else:
                return False   
        else:
            return True  
    else:
        return False

def days_in_month(year, month):
    # docsting ( documentation of a function )
    """ Take a year and month and it provides the 
    number of days that month has. """
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return months_days[month-1]



# code here
year = int(input("Enter a Year : "))
month = int(input("Enter a month : "))

output = days_in_month(year, month)

print(f"The year {year} has {output} days in month {month}.")


























