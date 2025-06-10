# Switch Case Statement

# Practise Example
weekName = 'Sunday'

match weekName:
    case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' :
        print("Weekday")
    case 'Saturday' | 'Sunday' :
        print('Weekend')
    case _ :
        print('No match found') 