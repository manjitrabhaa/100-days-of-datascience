# Pan Card Tampering Detection Flask App

## Overview

This project demonstrates how to detect tampering in PAN card images using image similarity techniques. While the example uses PAN cards, the same approach can be adapted for any organization to verify employee identity documents and authenticate users. By comparing an uploaded document with an original, organizations can automate the process of checking for alterations or forgeries.

## Features

- Upload a PAN card image and compare it with the original.
- Detect and highlight differences using structural similarity.
- Visualize tampered regions.
- Easily extendable for other types of identity documents (Aadhaar, employee ID, etc.).
- Can be integrated into user authentication workflows for organizations.

## Use Cases

- **Employee Authentication:** Organizations can use this system to verify the authenticity of employee ID cards during onboarding or periodic checks.
- **User Verification:** Any platform requiring document verification (banks, HR systems, etc.) can adapt this project to automate and secure their processes.

## Getting Started

### Prerequisites

- Python 3.7+
- Conda (recommended for environment management)

### Installation Steps

1. **Clone the Project**
   ```
   git clone <repository-url>
   ```

2. **Navigate to Project Directory**
   ```
   cd "Pan Card Tampering Flask App"
   ```

3. **Create a Conda Environment**
   ```
   conda create --name <environment_name> python=3.9
   ```

4. **Activate the Environment**
   ```
   conda activate <environment_name>
   ```

5. **Install Dependencies**
   ```
   python -m pip install -r requirements.txt
   ```

6. **Run the Application**
   ```
   python app.py
   ```

7. **Access the Web App**
   - Copy the URL shown in the terminal (usually `http://127.0.0.1:5000/`) and open it in your browser.

8. **Test the App**
   - Use sample images from the `sample_data` folder to test tampering detection.

## Folder Structure

- `app.py` - Main entry point for the Flask application.
- `app/` - Contains application modules.
  - `views.py` - Core logic for image processing and web routes.
  - `__init__.py` - Flask app initialization.
- `requirements.txt` - Python dependencies.
- `sample_data/` - Example images for testing.
- `app/static/` - Stores uploaded, original, and generated images.
- `readme.md` - Project documentation.

## How It Works

1. User uploads a PAN card image.
2. The app compares the uploaded image with the original using structural similarity.
3. Differences are highlighted and displayed.
4. The similarity score is shown to indicate authenticity.

## Extending the Project

- Replace PAN card images with any other document type.
- Integrate with employee onboarding systems.
- Add user management and authentication features.
- Connect to databases for storing verification results.

## License

This project is for educational and demonstration purposes. Adapt and extend as needed for your organization.

## Contact

For questions or contributions, please open an issue or submit a pull request.

Step to run application:
Step 1:	Create the copy of the project.
Step 2: Open command prompt and change your current path 
to folder where you can find 'app.py' file.
Step 3: Create environment by command given below-
conda create -name <environment name>
Step 4: Activate environment by command as follows-
conda activate <environment name>
Step 5: Use command below to install required dependencies-
python -m pip install -r requirements.txt
Step 6: Run application by command;
python app.py
You will get url copy it and paste in browser.
Step 7: You have sample_data folder where you can get images to test.
