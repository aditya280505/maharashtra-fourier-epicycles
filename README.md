# 🌀 Maharashtra Fourier Epicycles

### Bringing Maharashtra's Map to Life with Fourier Mathematics

A Python visualization project that reconstructs the geographical outline of Maharashtra, India, using Fourier transforms and rotating circles called **epicycles**.

<p align="center">
  <a href="https://maharashtra-fourier-epicycles.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_LAUNCH_LIVE_DEMO-Visit_App-FF4B4B?style=for-the-badge" alt="Launch Live Demo">
  </a>
  &nbsp;
  <a href="https://github.com/aditya280505/maharashtra-fourier-epicycles">
    <img src="https://img.shields.io/badge/GitHub-View_Source_Code-181717?style=for-the-badge&logo=github" alt="View Source Code">
  </a>
</p>

---

## 🌐 Try It Yourself

### [🚀 Open the Live Application](https://maharashtra-fourier-epicycles.streamlit.app/)

Experience how rotating circles combine to trace the outline of Maharashtra.

**How to explore:**

1. Open the live application using the button above.
2. Press play on the animation.
3. Watch the epicycles trace the geographical boundary.
4. Explore the source code to understand how the visualization works.

> **Note:** The live application displays a pre-generated MP4 animation. The Fourier calculations and animation generation are performed by the Python script.

---

## 📌 About the Project

Can a complex geographical shape be reconstructed using nothing but rotating circles?

This project demonstrates the mathematical idea behind that question.

The geographical boundary of Maharashtra is represented as a sequence of points. A Discrete Fourier Transform converts these points into frequency components, which are then visualized as rotating vectors.

Each vector contributes to the overall motion. When connected end-to-end, the vectors form epicycles whose final endpoint traces an approximation of the original boundary.

The project combines mathematics, geospatial data processing, Python programming, and scientific visualization in one animation.

### ✨ Key Features

* 🗺️ Geographical boundary visualization of Maharashtra, India.
* 🌀 Fourier-based reconstruction using rotating epicycles.
* 📐 Discrete Fourier Transform calculations.
* 🎬 MP4 animation generation.
* 🌐 Browser-based video playback using Streamlit.
* 🐍 Scientific computing and visualization with Python.

---

## 🧠 How Does It Work?

### 1. Obtain the Boundary

The project uses geographical boundary data stored in GeoJSON format.

### 2. Extract Coordinates

The boundary is converted into a sequence of two-dimensional points represented as complex numbers:

$$
z_n = x_n + iy_n
$$

Here, \(x_n\) and \(y_n\) represent the two coordinate components.

### 3. Apply the Fourier Transform

The Discrete Fourier Transform converts the sampled coordinates into frequency components:

$$
X_k = \sum_{n=0}^{N-1} z_n e^{-i2\pi kn/N}
$$

These coefficients contain the information needed to reconstruct the sampled shape.

### 4. Build the Epicycles

Each selected Fourier coefficient defines a rotating vector.

* **Magnitude:** Determines the vector's length.
* **Frequency:** Determines its rotation rate and direction.
* **Phase:** Determines its initial angular position.

Connecting these rotating vectors creates the epicycle chain.

### 5. Trace the Shape

As the vectors rotate, the endpoint of the final vector traces the reconstructed boundary.

The selected Fourier components determine how closely the reconstructed path resembles the original shape.

### 6. Generate the Animation

Python and Matplotlib render the motion and export it as an MP4 video. Streamlit then displays the generated video in the web application.

---

## 🛠️ Technology Stack

| Technology   | Purpose                                      |
| ------------ | -------------------------------------------- |
| Python       | Core programming language                    |
| NumPy        | Numerical calculations and Fourier transform |
| Matplotlib   | Visualization and animation                  |
| Shapely      | Geometrical processing                       |
| GeoJSON      | Geographical boundary data                   |
| FFmpeg       | MP4 video encoding                           |
| Streamlit    | Web application                              |
| Git & GitHub | Version control and source code hosting      |

---

## 📂 Project Structure

