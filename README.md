# Car Rental System

A comprehensive Car Rental System built with Python and MySQL that allows users to rent cars, manage bookings, and track rental history. The project covers various aspects of Python programming and database management using MySQL, and is suitable for learning and exploring concepts such as OOP, database interactions, CRUD operations, and user authentication.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Modules](#modules)
4. [Database Design](#database-design)
5. [Technologies Used](#technologies-used)
6. [Installation](#installation)
7. [Usage](#usage)
8. [HTML Code for Web Interface (Optional)](#html-code-for-web-interface-optional)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

The Car Rental System enables customers to rent cars, manage their bookings, and view rental history. Admins can manage the car inventory, view reports, and track the overall system status. This project covers essential features such as user authentication, booking management, and car maintenance tracking.

## Features

- **User Management**
  - User registration and login with role-based access (Customer, Admin).
  - Password management and profile updates.
- **Car Inventory Management**
  - Admins can add, update, view, and delete car details.
  - Tracks car maintenance history and service status.
- **Booking and Rental Management**
  - Search for available cars, book, extend rentals, and return cars.
  - Calculates total rental cost based on duration and car rate.
- **Payment and Billing**
  - Generate invoices for rentals and track payments.
  - Admins can view payment records and generate financial reports.
- **Admin Panel**
  - Admin dashboard for viewing system metrics and managing the inventory.
  - Manage users and view rental history.
- **Reports**
  - Generate rental, financial, and maintenance reports.

## Modules

1. **Authentication Module**
   - Handles user registration, login, and password management.
2. **Car Management Module**
   - Manages the car inventory, including adding, updating, and deleting cars.
3. **Booking Module**
   - Handles rental booking, extension, and cancellation.
4. **Payment and Billing Module**
   - Generates invoices and manages payment tracking.
5. **Admin Panel Module**
   - Admin functionalities for viewing system metrics, reports, and user management.
6. **Reports Module**
   - Generates various reports for rentals, finances, and car popularity.

## Database Design

The project uses a MySQL database with the following tables:

- **Users Table**: Stores user information and roles.
- **Cars Table**: Manages car details, availability, and maintenance.
- **Bookings Table**: Tracks rental bookings and status.
- **Payments Table**: Records payment transactions.
- **Maintenance Table**: Logs car maintenance activities.

## Technologies Used

- **Backend**: Python (Flask or Django for web interface)
- **Database**: MySQL
- **Libraries**:
  - `Flask` or `Django` for web-based implementation
  - `MySQL-Connector` for database connectivity
  - `bcrypt` for password hashing
  - `SQLAlchemy` for ORM (if using Flask)
