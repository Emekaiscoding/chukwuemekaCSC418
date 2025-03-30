import cv2
import os

# User Data
users = {
    "emeka anyanwu": {"email": "chukwuemekaanyanwu322@gmail.com", "age": 18},
    "bona chukwu": {"email": "bonachukwu1@gmail.com", "age": 17},
    "tabitha udezi": {"email": "tabithaudezi23@gmail.com", "age": 23},
    "abdullah salami": {"email": "abdullahsalami343@gmail.com", "age": 26},
}

# Define folders for each art collection
art_collections = {
    "cont_art": "./images/cont_art/",
    "modern_art": "./images/modern_art/",
    "trad_art": "./images/trad_art/"
}

class Project:
    def __init__(self, username, email):
        self.username = username.lower()
        self.email = email

    def verify_user(self, users):
        """Check if user exists and verify age."""
        if self.username in users and users[self.username]["email"] == self.email:
            user_age = users[self.username]["age"]
            if user_age >= 18:
                print(f"Welcome, {self.username.capitalize()}! You have access.")
                return True
            else:
                print("Access restricted. You must be at least 18.")
                return False
        print("User not found or incorrect email.")
        return False

    def display_images_in_category(self, category, art_collections):
        """Display images from the selected category's folder."""
        category = category.lower()
        if category not in art_collections:
            print(f"Category '{category}' not found!")
            return

        folder_path = art_collections[category]

        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist!")
            return

        images = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

        if not images:
            print(f"No images found in '{category}'.")
            return

        for image_filename in images:
            image_path = os.path.join(folder_path, image_filename)
            image = cv2.imread(image_path)

            if image is None:
                print(f"Error: Image '{image_filename}' not found or cannot be opened!")
            else:
                print(f"Displaying: {image_filename}")
                cv2.imshow("Artwork", image)

                # Perform image transformation
                self.apply_transformations(image)

                cv2.waitKey(0)  # Wait for user input before showing the next image
                cv2.destroyAllWindows()

    def apply_transformations(self, image):
        """Apply transformations to the image."""
        print("\nChoose an image transformation:")
        print("1. Grayscale")
        print("2. Edge Detection (Canny)")
        print("3. Blurring")
        print("4. Rotate 90 degrees")
        print("5. Exit")

        while True:
            choice = input("Enter your choice (1-5): ").strip()
            if choice == "1":
                transformed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imshow("Grayscale Image", transformed_image)
            elif choice == "2":
                transformed_image = cv2.Canny(image, 100, 200)
                cv2.imshow("Edge Detection", transformed_image)
            elif choice == "3":
                transformed_image = cv2.GaussianBlur(image, (15, 15), 0)
                cv2.imshow("Blurred Image", transformed_image)
            elif choice == "4":
                transformed_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                cv2.imshow("Rotated Image", transformed_image)
            elif choice == "5":
                print("Exiting transformations...")
                break
            else:
                print("Invalid choice. Try again.")

            cv2.waitKey(0)
            cv2.destroyAllWindows()


# Get user input
username_input = input("Enter your username: ").strip().lower()
email_input = input("Enter your email: ").strip()

# Initialize Project
project = Project(username=username_input, email=email_input)

# Verify user
if project.verify_user(users):
    category_input = input("Enter an art category (cont_art, modern_art, trad_art): ").strip().lower()
    project.display_images_in_category(category_input, art_collections)
