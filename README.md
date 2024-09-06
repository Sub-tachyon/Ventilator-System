# Ventilator⚕️Backend System

A Django-based application designed for managing and monitoring medical devices. This README provides instructions on how to set up and run the development server.

## System Requirements 📝

- **Python 3.8+**: Ensure you have Python 3.8 or higher installed.
- **Redis**: Required for Django Channels. Install and run Redis on your local machine or use a Docker container.

 
## How It Works 🛠️

### Overview

It is designed for managing ventilators and patient data in a medical setting. The system includes functionalities for device registration, patient management, and real-time updates using WebSockets. Here's a breakdown of its main components and their functionalities:

### Components 🧩

#### 1. Models ⛁

- **Ventilator**: Represents a medical ventilator device with attributes like serial number, model, and status.
- **Patient**: Represents a patient with details such as name, age, and medical information. Each patient is linked to a ventilator.
- **device_logs**: Logs actions related to ventilator usage, including allocation and deallocation.
- **mydevices**: Tracks devices associated with users based on email addresses.

#### 2. Views 👀

- **Device Registration (`device_reg2`)**: Handles POST requests to register new ventilators. It saves the device details to the database and sends a POST request to a remote URL for additional processing.
- **Patient Registration (`patient_data`)**: Handles POST requests for registering new patients. It links patients to ventilators, updates device status, and logs device allocation.
- **Remove Device (`remove_device`)**: Unallocates a ventilator and updates its status. It also logs the device return and updates patient status.
- **Patient List (`patient_list`)**: Retrieves and displays a list of all patients.
- **Device List (`device_list`)**: Retrieves and displays a list of all ventilators.
- **My Devices (`my_devices`)**: Displays the list of patients, though this seems to duplicate the patient list functionality.
- **Device Logs (`device_logs_view`)**: Retrieves and displays logs related to device usage.

#### 3. Serializers

- **devicedataSerializer**: Converts Ventilator model data to and from JSON format for API use.

#### 4. WebSockets 🔌 

- **DummyDataConsumer**: A WebSocket consumer that simulates sending dummy device data every 2 seconds. It uses Django Channels for real-time communication.

#### 5. URLs and Routing 🔗

- **WebSocket URL Configuration**: Maps WebSocket connections to the `DummyDataConsumer`.

#### 6. Email and Authentication ✉️ 

- **SMTP for Email**: The application uses SMTP for sending emails, including OTPs and password reset links. The configuration is set up in `settings.py` to use Gmail's SMTP server.
  - **Email Backend Configuration**:
    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = port number
    EMAIL_HOST_USER = host address
    EMAIL_HOST_PASSWORD = password
    ```

### Running the Application 👩🏻‍💻

1. **Start the Django Development Server**: Use the command `python manage.py runserver` to start the server.
2. **Access the Application**: Visit `http://127.0.0.1:8000/`in your browser to interact with the application.
3. **WebSocket Communication**: Ensure Redis is running for WebSocket support. The WebSocket endpoint `/ws/dummy_data/` will provide real-time updates.

### Example Use Case

1. **Registering a Device**: Use the device registration view to add new ventilators. The device will be saved in the database, and its status will be set to 'Not allocated.'
2. **Allocating a Device to a Patient**: After registering a patient, the view will allocate an available ventilator to the patient and log this action.
3. **Viewing Logs**: Access device logs to see the history of allocations and deallocations.

Thank You for visiting, Happy coding!...

