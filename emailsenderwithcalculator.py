import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sqlite3

# --- Email Sending Functionality ---
def send_email(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, sender_password):
    try:
        # Create the message object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # Attach the body of the email
        msg.attach(MIMEText(body, 'plain'))
        
        # Open the attachment file in binary mode
        with open(attachment_path, "rb") as attachment:
            # Create an instance of MIMEBase and encode the attachment
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            
            # Add the attachment to the email
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path.split("/")[-1]}')
            msg.attach(part)
        
        # Set up the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Arithmetic Functions 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# --- SQLite Database Setup ---
conn = sqlite3.connect('calculator_history.db')
cursor = conn.cursor()

# Create table for storing calculation history
cursor.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        operation TEXT,
        num1 REAL,
        num2 REAL,
        result REAL
    )
''')
conn.commit()

def save_history(operation, num1, num2, result):
    cursor.execute('''
        INSERT INTO history (operation, num1, num2, result)
        VALUES (?, ?, ?, ?)
    ''', (operation, num1, num2, result))
    conn.commit()

# --- Function to get user input ---
def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# --- Main Console UI ---
def calculator():
    print("Welcome to the Python Calculator!")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View Calculation History")
        print("6. Send Email with Attachment")
        print("7. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7): ")
        
        if choice == '7':
            print("Exiting Calculator. Goodbye!")
            break
        
        if choice == '5':
            cursor.execute("SELECT * FROM history")
            rows = cursor.fetchall()
            if not rows:
                print("No history found.")
            else:
                print("\nCalculation History:")
                for row in rows:
                    print(f"ID: {row[0]}, Operation: {row[1]}, Num1: {row[2]}, Num2: {row[3]}, Result: {row[4]}")
            continue
        
        if choice == '6':
            sender_email = input("Enter your email: ")
            receiver_email = input("Enter receiver's email: ")
            subject = input("Enter subject: ")
            body = input("Enter body of the email: ")
            attachment_path = input("Enter the path of the attachment: ")
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            sender_password = input("Enter your email password: ")
            send_email(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, sender_password)
            continue
        
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")
        
        if choice == '1':
            result = add(num1, num2)
            operation = "Addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "Subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "Multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "Division"
        else:
            print("Invalid choice. Please try again.")
            continue
        
        print(f"Result: {result}")
        
        # Save the operation to the history
        save_history(operation, num1, num2, result)

# --- Run the Calculator ---
if __name__ == "__main__":
    calculator()

# Close the SQLite connection when the program ends
conn.close()
