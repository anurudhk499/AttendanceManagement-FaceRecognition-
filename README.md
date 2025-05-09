# Attendance Management (using face recognition)

### Project Description  
A real-time face recognition-based attendance management system that captures faces, stores face encodings, and marks attendance automatically when a known face is detected.  
This project is divided into three main parts:  

1. Face Capture - Captures multiple images of a person and stores them in a dataset.  
2. Face Encoding - Generates face encodings and saves them for recognition.  
3. Attendance Marking - Detects faces in real-time, matches them with stored encodings, and logs attendance into a CSV file.  

### Features  
* Real-time face detection and recognition.  
* Automatic attendance marking with a timestamp.  
* Easy dataset generation for new users.  
* Simple CSV-based attendance log.  

### Installation & Setup

1. Clone the repository:

   ```bash
   git clone <repository-link>
   cd Face-Recognition-Attendance-System
   ```

2. Install Dependencies:

   ```bash
   pip install opencv-python opencv-python-headless face_recognition numpy
   ```

3. Prepare Dataset:
   Run `capture_faces.py` to capture images for new users:

   ```bash
   python capture_faces.py
   ```

   Follow the instructions to enter User ID and Name.

4. Generate Encodings:
   After capturing images, run:

   ```bash
   python face_encoding.py
   ```

5. Run the Attendance System:
   Finally, launch the attendance marking application:

   ```bash
   python attendance.py
   ```

### File Descriptions  
* `capture_faces.py` - Script to capture face images and store them in the dataset.  
* `face_encoding.py` - Generates face encodings from the captured dataset.  
* `attendance.py` - Detects faces in real-time and logs attendance.  
* `face_encoding.pkl` - Serialized encodings of faces for recognition.  
* `attendance.csv` - Stores attendance records with names and timestamps.  

### Technologies Used    
* Python  
* OpenCV  
* Face Recognition  
* NumPy  
* CSV for data storage  

### Contributing  
Feel free to fork this repository and contribute by submitting a pull request. Any enhancements are welcome.  

### Acknowledgments  
Special thanks to the OpenCV and Face Recognition libraries for their robust tools in computer vision.  


### Future Enhancements  
* Add GUI for better user interaction.  
* Integrate with database instead of CSV.  
* Email notifications for attendance confirmation.  
* Real-time monitoring and analytics dashboard.
 

