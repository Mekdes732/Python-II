from pyscript import document

def process_data(event):
    # 1. Look for the input box in the HTML
    input_element = document.querySelector("#user_num")
    user_value = input_element.value
    
    # 2. Check if the user actually typed a number
    if user_value:
        # Convert text to a whole number (integer)
        number = int(user_value)
        
        # Perform your logic (let's double the number)
        result = number * 2
        
        # 3. Find the display area in HTML to show the answer
        output_element = document.querySelector("#display_area")
        output_element.innerText = f"Python calculated: {result}"
    else:
        # If the box is empty, show a warning
        document.querySelector("#display_area").innerText = "Please enter a number first!"


