# Inventory-management
Point of sale for retail store

**Inventory Management System** is a Django-based web application for managing your tile inventory. It allows you to add, update, and view the details of your tile products, dealers, and customers.

## Features

- **Tile Management**: Add new tile products with their name, quantity, and dealer information.
- **Customer Orders**: Create orders for customers by selecting tile products from your inventory.
- **Stock Updates**: Update the quantity of tile products based on sales.
- **List and Detail Views**: View the list of tile products and details of individual products.
- **User-Friendly Interface**: Easily manage your tile inventory with a clean and intuitive web interface.

## Getting Started

Follow these steps to set up and run the Inventory Management System on your local machine:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/inventory-management.git
    cd inventory-management
    ```

2. **Create a Virtual Environment:**

    It's recommended to use a virtual environment to manage dependencies.

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    Install the required Python packages using `pip`.

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    Apply the database migrations to set up the database schema.

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server:**

    Start the Django development server.

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**

    Open a web browser and go to `http://127.0.0.1:8000/` to access the Inventory Management System.

## Usage

1. **Adding Tile Products:**

    - Navigate to the admin panel (e.g., `http://127.0.0.1:8000/admin`) to add new tile products.

2. **Managing Customer Orders:**

    - Visit the Inventory Management System to create and update customer orders.

3. **Viewing Inventory:**

    - Use the web interface to see your current tile inventory and its details.

4. **Customization:**

    - Customize the application by modifying templates, styles, or extending functionality as needed.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## Acknowledgments

- [Django](https://www.djangoproject.com/): The web framework used to build this application.
- [Bootstrap](https://getbootstrap.com/): The CSS framework used for styling.

---

The project is in progress. Thanks for your time.:)
