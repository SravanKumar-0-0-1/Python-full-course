#match-case statements(SWITCH): An alternative to using many "elif" statements 
#                               Execute some code if a values matches a case:
#                               Benefits:cleaner and syntax is more readable.

def is_weekend(day):
    match day:
        case "saturday"| "sunday":
            print("just chill")
            return "its a good day"
        case "monday"| "tuesday"|"wednesday"|"thursday"|"friday":
            return "its a bad day"
        case _:
            return "no day"
print(is_weekend("sunday"))