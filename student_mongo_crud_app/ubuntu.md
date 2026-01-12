# 🧩 Flask + MongoDB CRUD Web Application – AWS Ubuntu (EC2) Setup

This guide explains how to **deploy and run** the Flask + MongoDB Student CRUD application on an **AWS EC2 Ubuntu server**.

---

## ✅ 1. Launch AWS EC2 Ubuntu Instance

1. Go to **AWS Console → EC2 → Launch Instance**
2. Choose:
   - **AMI**: Ubuntu Server 24.04 LTS (noble)  
   - **Instance type**: t2.micro (Free Tier)
   - **Key Pair**: Create new or use existing (`.pem` file)
3. Configure **Security Group**:
   - Allow **SSH**:  
     - Type: SSH, Port: 22, Source: My IP
   - Allow **Flask (dev port)**:  
     - Type: Custom TCP, Port: 5000, Source: `0.0.0.0/0` (for testing)
   - (Optional) Allow **HTTP (port 80)** if you will run app on port 80:
     - Type: HTTP, Port: 80, Source: `0.0.0.0/0`
4. Launch the instance.

---

## ✅ 2. Connect to EC2 via SSH

From your local machine (where `.pem` file is):

```bash
chmod 400 your-key.pem

ssh -i your-key.pem ubuntu@<PUBLIC_IP>
````

Example:

```bash
ssh -i my-key.pem ubuntu@50.17.85.192
```

---

## ✅ 3. Install System Packages (Python, Git, etc.)

On EC2:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
```

---

## ✅ 4. Clone Project Repository

```bash
cd /home/ubuntu

git clone <YOUR_GIT_REPO_URL> student_mongo_crud_app
cd student_mongo_crud_app
```

> Example:
> `git clone https://github.com/yourname/student_mongo_crud_app.git`

---

## ✅ 5. Create Virtual Environment & Install Python Dependencies

```bash
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

> `requirements.txt` should include:
>
> ```txt
> Flask==3.0.3
> pymongo==4.9.1
> dnspython==2.6.1
> ```

---

## ✅ 6. Install MongoDB Community Server (Ubuntu 24.04 – noble)

Add MongoDB GPG key:

```bash
curl -fsSL https://pgp.mongodb.com/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor
```

Add MongoDB repository:

```bash
echo "deb [arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | \
  sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
```

Update & install MongoDB:

```bash
sudo apt update
sudo apt install -y mongodb-org
```

Enable and start MongoDB service:

```bash
sudo systemctl enable mongod
sudo systemctl start mongod
sudo systemctl status mongod
```

Status should show: `active (running)`.

---

## ✅ 7. Flask App MongoDB Config (`app.py`)

`app.py` already uses:

```python
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['myapp_db']
collection = db['students']
```

Since MongoDB is running locally on EC2, default URI is fine:

```text
mongodb://localhost:27017/
```

---

## ✅ 8. Run Flask App on EC2

Make sure you’re in the project folder:

```bash
cd /home/ubuntu/student_mongo_crud_app
source venv/bin/activate
```

Update the `app.py` run section to bind to all addresses (so it’s reachable from outside):

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Then run:

```bash
python app.py
```

You should see:

```text
* Serving Flask app 'app'
* Debug mode: on
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://172.x.x.x:5000
```

---

## ✅ 9. Access Application in Browser

On your local machine, open:

```text
http://<PUBLIC_IP>:5000
```

Example:

```text
http://50.17.85.192:5000
```

You should see the **Student CRUD Web App**:

* List all students
* Add new student
* Edit student
* Delete student

---

## 🔁 10. Restarting the App & Freeing Port 5000

If you see:

```text
Address already in use
Port 5000 is in use by another program
```

It means another Python/Flask instance is already running on port 5000.

### 10.1. Find the process using port 5000

```bash
sudo lsof -i :5000
```

Example output:

```text
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python   5772 root    7u  IPv4  27802      0t0  TCP *:5000 (LISTEN)
python   5778 root    7u  IPv4  27802      0t0  TCP *:5000 (LISTEN)
```

### 10.2. Kill the processes

```bash
sudo kill -9 5772 5778
```

(Replace with actual PIDs from your output.)

Check again:

```bash
sudo lsof -i :5000
```

No output → port is free.

### 10.3. Start the app again

```bash
cd /home/ubuntu/student_mongo_crud_app
source venv/bin/activate
python app.py
```

---

## 🌐 (Optional) Run on Port 80 Without `:5000`

If you want to open the app as:

```text
http://50.17.85.192
```

Update `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
```

Run as root (port 80 is privileged):

```bash
sudo su
cd /home/ubuntu/student_mongo_crud_app
source venv/bin/activate
python app.py
```

Make sure **Security Group** allows HTTP (port 80).

---

## 🧩 Project Features Recap

* ✅ Add new students
* ✅ View all student records in a table
* ✅ Edit and update student details
* ✅ Delete existing records
* ✅ MongoDB as backend database
* ✅ Bootstrap 5 UI (Responsive and clean)

---

## 🆘 Troubleshooting

* **`Address already in use` on port 5000**
  → Use `sudo lsof -i :5000` and `sudo kill -9 <PID>` then restart app.

* **Page not opening from browser**

  * Check Flask is running in EC2
  * Check EC2 Security Group (port 5000 or 80 open)
  * Check `sudo ufw status` (if `active`, allow port):

    ```bash
    sudo ufw allow 5000/tcp
    sudo ufw allow 80/tcp
    ```

* **MongoDB connection error**

  * Check MongoDB service:

    ```bash
    sudo systemctl status mongod
    ```

---

