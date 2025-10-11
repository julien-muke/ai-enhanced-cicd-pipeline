# app.py

def add_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    It's a simple, well-defined function.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers (integer or float).")
    return a + b

def get_user_greeting(user_data):
    """
    Generates a greeting for a user.
    This function works, but an AI might suggest improvements for handling
    missing keys or different data structures.
    """
    # A potential issue: This will fail if 'name' or 'city' is not in the dictionary.
    # An AI should be able to point this out.
    try:
        name = user_data["name"]
        city = user_data["city"]
        return f"Hello, {name} from {city}!"
    except KeyError:
        return "Hello, Guest! User data is incomplete."
    except TypeError:
        return "Hello, Guest! Invalid user data provided."

# --- FOR TESTING THE PIPELINE FAILURE ----
# Uncomment the function below to introduce a "CRITICAL" issue
# that the AI reviewer should flag, causing the pipeline to fail.

# def insecure_add(a, b):
#     """

#     This is a terribly insecure function that uses eval().
#     An AI reviewer should immediately flag this as a critical security risk.
#     """
#     # Using eval() on unvalidated input is a major security vulnerability.
#     result = eval(f"{a} + {b}") 
#     return result
