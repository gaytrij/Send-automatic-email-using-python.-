# Send-automatic-email-using-python.-

Structure:
  -User Interface: Design a console-based user interface for input and output, allowing users to interact with the calculator using simple commands or GUI ).
  
Functionality: Implement features to perform basic arithmetic operations, error handling for invalid inputs, and support for decimal or integer inputs.

Reports: Generate reports or logs of performed operations (optional) and save them into a text file or a database.

Technologies: -Python: For developing the application’s core logic and features.
-Tkinter (Optional): For building a GUI-based calculator with buttons, input fields, and result displays.
-SQLite (Optional): For saving the history of operations performed by the user.

Email Sending Functionality:
The send_email() function sends an email with an attachment to the specified receiver. It uses the smtplib and email libraries to connect to the Gmail SMTP server and send the email.

Basic Arithmetic Operations:
The add(), subtract(), multiply(), and divide() functions perform the respective arithmetic operations. The division function checks for division by zero.

SQLite Database Integration:
 A SQLite database calculator_history.db is created to store the history of calculations. Each calculation (operation, operands, result) is saved in the history table.

 Console User Interface: The user interacts with the program via the console. They can perform arithmetic operations, view the history of previous calculations, or send emails with attachments.
the program supports error handling for invalid inputs (e.g., non-numeric values).
