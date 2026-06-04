# ZeroNetwork-Facial-Authentication

Offline-first facial recognition and liveness detection system for secure authentication in zero-network environments with local verification, encrypted vaults, attendance tracking, offline synchronization, and tamper-evident audit logging.

**#NHAI Innovation Hackathon 7.0
#Develop a Mobile Based Secure Offline Facial Recognition and Liveness Detection System for Remote Locations**


An offline-first identity verification platform designed for secure authentication in zero-network environments. The system performs local face recognition, liveness verification, encrypted vault management, attendance tracking, audit logging, and offline-to-cloud synchronization without requiring continuous internet connectivity.

---

## 🚀 Key Features

### 🔐 Offline Face Recognition

* Multi-face enrollment using 5 facial samples
* Local face matching using facial embeddings
* Adjustable recognition threshold
* Confidence score visualization
* Multi-face detection and rejection
* No cloud dependency

### 🛡️ Liveness Detection

Prevents spoofing attacks through:

* 👁️ Blink Detection
* 😄 Smile Detection
* ↔️ Head Turn Detection

All checks run locally using facial landmarks.

### 📷 Multi-Sample Enrollment

Each user is enrolled using:

1. Front Face
2. Slight Left
3. Slight Right
4. Slight Up
5. Slight Down

This improves recognition robustness under varying head poses.

### 📋 Attendance Management

Upon successful recognition:

* Attendance is automatically recorded
* Duplicate attendance is prevented
* Verification status is stored
* Timestamp is generated locally

Example:

```json
{
  "name": "John",
  "time": "2026-06-04 09:01",
  "liveness": "passed",
  "verified": true
}
```

### 🔒 Secure Vault System

Encrypted local identity storage using:

* AES-GCM 256-bit encryption
* PBKDF2-SHA256 key derivation
* Local-only vault records

### 📑 Tamper-Evident Audit Trail

Tracks:

* Login events
* Face enrollment
* Recognition attempts
* Attendance marking
* Liveness verification
* AWS sync operations
* Network mode changes

Each event is chained using SHA-256 hashes.

### 🌐 Offline-First Architecture

* Works completely offline
* No internet required for authentication
* Suitable for remote deployments
* Supports disaster recovery environments

---

## ☁️ Offline-to-AWS Sync Architecture

To support future cloud deployment, the system implements an offline synchronization queue.

### Workflow

```text
Face Recognition
        ↓
Attendance Created
        ↓
Stored Locally
        ↓
Added To Sync Queue
        ↓
AWS Sync Trigger
        ↓
Marked As Synced
        ↓
Purge Local Cache
```

### Sync Queue Example

```json
{
  "type": "attendance",
  "name": "John",
  "timestamp": "2026-06-04T09:01:00",
  "status": "pending"
}
```

### AWS Sync Features

* Offline queue management
* Pending sync counter
* Sync simulation
* Purge synced records
* Future-ready for AWS integration

---

## 🧠 Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)

### AI / Computer Vision

* face-api.js
* Tiny Face Detector
* Face Landmark 68 Model
* Face Recognition Model

### Security

* WebCrypto API
* AES-GCM Encryption
* PBKDF2-SHA256
* SHA-256 Audit Hashing

### Storage

* LocalStorage
* Face Database
* Attendance Database
* Audit Database
* Sync Queue

### Backend (Development)

* Python
* Flask
* Local Logging Server

---

## 📂 Project Structure

```text
project-folder/
│
├── index.html
├── highway.html
├── server.py
│
├── models/
│   ├── tiny_face_detector_model-shard1
│   ├── tiny_face_detector_model-weights_manifest.json
│   ├── face_landmark_68_model-shard1
│   ├── face_landmark_68_model-weights_manifest.json
│   ├── face_recognition_model-shard1
│   ├── face_recognition_model-shard2
│   └── face_recognition_model-weights_manifest.json
│
├── localStorage
│   ├── face_db
│   ├── attendance
│   ├── dl3_audit
│   ├── dl3_vault
│   └── dl3_sync_queue
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ZeroNetwork-Facial-Authentication.git

cd ZeroNetwork-Facial-Authentication
```

### 2. Download Face Recognition Models

Download model weights:

https://github.com/justadudewhohacks/face-api.js/tree/master/weights

Place them inside:

```text
/models
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run Server

```bash
python server.py
```

Open:

```text
http://localhost:5000
```

---

## 🔄 System Workflow

### Enrollment Flow

```text
Start Camera
      ↓
Enter Name
      ↓
Enroll Face
      ↓
Capture 5 Face Angles
      ↓
Store Face Embeddings
```

### Authentication Flow

```text
Start Camera
      ↓
Run Liveness Challenge
      ↓
Blink
      ↓
Smile
      ↓
Head Turn
      ↓
Recognition
      ↓
Attendance Marked
```

### Sync Flow

```text
Attendance
      ↓
Sync Queue
      ↓
AWS Sync
      ↓
Purge Synced Records
```

---

## 🔍 Security Design

### Privacy First

* No cloud-based recognition
* No external biometric transmission
* Local-only face processing

### Offline Reliability

* Fully functional without internet
* Supports remote environments
* Zero-network deployment ready

### Anti-Spoofing

* Blink verification
* Smile verification
* Head movement verification

### Tamper Awareness

* Audit chain hashing
* Encrypted vault storage
* Sync tracking

---

## 🎯 Use Cases

* Remote workforce authentication
* Industrial attendance systems
* Secure access control
* Military installations
* Disaster recovery centers
* Zero-network operational zones
* Critical infrastructure security

---

## 📈 Future Enhancements

### AI Improvements

* Randomized liveness challenges
* Sequential challenge workflow
* TensorFlow Lite optimization
* Advanced anti-spoofing

### Cloud Integration

* AWS Lambda
* AWS API Gateway
* AWS DynamoDB
* AWS S3 Audit Backup

### Deployment

* React Native Mobile App
* Android Deployment
* Enterprise User Management

---

## 👥 Team Contributions

### Frontend & Dashboard

* Dashboard UI
* Offline Security Console
* Attendance Dashboard
* Sync Queue Interface

### AI & Computer Vision

* Face Recognition Pipeline
* Multi-Sample Enrollment
* Liveness Detection
* Threshold Tuning
* Confidence Scoring

### Security

* Encrypted Vault
* Audit Trail
* Hash Chaining
* Offline Authentication

### Integration & Backend

* Flask Logging Server
* AWS Sync Architecture
* Attendance Tracking
* Offline Queue Management

---

## 📜 License

Developed as a prototype solution for Hackathon 7.0.

This project is intended for academic, research, and innovation purposes.
