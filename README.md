🩺 YOLOv8-Based Kidney Disease Detection
📌 Project Overview

This project focuses on automated kidney disease detection and segmentation using YOLOv8.
The model is trained on medical imaging data (CT scans) to identify and segment diseased regions in the kidney.

Our goal is to build a fast, accurate, and lightweight solution for medical imaging that can assist radiologists and healthcare professionals in early diagnosis.

⚙️ Features

🔍 Object Detection & Segmentation of kidney abnormalities

⚡ Real-time inference using YOLOv8

📊 Evaluation metrics (mAP, Precision, Recall, IoU)

🌐 Future deployment as a Flask web application

📂 Organized pipeline (Training → Validation → Testing → Deployment)

📁 Project Structure
YOLOv8_CKD_Project/
│── data/               # Dataset (images + annotations)
│── runs/               # Training results and logs
│── models/             # YOLOv8 pretrained/custom weights
│── notebooks/          # Jupyter notebooks for experiments
│── app/                # Flask web app (for deployment)
│── results/            # Prediction outputs & visualizations
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

🚀 Installation & Setup

Clone the Repository

git clone https://github.com/your-username/YOLOv8_CKD_Project.git
cd YOLOv8_CKD_Project


Create Virtual Environment & Install Dependencies

pip install -r requirements.txt


Download YOLOv8

pip install ultralytics


Run Training

yolo task=segment mode=train model=yolov8s-seg.pt data=data.yaml epochs=100 imgsz=640


Run Inference

yolo task=segment mode=predict model=runs/segment/train/weights/best.pt source="test_images/"

📊 Results & Performance

Achieved high accuracy in detecting diseased regions.

Model performance evaluated using Precision, Recall, IoU, and mAP.

Visual results show accurate segmentation of abnormalities.

🌐 Future Scope

✅ Deploy real-time detection system using Flask / FastAPI

✅ Extend dataset for better generalization

✅ Optimize model for edge devices (mobile, Raspberry Pi, Jetson Nano)

🤝 Contributors

👨‍💻 Shailesh chowdary – Project Lead

📚 Mehar Meghana,k.Poojitha – Dataset preparation, training, and evaluation

📜 License

This project is licensed under the MIT License – feel free to use and modify.
