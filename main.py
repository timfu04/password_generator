# Import modules
import string
import random



# Function to generate password or PIN
def password_generator(type : str, length : int, digits : bool = False, symbols : bool = False) -> str:
    
    """ Password generator (Password or PIN)

    Args:
        type (str): Password or PIN
        length (int): Length of password or PIN
        digits (bool): Whether to include digits in password
        symbols (bool): Whether to include symbols in password

    Returns:
        str: Password or PIN generated
    """
        
    temp_password = ""
    
    if type == "Password":
        temp_password += string.ascii_lowercase
        temp_password += string.ascii_uppercase
            
        if digits:
            temp_password += string.digits
        if symbols:
            temp_password += string.punctuation
            
    elif type == "PIN":
        temp_password += string.digits
        
    while len(temp_password) < length:
        temp_password += temp_password
    
    final_password = "".join(random.sample(temp_password, length))
    
    return final_password
    


if __name__ == "__main__":
    # Password
    # Alphabets only - False, False
    # Alphabets & digits - True, False
    # Alphabets & symbols - False, True
    # Alphabets & digits & symbols - True, True
    result = password_generator("Password", 100, True, True)
    print(result)
    
    print("\n")
    
    # PIN
    result2 = password_generator("PIN", 100)
    print(result2)
    
    
    