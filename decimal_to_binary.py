def decimal_to_binary(decimal_num):
    """
    Converts a non-negative decimal integer to its binary string representation.

    This uses the principle of repeated division by 2 and tracking the remainders.

    Args:
        decimal_num (int): The non-negative integer to convert.

    Returns:
        str: A string representing the number in binary (base 2). 
             Returns an error string for invalid input.
    """
    # 1. Input Validation
    if not isinstance(decimal_num, int) or decimal_num < 0:
        return "Error: Input must be a non-negative integer."
    
    # 2. Base Case: Zero
    if decimal_num == 0:
        return "0"

    binary_string = ""
    current_num = decimal_num
    
    # 3. Conversion Loop (Repeated Division)
    while current_num > 0:
        # Get the remainder (this is the next binary digit: 0 or 1)
        remainder = current_num % 2
        
        # Prepend the remainder to the result string (since binary digits are read bottom-up)
        binary_string = str(remainder) + binary_string
        
        # Update the number by integer division (discarding the remainder)
        current_num //= 2
        
    return binary_string

# --- Example Usage ---

if __name__ == "__main__":
    
    # Test Cases
    num1 = 13  # Expected: 1101 (8 + 4 + 0 + 1)
    num2 = 0   # Expected: 0
    num3 = 255 # Expected: 11111111
    num_invalid = -5

    print(f"Decimal {num1} in Binary: {decimal_to_binary(num1)}")
    print(f"Decimal {num2} in Binary: {decimal_to_binary(num2)}")
    print(f"Decimal {num3} in Binary: {decimal_to_binary(num3)}")
    
    print("\n--- Invalid Input Test ---")
    print(decimal_to_binary(num_invalid))
    
    # Note: For real-world use, Python's built-in function `bin(13)` 
    # returns '0b1101' (0b prefix)
