"""
Simple Login Page (desktop GUI) using Tkinter + SQLite.
- Register (sign up) with username and password
- Passwords are stored as SHA-256 hashes, never in plain text
- Login validates credentials against the database

Run:  python login_page.py
"""

import hashlib
import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = "users.db"


# ---------------- Database helpers ----------------

def init_db():
    """Create the users table if it doesn't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password_hash TEXT NOT NULL
            )
            """
        )


def hash_password(password: str) -> str:
    """Hash a password with SHA-256 (for real apps use bcrypt instead)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def register_user(username: str, password: str) -> bool:
    """Insert a new user. Returns False if the username already exists."""
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, hash_password(password)),
            )
        return True
    except sqlite3.IntegrityError:
        return False


def validate_login(username: str, password: str) -> bool:
    """Check username + password against the database."""
    with sqlite3.connect(DB_NAME) as conn:
        row = conn.execute(
            "SELECT password_hash FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    return row is not None and row[0] == hash_password(password)


# ---------------- GUI ----------------

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("360x220")
        self.resizable(False, False)
        self.build_login_screen()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def build_login_screen(self):
        self.clear_window()

        tk.Label(self, text="Login", font=("Arial", 16, "bold")).pack(pady=(20, 10))

        frame = tk.Frame(self)
        frame.pack()

        tk.Label(frame, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        username_entry = tk.Entry(frame, width=25)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        password_entry = tk.Entry(frame, width=25, show="*")
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        def do_login():
            username = username_entry.get().strip()
            password = password_entry.get()
            if not username or not password:
                messagebox.showwarning("Missing info", "Please fill in both fields.")
                return
            if validate_login(username, password):
                messagebox.showinfo("Success", f"Welcome back, {username}!")
            else:
                messagebox.showerror("Failed", "Invalid username or password.")

        tk.Button(self, text="Login", width=20, command=do_login).pack(pady=10)
        tk.Button(
            self, text="Create an account", fg="blue", bd=0,
            command=self.build_register_screen,
        ).pack()

    def build_register_screen(self):
        self.clear_window()

        tk.Label(self, text="Sign Up", font=("Arial", 16, "bold")).pack(pady=(20, 10))

        frame = tk.Frame(self)
        frame.pack()

        tk.Label(frame, text="Username:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        username_entry = tk.Entry(frame, width=25)
        username_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        password_entry = tk.Entry(frame, width=25, show="*")
        password_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Confirm:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        confirm_entry = tk.Entry(frame, width=25, show="*")
        confirm_entry.grid(row=2, column=1, padx=5, pady=5)

        def do_register():
            username = username_entry.get().strip()
            password = password_entry.get()
            confirm = confirm_entry.get()

            if not username or not password:
                messagebox.showwarning("Missing info", "Please fill in both fields.")
                return
            if len(password) < 6:
                messagebox.showwarning("Weak password", "Password must be at least 6 characters.")
                return
            if password != confirm:
                messagebox.showerror("Mismatch", "Passwords do not match.")
                return
            if register_user(username, password):
                messagebox.showinfo("Success", "Account created! You can log in now.")
                self.build_login_screen()
            else:
                messagebox.showerror("Exists", "That username is already taken.")

        tk.Button(self, text="Register", width=20, command=do_register).pack(pady=10)
        tk.Button(
            self, text="Back to login", fg="blue", bd=0,
            command=self.build_login_screen,
        ).pack()


if __name__ == "__main__":
    init_db()
    app = LoginApp()
    app.mainloop()


    