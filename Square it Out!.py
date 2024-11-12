def get_square_values(start, end):
    squares = {}
    for number in range(start, end + 1):
        square = number ** 2
        if square % 2 == 0:
            squares.setdefault('even', []).append(square)
        else:
            squares.setdefault('odd', []).append(square)
    return squares

def main():
    print("Welcome to the Square Values Program!")
    
    # Get user input for the range
    try:
        start = int(input("Enter the start of the range (inclusive): "))
        end = int(input("Enter the end of the range (inclusive): "))
        
        if start > end:
            print("Invalid range. Start should be less than or equal to end.")
            return
        
        # Get the square values and separate them
        squares = get_square_values(start, end)
        
        # Display the results
        print("\nSquare values:")
        print("Even squares:", squares.get('even', []))
        print("Odd squares:", squares.get('odd', []))
        
    except ValueError:
        print("Please enter valid integers for the range.")

if __name__ == "__main__":
    main()