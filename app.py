from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ----------------------------
# Database Initialization
# ----------------------------
def init_db():
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            type TEXT,
            amount REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

# ----------------------------
# Helper Functions
# ----------------------------
def get_connection():
    return sqlite3.connect("bank.db")

def get_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = ?", (account_id,))
    account = cursor.fetchone()
    conn.close()
    return account

# ----------------------------
# Routes
# ----------------------------

@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    conn.close()
    return render_template("home.html", accounts=accounts)

@app.route("/create", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        name = request.form["name"]
        initial_balance = float(request.form["balance"])

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO accounts (name, balance) VALUES (?, ?)",
            (name, initial_balance)
        )
        account_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO transactions (account_id, type, amount, timestamp) VALUES (?, ?, ?, ?)",
            (
                account_id,
                "Deposit",
                initial_balance,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )

        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    return render_template("create_account.html")

@app.route("/deposit/<int:account_id>", methods=["GET", "POST"])
def deposit(account_id):
    if request.method == "POST":
        amount = float(request.form["amount"])

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, account_id)
        )

        cursor.execute(
            "INSERT INTO transactions (account_id, type, amount, timestamp) VALUES (?, ?, ?, ?)",
            (
                account_id,
                "Deposit",
                amount,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )

        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    account = get_account(account_id)
    return render_template("deposit.html", account=account)

@app.route("/withdraw/<int:account_id>", methods=["GET", "POST"])
def withdraw(account_id):
    account = get_account(account_id)

    if request.method == "POST":
        amount = float(request.form["amount"])

        if amount <= account[2]:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE accounts SET balance = balance - ? WHERE id = ?",
                (amount, account_id)
            )

            cursor.execute(
                "INSERT INTO transactions (account_id, type, amount, timestamp) VALUES (?, ?, ?, ?)",
                (
                    account_id,
                    "Withdraw",
                    amount,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )

            conn.commit()
            conn.close()

        return redirect(url_for("home"))

    return render_template("withdraw.html", account=account)

@app.route("/transactions/<int:account_id>")
def transactions(account_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT type, amount, timestamp
        FROM transactions
        WHERE account_id = ?
        ORDER BY id DESC
    """, (account_id,))

    records = cursor.fetchall()
    conn.close()

    return render_template(
        "transactions.html",
        transactions=records,
        account_id=account_id
    )

# ----------------------------
# Main
# ----------------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
