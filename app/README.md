# 📝 My Awesome To-Do List ✔️

Welcome to my Awesome To-Do List! A simple yet powerful Django application to help you keep track of your daily tasks and stay organized. Never forget a task again! ✨

This project is built to be clean, efficient, and easy to understand.

## 🚀 Features

*   **Create Tasks:** Easily add new tasks to your list. ✍️
*   **Edit Tasks:** Made a typo? Need to add more details? No problem! ✏️
*   **Delete Tasks:** Finished a task for good? Remove it from your list. 🗑️
*   **Set Due Dates:** Assign due dates to keep your priorities straight. 🗓️
*   **Track Status:** Mark tasks as 'Pending', 'Done', or 'Cancelled' to see your progress. ✅

## 💻 Technologies Used

This project is built with a classic and robust web stack:

*   **Backend:** Python 🐍 & Django 🎶
*   **Database:** SQLite3 💾 (the default Django database)
*   **Frontend:** Simple HTML & CSS 🎨

## 🛠️ Getting Started

Follow these instructions to get your own copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python 3 and `pip` installed on your system.

### Installation

1.  **Navigate to the project directory:**
    ```bash
    cd /path/to/your/app/
    ```

2.  **Create and activate a virtual environment:**

    *On macOS/Linux:*
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    *On Windows:*
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    *(Note: It's a good practice to create a `requirements.txt` file by running `pip freeze > requirements.txt` so others can install dependencies with `pip install -r requirements.txt`)*

    ```bash
    pip install Django
    ```

4.  **Apply database migrations:**
    This will set up the database schema for our `Task` model.
    ```bash
    python manage.py migrate
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    Now, open your favorite web browser and navigate to `http://127.0.0.1:8000/tasks/` to see the app in action! 🥳

## 🧪 Running Tests

We have a suite of tests to ensure the core functionality (Create, Read, Update, Delete) works correctly. To run the tests, execute the following command:

```bash
python manage.py test todo.tasks
```

---

Happy tasking! 😊