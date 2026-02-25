from pyscript import document

def check_login(event):
    # Grab inputs
    username = document.querySelector("#login_user").value
    password = document.querySelector("#login_pass").value
    
    # Error message element
    error_msg = document.querySelector("#login_error")
    
    # Logic: Check if username is 'admin' and password is the elevation '2699'
    if username == "admin" and password == "2699":
        # Hide the Modal
        document.querySelector("#loginModal").style.display = "none"
        # Show the Dashboard
        document.querySelector("#main_content").style.display = "block"
        print("Access Granted")
    else:
        # Show error message
        error_msg.style.display = "block"
        print("Access Denied")

def process_data(event):
    # Your existing doubling logic
    user_input = document.querySelector("#user_num").value
    if user_input:
        result = int(user_input) * 2
        document.querySelector("#display_area").innerText = f"Result: {result}"
