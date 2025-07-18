# 🔐 NeuroCrypt - AI Powered Encryption App

**NeuroCrypt** is a secure, user-friendly web application that allows users to encrypt and decrypt messages and files using AES encryption. Built with Streamlit, it features a simple UI, optional AI-based key generation, and secure file management.

---

## 🚀 Features

- ✅ AES-128 encryption using EAX mode
- 🔐 Message encryption and decryption
- 📁 File upload, preview, and instant decryption
- 🔑 Key export and reuse
- 👤 Basic user authentication
- 🧠 Optional AI-based key generation

---

## 🛠️ Tech Stack

- Python 3.x
- Streamlit (for frontend)
- PyCryptodome (for AES encryption)
- Neural Networks (for optional keygen)
- Amazon EC2 (optional deployment)

---

## 💻 How to Run Locally

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the app
streamlit run app.py
```

---

## 📦 File Structure

```
.
├── app.py                  # Main Streamlit app
├── auth_utils.py           # Handles login/authentication
├── crypto_utils.py         # AES encryption/decryption logic
├── log_utils.py            # Activity logging
├── neural_keygen.py        # (Optional) Neural key generation
├── user_db.json            # User data (optional)
├── uploads/                # Folder for encrypted file storage
├── activity_log.txt        # Stores logs of user actions
└── requirements.txt
```

---

## 📚 Use Cases

- Secure messaging for individuals and teams
- Teaching encryption and cryptography concepts
- Private file encryption with local key control
- Lightweight data protection for developers

---

## 🌐 Deployment

To deploy on Amazon EC2:
- Launch a Linux VM
- Install Python and pip
- Upload app files using SCP or Git
- Run: `streamlit run app.py --server.port 8501 --server.enableCORS false`
- Access via: `http://<your-ec2-ip>:8501`

---

## 🔒 License

This project is licensed under the MIT License.