```text
maharashtra-fourier-epicycles/
│
├── app.py
├── maharashtra_fourier.py
├── maharashtra.geojson
├── maharashtra_fourier.mp4
├── download_map.py
├── requirements.txt
└── README.md
```

| File                      | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| `app.py`                  | Streamlit application that displays the animation         |
| `maharashtra_fourier.py`  | Fourier calculations, epicycles, and animation generation |
| `maharashtra.geojson`     | Geographical boundary data                                |
| `maharashtra_fourier.mp4` | Generated animation                                       |
| `download_map.py`         | Script for downloading boundary data                      |
| `requirements.txt`        | Python dependencies for deployment                        |
| `README.md`               | Project documentation                                     |

---

## ⚙️ Run the Project Locally

### Prerequisites

* Python 3
* Git
* FFmpeg, if regenerating the animation

### Step 1 — Clone the Repository

```bash
git clone https://github.com/aditya280505/maharashtra-fourier-epicycles.git
```

### Step 2 — Enter the Project Directory

```bash
cd maharashtra-fourier-epicycles
```

### Step 3 — Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

For local animation generation, install the additional scientific libraries if they are not already included:

```bash
pip install numpy matplotlib shapely
```

FFmpeg must also be installed and configured for Matplotlib video export.

### Step 5 — Launch the Web Application

```bash
streamlit run app.py
```

Open the local address shown in your terminal, usually:

**http://localhost:8501**

Make sure `maharashtra_fourier.mp4` exists in the expected project directory.

---

## 🎬 Regenerate the Animation

To generate the animation again, run:

```bash
python maharashtra_fourier.py
```

The script processes the boundary coordinates, calculates Fourier components, renders the epicycle animation, and exports the MP4 video.

### Animation Parameters

The following settings can be adjusted in the Python script:

| Parameter      | Purpose                                     |
| -------------- | ------------------------------------------- |
| `NUM_CIRCLES`  | Number of Fourier components used           |
| `FRAMES`       | Total number of animation frames            |
| `FPS`          | Frames rendered per second                  |
| `EXPORT_MP4`   | Controls video export                       |
| `SHOW_CIRCLES` | Controls the visibility of epicycle circles |

The visual result depends on the selected Fourier components, coordinate sampling, and animation settings.

---

## 📦 Deployment Dependencies

The deployed application only needs Streamlit when it plays the existing MP4 file.

Example `requirements.txt`:

```text
streamlit
```

For regenerating the animation locally, NumPy, Matplotlib, Shapely, and a working FFmpeg installation are also required.

---

## 🌍 Geographical Data Source

The project uses Maharashtra boundary data from DataMeet.

**[View Maharashtra GeoJSON Data](https://raw.githubusercontent.com/datameet/maps/master/States/Maharashtra.geojson)**

The GeoJSON coordinates serve as the input for the boundary-processing and Fourier reconstruction steps.

---

## 📚 Concepts Demonstrated

* Discrete Fourier Transform
* Fourier Series and frequency components
* Complex numbers and rotating vectors
* Epicycles and shape reconstruction
* Geospatial data processing
* Scientific visualization
* Python animation and MP4 rendering
* Streamlit application deployment

---

## 🔮 Future Enhancements

Potential improvements include:

* Interactive control over the number of epicycles.
* Adjustable animation speed.
* Step-by-step visualization of Fourier components.
* Support for additional geographical boundaries.
* Custom shape uploads.
* Comparison between the original and reconstructed boundaries.
* Interactive playback controls.

---

## 👨‍💻 Author

**Aditya Borgaonkar**

Computer Science Engineering — Artificial Intelligence & Analytics
MIT ADT University, Pune

<p align="center">
  <a href="https://github.com/aditya280505">
    <img src="https://img.shields.io/badge/GitHub-aditya280505-181717?style=for-the-badge&logo=github" alt="Aditya Borgaonkar on GitHub">
  </a>
  <a href="https://maharashtra-fourier-epicycles.streamlit.app/">
    <img src="https://img.shields.io/badge/Live_Demo-Open_Application-FF4B4B?style=for-the-badge" alt="Open Live Application">
  </a>
</p>
