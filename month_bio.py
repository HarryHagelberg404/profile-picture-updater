from datetime import datetime

def months_passed(current_date):
    current_month = current_date.month
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    result = 'The current month:'
    for i in range(12):
        if (i) < current_month:
            result += '|'
        else:
            result += '-'
    return result

# Example usage:
# current_date = datetime.now()
# print(months_passed(current_date))