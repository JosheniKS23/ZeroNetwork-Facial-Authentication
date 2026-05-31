Contributed AWS Sync architecture and offline queue design.
# ZeroNetwork-Facial-Authentication
Offline-first facial recognition and liveness detection system for secure authentication in zero-network environments with local verification, encrypted vaults, and audit logging.

# Datalake 3.0 – Offline Facial Recognition & Liveness Detection System

An offline-first facial recognition and liveness verification system designed for secure authentication in zero-network environments. The solution performs local face recognition, anti-spoofing checks, encrypted vault handling, and tamper-evident audit logging without requiring internet connectivity.

## 🚀 Features

### 🔐 Offline Face Recognition
- Multi-face enrollment (5-angle sampling)
- Local face matching using facial embeddings
- No cloud dependency
- Privacy-preserving local storage

### 🛡️ Liveness Detection
Prevents spoofing attacks using:
- 👁️ Blink Detection (Eye Aspect Ratio)
- 😄 Smile Detection (Mouth geometry)
- ↔️ Head Turn Detection (Facial landmark displacement)

### 📷 Camera-Based Verification
- Real-time webcam integration
- Offline inference using `face-api.js`
- Mid-range device compatibility

### 🔒 Secure Vault System
- AES-GCM encrypted local vault
- PBKDF2-SHA256 key derivation
- Local-only encrypted identity storage

### 📑 Audit Trail
Tamper-evident local logs for:
- Login attempts
- Face recognition
- Liveness verification
- Vault creation
- Network state changes

### 🌐 Offline-First Architecture
- Fully functional without internet
- Designed for remote/field deployments
- Supports zero-network operational zones

---

## 🧠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### AI / Computer Vision
- `face-api.js`
- Tiny Face Detector
- Face Landmark 68 Model
- Face Recognition Model

### Security
- WebCrypto API
- AES-GCM Encryption
- PBKDF2-SHA256

### Storage
- LocalStorage
- Encrypted vault records
- Offline audit logs

---

## 📂 Project Structure

```txt
project-folder/
│── highway.html
│── models/
│     ├── tiny_face_detector_model-shard1
│     ├── tiny_face_detector_model-weights_manifest.json
│     ├── face_landmark_68_model-shard1
│     ├── face_landmark_68_model-weights_manifest.json
│     ├── face_recognition_model-shard1
│     ├── face_recognition_model-shard2
│     └── face_recognition_model-weights_manifest.json

_______________________________________________________________________________________________________________________________________________________________________________________________________________
Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/datalake-offline-security.git
cd datalake-offline-security
2. Install face recognition models

Download model weights from:

https://github.com/justadudewhohacks/face-api.js/tree/master/weights

Place them inside:

/models
3. Run local server
python -m http.server 8000

Open:

http://localhost:8000/highway.html


🔄 Workflow
Enrollment
Start camera
Enter operator name
Click Enroll Face
Capture 5 face angles:
Front
Left
Right
Slight Up
Slight Down
Recognition
Start camera
Click Recognize Face
Face embedding comparison performed locally
Displays:
✅ Recognized
❌ Unknown Person
Liveness Verification

User performs:

Blink
Smile
Head Turn

System validates motion patterns locally to prevent spoofing.

🔍 Security Design

The system is designed with:

Privacy First
No biometric data sent to cloud
Fully local inference
Offline Reliability
Works in remote areas
No dependency on network connectivity
Tamper Awareness
Signed local audit chain
Secure vault encryption
🎯 Use Cases
Remote field authentication
Zero-network security zones
Attendance systems
Industrial workforce verification
Autonomous mobility centres
Military / critical infrastructure

📌 Future Improvements
Sequential randomized liveness challenges
React Native mobile deployment
TensorFlow Lite optimization
AWS sync after connectivity restoration
Confidence score visualization
Multi-user enterprise deployment

👥 Team Contribution
Frontend & Dashboard
Base UI/dashboard implementation
AI Integration
Face recognition pipeline
Multi-face enrollment
Liveness detection
Model integration
Threshold tuning
Backend / Integration
Audit logging
Offline sync architecture
Deployment support
📜 License

This project is developed for Hackathon 7.0 as an academic/innovation prototype.


### 1–2 line project description (for GitHub/About/Resume)

**Option 1 (best):**

> An offline-first facial recognition and liveness detection system for secure authentication in zero-network environments, featuring local face verification, anti-spoofing checks, encrypted vaults, and audit logging.

**Option 2 (shorter):**

> A secure offline facial authentication system with liveness detection and local audit logging designed for remote and zero-network environments.
