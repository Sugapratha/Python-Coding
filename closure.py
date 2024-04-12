def create_counter():
    count = 67
    
    def increment():
        nonlocal count
        count += 1
        print("Incremented. Count is now:", count)
    
    def decrement():
        nonlocal count
        count -= 1
        print("Decremented. Count is now:", count)
    
    def get_count():
        return count
    
    return increment, decrement, get_count

# Create a counter
increment_counter, decrement_counter, get_count = create_counter()

# Test the counter
increment_counter()  # Increment
increment_counter()  # Increment
decrement_counter()  # Decrement
print("Current count:", get_count())  # Get current count
