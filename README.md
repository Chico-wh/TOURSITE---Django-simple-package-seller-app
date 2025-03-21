# TourSITE

**TourSITE is a webapp for selling travel packages from agencies, with features such as voucher generation, email notifications, and Stripe integration for payments.**

---

## 🌟 Features

- **Sell Travel Packages**: 
  Create, edit, and display travel packages offered by various agencies.
  
- **Voucher Generation**: 
  Automatically generate digital vouchers for customers after purchase.

- **Email Notifications**: 
  Send purchase confirmations, vouchers, and updates directly to the customer's email.

- **Stripe Integration**: 
  Secure and reliable payments via credit/debit cards with Stripe.

- **Admin Dashboard**: 
  Exclusive area for agencies to manage packages, sales, and reports.

---

## 🛠️ Installation Instructions

### 1. Clone This Repository:
```bash
git clone https://github.com/youruser/toursite.git
cd toursite
````
2. Set Up the Virtual Environment:
```bash
pip install virtualenv
python -m venv venv
.\venv\Scripts\activate # Windows
# or
source venv/bin/activate # macOS/Linux
````
3. Install Dependencies:
````bash
pip install -r requirements.txt
````
4. Apply Database Migrations:
```bash
python manage.py migrate
````
5. Start the Server:
````bash
python manage.py runserver
````
Access the webapp at: http://localhost:8000

🌐 Additional Features
Filter Packages by Category, Location, or Price

Secure Checkout with Stripe

Responsive Design for mobile and desktop devices

Review and Rating System

📦 How to Add New Packages?
Access the admin panel at http://localhost:8000/admin.

Register new travel packages with detailed information.

Manage prices, images, and descriptions.

🚀 Planned Features
Recommendation system for packages based on customer preferences.

Additional payment methods, such as PayPal and Pix.

Detailed performance reports for agencies.

Support for multiple languages and currencies for international reach.

Agency rating system from customer feedback.

Integration with social media platforms for package promotion.

Contribute to TourSITE!
Found an issue or want to add new features? Feel free to open a pull request or submit an issue.

Enjoy and happy selling!
