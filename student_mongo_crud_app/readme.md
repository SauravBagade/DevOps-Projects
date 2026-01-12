# 🧩 Flask + MongoDB CRUD Web Application

A simple full-stack **Flask** web app connected to **MongoDB** for performing complete **CRUD (Create, Read, Update, Delete)** operations on student data.

This project demonstrates how to build a clean and functional Flask application with Bootstrap styling and MongoDB integration using **PyMongo**.

---

## 📋 Project Features

✅ Add new students  
✅ View all student records in a table  
✅ Edit and update student details  
✅ Delete existing records  
✅ MongoDB as backend database  
✅ Bootstrap 5 UI (Responsive and clean)

---

## 🛠️ Tech Stack

| Layer | Technology Used |
|--------|----------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, Jinja2 |
| **Backend** | Python (Flask Framework) |
| **Database** | MongoDB (Local or Cloud via MongoDB Atlas) |
| **Driver** | PyMongo |
| **Environment** | Flask Development Server |

---

## ⚙️ Requirements

### **System Requirements**
| Requirement | Details |
|--------------|----------|
| Python | 3.8+ (tested on Python 3.13) |
| MongoDB | Local Community Server or MongoDB Atlas (Cloud) |
| Browser | Chrome / Edge / Firefox |

---

### **Python Dependencies**

Create a `requirements.txt` file with the following:

```

Flask==3.0.3
pymongo==4.9.1
dnspython==2.6.1

````

Install all dependencies with:
```bash
pip install -r requirements.txt
````

Or individually:

```bash
pip install flask pymongo dnspython
```

---

## 💾 MongoDB Setup

### Option 1 — Local MongoDB

1. Install MongoDB Community Edition:
   [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
2. Start the MongoDB service (default port 27017).
3. The app will automatically connect to:

   ```
   mongodb://localhost:27017/
   ```

### Option 2 — MongoDB Atlas (Cloud)

1. Go to [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster and get your connection string:

   ```
   mongodb+srv://<username>:<password>@cluster0.mongodb.net/
   ```
3. Set it as an environment variable:

   ```bash
   set MONGO_URI="your_connection_string_here"
   ```

   *(Use `export` on macOS/Linux.)*

---

## 📂 Project Structure

```
flask_mongo_crud_app/
│
├── app.py                     # Main Flask application
│
├── templates/                 # HTML templates
│   ├── base.html              # Layout template (Bootstrap)
│   ├── index.html             # List of students (Read)
│   └── form.html              # Add/Edit student (Create/Update)
│
├── static/                    # Static files
│   └── style.css              # Custom styles
│
├── requirements.txt           # Project dependencies
│
└── README.md                  # Project documentation
```

---

## 🚀 Running the Application

1. **Start MongoDB** (if local)
2. **Run the Flask app**:

   ```bash
   python app.py
   ```
3. **Open in your browser**:

   ```
   http://127.0.0.1:5000
   ```

---

## 🧠 CRUD Operations

| Function          | Description                       | Route          |
| ----------------- | --------------------------------- | -------------- |
| View All Students | List all records                  | `/`            |
| Add Student       | Display form to create new record | `/create`      |
| Edit Student      | Update existing record            | `/edit/<id>`   |
| Delete Student    | Delete record                     | `/delete/<id>` |

---

## 🎨 UI Preview

| Page              | Description                             |
| ----------------- | --------------------------------------- |
| **Home Page**     | Displays all student records in a table |
| **Add/Edit Form** | Bootstrap-styled input form             |
| **Delete Action** | Removes record after confirmation       |

---

## 🧩 Future Improvements

* Add user authentication (login/logout)
* Add search and pagination
* Add form validation
* Add REST API endpoints (JSON-based)
* Dockerize the app for deployment

---

## 👨‍💻 Author

**Saurav Bagade**
📧 [saurav.bagade@example.com](mailto:saurav.bagade@example.com)
💻 Flask + MongoDB Developer Project

---

## 📜 License

This project is open-source and free to use for educational or personal purposes.

```

---

Would you like me to **add this README.md directly into your project (canvas)** so it’s saved with your other files?
```
