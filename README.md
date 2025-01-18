# Mutual Fund Broker Web Application
A web application that allows users to register, log in, and manage a portfolio of mutual funds. The application supports features such as displaying a portfolio, simulating the purchase and sale of mutual funds, and tracking the current portfolio value. It integrates with RapidAPI to fetch mutual fund data and is built using Python with FastAPI and Jinja2 for templating.

### Features:
- User Registration and Login: Users can create an account and log in securely.
- Portfolio Management: Users can view their current portfolio, including profit or loss.
- Simulated Buy and Sell: Users can simulate the purchase and sale of mutual funds based on the current NAV (Net Asset Value).
- RapidAPI Integration: Fetches real-time mutual fund data through RapidAPI.
- Database Support: The application supports SQL-based databases (e.g., PostgreSQL, MySQL, SQLite) for data persistence.
- Extensibility: Designed to be easily extensible with the addition of new features and services.


### Tech Stack
- Backend: Python (FastAPI)
- Database: SQLite
- API Integration: RapidAPI for fetching mutual fund data

### Installation

1. Clone the repository
```bash
git clone https://github.com/Amitava123/Mutual-Fund-Broker-API.git
cd Mutual-Fund-Broker-API
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up the database
Update the DATABASE_URL in the .env file to your SQL database connection string.

Run the database migration scripts:

```python
import sqlite3

def create_schema():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create portfolios table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS portfolios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            total_investment REAL DEFAULT 0,
            total_value REAL DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    # Create mutual funds table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mutual_funds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            nav REAL NOT NULL,
            fund_type TEXT NOT NULL
        )
    ''')

    # Create transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            fund_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            transaction_type TEXT CHECK(transaction_type IN ('buy', 'sell')),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (fund_id) REFERENCES mutual_funds(id)
        )
    ''')

    # Create fund holdings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fund_holdings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            fund_id INTEGER NOT NULL,
            quantity INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (fund_id) REFERENCES mutual_funds(id)
        )
    ''')

    conn.commit()
    conn.close()

# Run the schema creation
create_schema()

```

5. Start the application
```bash
uvicorn app.main:app --reload
The application will be running on http://localhost:8000.
```

### Endpoints

- User Authentication

POST /register - Registers a new user
Request body:
```json
{
  "username": "user1",
  "password": "password123"
}
```
POST /login - Logs in an existing user
Request body:
```json
{
  "username": "user1",
  "password": "password123"
}
```
Portfolio Management
GET /dashboard - Displays the current portfolio of the user

Response:
```json
{
  "portfolio_value": 50000,
  "profit_or_loss": 5000,
  "funds": [
    {
      "name": "Fund A",
      "quantity": 10,
      "current_value": 5000
    },
    {
      "name": "Fund B",
      "quantity": 20,
      "current_value": 10000
    }
  ]
}
```

POST /buy - Simulates buying a mutual fund

Request body:
```json
{
  "fund_id": 1,
  "quantity": 10
}
```

POST /sell - Simulates selling a mutual fund

Request body:
```json
{
  "fund_id": 1,
  "quantity": 5
}
```

Other
GET /funds - Fetches a list of available mutual funds (from RapidAPI)

Response:
```json
[
  {
    "id": 1,
    "name": "Fund A",
    "category": "Equity"
  },
  {
    "id": 2,
    "name": "Fund B",
    "category": "Debt"
  }
]
```

Database Models
User
```
id: Integer (Primary Key)
username: String
password: String (hashed)
```

Portfolio
```
id: Integer (Primary Key)
user_id: Integer (Foreign Key to User)
fund_id: Integer (Foreign Key to Fund)
quantity: Integer
```

Fund
```
id: Integer (Primary Key)
name: String
category: String
current_nav: Decimal
```

License
This project is licensed under the MIT License - see the LICENSE file for details.
