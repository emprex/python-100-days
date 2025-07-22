Cashier Billing System
This project implements a simple cashier billing system in Python. It guides users through entering products, selecting a membership type, applies the correct discount, and prints a final bill. The workflow mirrors a clear, professional flowchart, and is structured for easy understanding and extension.

Features
Multiple Products: Enter as many items as desired, each with a name, quantity, and price.

Membership Discounts: Supports four membership levels (Gold, Silver, Bronze, No Membership) with variable discount rates.

Robust Input Validation: Checks for valid numeric inputs.

Receipt Output: Displays a well-formatted bill showing all details and savings.

Clean, Modular Code: Each part (input, processing, output) is handled by dedicated Python functions with clear comments.

How It Works
Input Products:
The user is prompted to enter product details in a loop until choosing to stop.

Select Membership:
Enter the customer’s membership type. Discount rates:

Gold: 30%

Silver: 10%

Bronze: 5%

No membership: 0%

Calculate Bill:
The script sums totals, applies the correct discount, and prints a formatted receipt.

Example Usage
shell
$ python cashier.py
Enter product name: Coffee
Enter quantity: 2
Enter price per item: £3.5
Add another product? (yes/no): yes
Enter product name: Sandwich
Enter quantity: 1
Enter price per item: £4.0
Add another product? (yes/no): no
Membership type (NO, Gold, Silver, Bronze): Gold

--- Final Receipt ---
2 x Coffee @ £3.50 = £7.00
1 x Sandwich @ £4.00 = £4.00
Subtotal: £11.00
Discount: 30%
Discounted amount: -£3.30
Total to pay: £7.70
Diagram
The logic flow is documented in the project diagram (docs/cashier_flow.png):

Product entry loop

Membership selection branching

Discount application

Final output node

See images/cashier_diagram.png for the full decision flow.

How to Run
Clone the repository.

Ensure you have Python 3.8+ installed.

Execute the script:

bash
python cashier.py
Follow the on-screen prompts.

Project Structure
File/Folder	Purpose
cashier.py	Main Python script (billed logic)
images/cashier_diagram.png	Logic flowchart exported from draw.io
README.md	This documentation
Customization Ideas
Add product categories.

Allow for coupon codes or extra offers.

Save receipts to a text or CSV file.

Integrate with a simple GUI (Tkinter, PyQt).

Extend membership types or make discounts dynamic.

Professional Practices Demonstrated
Modular, readable Python code with docstrings

Clear input validation and error handling

Workflow documented by a logic diagram

Stepwise commit history and meaningful messages

README structured for learner and portfolio clarity

Further Reading
Python Crash Course, 2nd Edition: Chapter 5 (“If Statements”)—Conditional logic and control flow.

100-Day Python Professional Course: Day 7—Branching, memberships, and practical applications.

Fluent Python: Chapter 4—Best practices for Boolean logic and control flow.

Effective Python: Items on code clarity and professional idioms for branching.

License
MIT License—see LICENSE for details.

Built as part of the 100-Day Python Bootcamp to practice control flow, modular coding habits, and professional documentation.