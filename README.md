# 💍 Pandora-Style E-Commerce Site Clone | Real-Time Filtering & Mobile Compatible

This project was developed from scratch, closely mimicking the shopping experience of the world-famous Pandora brand.
It includes all components of a modern e-commerce site with real-time filtering, product variations, and mobile-responsive design.

---

## 🌟 Key Features

### ⚡️ Real-Time Filtering (AJAX)
- Filter options: Metal, Color, Price Range, Collection, etc.
- Instant product filtering without page refresh
- Filter information automatically added to URL parameters → shareable link structure

### 💎 Product Family & Variation Switching
- View different color variations of the same model on product detail page
- Hover preview + redirect to relevant page on click
- Automatic image updates

### 📱 Mobile Responsive Design
- Filters displayed in special menu for mobile
- 2-column product list on mobile, 4-column on desktop
- Lazy-loading used for performance

### ❤️ Favorite System
- Add products to favorites (stored with localStorage)
- "Complementary Products" recommendation system
  
---

## 🔧 Technologies Used

| Katman       | Teknoloji         | Açıklama                                 |
|--------------|-------------------|------------------------------------------|
| **Backend**  | Django             | Product management, filtering endpoints |
| **Frontend** | Vanilla JavaScript | AJAX operations, filtering, interactions|
|              | Bootstrap 5        | Responsive design                       |
| **Tasarım**  | CSS3 + Flexbox     | Mobile-compatible custom styles         |
| **API**      | Axios              | AJAX requests                           |

---
## 🖥️ Desktop Views

|🏠 Home Page |
|-------------|
[![▶️ İzlemek için tıkla](screenshots/mainC.gif)](https://youtu.be/4rmXltN4lzM)

---

|🛍️ Product List |
|-------------|
[![▶️ İzlemek için tıkla](screenshots/menuC.gif)](https://youtu.be/CaPrFtV_Wsk)

---

|📄 Product Detail |
|-------------|
[![▶️ İzlemek için tıkla](screenshots/productC.gif)](https://youtu.be/DF_GKciMD50)

---

## 📱 Mobile Views

### 🏠 Home Page  
[![▶️ İzlemek için tıkla](screenshots/mainM.gif)](https://youtu.be/67BQphoCt7k)

---

### 🛍️ Product List  
[![▶️ İzlemek için tıkla](screenshots/menuM.gif)](https://youtu.be/jwreRi7uapE)

---

### 📄 Product Detail 
[![▶️ İzlemek için tıkla](screenshots/productM.gif)](https://youtu.be/5GOwtd5PvBY)

---

## 🖥️ Admin Panel Preview

![Screenshot](screenshots/admin-panel.png)

This admin panel enables fast and efficient management of e-commerce operations. The following operations can be performed through the panel:

🛒 Adding new products and updating existing product information

📁 Creating and editing product categories

👤 Viewing and managing user data

📦  Order tracking and updating order statuses

🗂️ Stock control and product inventory management

💬 Viewing and managing user reviews

This panel centralizes e-commerce processes, providing a user-friendly management experience.


## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/GoktugGok/jewelry-e-commerce.git
cd .\jewelryECommerce\

# 2. Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3. Install Required Packages
pip install -r requirements.txt

# 4. Database Migrations
python manage.py migrate

# 5. Create Admin User
python manage.py createsuperuser

# 6. Start the Project
python manage.py runserver

