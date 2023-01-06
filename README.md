# SnapShots - Capturing life's moments, one picture at a time
This repository contains an image sharing app built with Django. The app allows users to upload and share images with others, as well as view and like images posted by other users.
# Prerequisites
Before you begin, make sure you have the following prerequisites installed on your system:

1. Python 3.6 or higher
2. Django 3.0 or higher
3. Pillow 7.0 or higher

# Installation
To install and run the image sharing app, follow these steps:

1. Clone the repository: git clone https://github.com/Codewithshagbaor/SnapShots.git
2. Navigate to the project directory: SnapShots
3. Install the required packages: pip install -r requirements.txt
4. Run the migration scripts: python manage.py makemigrations and python manage.py migrate
5. Create a superuser: python manage.py createsuperuser
6. Run the development server: python manage.py runserver
7. Open the app in your web browser at http://127.0.0.1:8000/

# Usage
To use the image sharing app, follow these steps:

1. Sign up for an account or log in if you already have an account.
2. Click on the "Upload" button to upload an image.
3. Enter a caption for your image and click "Post".
4. Your image will be displayed on the homepage along with the caption and your username.
5. You can view other users' images by clicking on their username or the image itself. This will take you to a page with a full view of the image and its caption.
6. You can like an image by clicking on the "Like" button.
7. You can view your own images and the images you have liked by clicking on the "My Images" or "Liked Images" buttons in the menu bar.

# Contributions
We welcome contributions to the image sharing app. If you would like to report a bug or submit a feature request, please open an issue on the repository. If you would like to contribute code, please fork the repository, make your changes, and submit a pull request.
