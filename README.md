<div align="center">

# 🌀 MAHARASHTRA

# FOURIER EPICYCLES

### Turning Geography into Mathematics.

**What if rotating circles could draw an entire state?**

A mathematical visualization of Maharashtra's geographical outline using Fourier transforms, complex numbers, and rotating epicycles.

<br>

<a href="https://maharashtra-fourier-epicycles.streamlit.app/">
  <img src="https://img.shields.io/badge/▶%20EXPLORE%20LIVE%20DEMO-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Explore Live Demo">
</a>

<a href="#-how-it-works">
  <img src="https://img.shields.io/badge/UNDERSTAND%20THE%20MATH-20232A?style=for-the-badge" alt="Understand the Math">
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy">
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square" alt="Matplotlib">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">

</div>

---

## ✨ Experience the Project

<div align="center">

### 🗺️ One State. Many Circles. One Continuous Path.

**[🚀 OPEN THE LIVE ANIMATION](https://maharashtra-fourier-epicycles.streamlit.app/)**

Watch the epicycles rotate and trace the outline of Maharashtra.

</div>

> 💡 **Quick tip:** Open the live demo first to experience the animation. Then explore the sections below to understand the mathematics behind it.

---

## 🧭 Explore

| Discover                                    | What you'll learn                                 |
| :------------------------------------------ | :------------------------------------------------ |
| [🎯 The Idea](#-the-idea)                   | What the project does and why it is interesting   |
| [⚙️ How It Works](#-how-it-works)           | From geographical coordinates to rotating circles |
| [🧮 The Mathematics](#-the-mathematics)     | Fourier transforms and complex numbers            |
| [🛠️ Technology](#️-technology-stack)       | Tools and libraries used                          |
| [💻 Run Locally](#-run-it-on-your-computer) | Set up the project on your machine                |
| [🔮 What's Next](#-future-possibilities)    | Ideas for making it even better                   |

---

## 🎯 The Idea

A geographical boundary may look complicated, but it can be represented as a combination of simpler mathematical components.

This project takes the outline of Maharashtra and uses the **Discrete Fourier Transform (DFT)** to represent its sampled boundary coordinates as rotating vectors.

When those vectors rotate together, their combined endpoint traces an approximation of the original shape.

**The result:** a mathematical animation that connects geography, signal processing, and computer visualization.

### Why is this interesting?

* **Mathematics becomes visual:** Fourier coefficients become rotating circles.
* **Complex shapes become understandable:** A boundary is reconstructed from simpler components.
* **Data becomes an animation:** Geographical coordinates are transformed into a visual experience.

---

## ⚙️ How It Works

<div align="center">

**STEP 01 — GEOGRAPHICAL DATA**

🗺️ Maharashtra boundary in GeoJSON

⬇️

**STEP 02 — COORDINATE PROCESSING**

📍 Extract and prepare boundary points

⬇️

**STEP 03 — FOURIER TRANSFORM**

🧮 Calculate frequency components

⬇️

**STEP 04 — EPICYCLE CONSTRUCTION**

🌀 Combine rotating vectors

⬇️

**STEP 05 — ANIMATION**

🎬 Trace the reconstructed boundary

⬇️

**FINAL RESULT**

✨ A Fourier-based visualization of Maharashtra

</div>

### 1. Get the Boundary

The project uses geographical coordinates stored in GeoJSON format.

### 2. Represent the Coordinates

The sampled two-dimensional points are represented using complex numbers:

$$
z_n = x_n + iy_n
$$

Here, \(x_n\) and \(y_n\) represent the two coordinate components.

### 3. Calculate Fourier Coefficients

The Discrete Fourier Transform converts the sequence of points into frequency components:

$$
X_k = \sum_{n=0}^{N-1} z_n e^{-i2\pi kn/N}
$$

These coefficients encode the information used to reconstruct the sampled path.

### 4. Build Rotating Epicycles

Each selected Fourier coefficient defines a rotating vector.

* **Magnitude** determines its length.
* **Frequency** determines its rotation rate and direction.
* **Phase** determines its initial angular position.

### 5. Draw the Shape

The vectors rotate together, and the endpoint of the final vector traces the reconstructed boundary.

The quality of the reconstruction depends on the selected Fourier components and the coordinate sampling.

---

## 🧮 The Mathematics Behind the Magic

The central idea is that a sampled periodic path can be represented through a collection of complex Fourier components.

Each component contributes a rotating vector:

$$
z(t) = \sum_{k=0}^{N-1} X_k e^{i2\pi kt/N}
$$

The implementation may reorder or normalize Fourier coefficients for its particular animation. The expression above illustrates the underlying reconstruction principle.

Think of it this way:

* One rotating vector creates a simple circular motion.
* Several rotating vectors combine into a more complex path.
* A carefully selected collection of components can approximate the original boundary.

**That's the core idea behind Fourier epicycles.**

---

## 🛠️ Technology Stack

| Technology      | Role in the Project                           |
| :-------------- | :-------------------------------------------- |
| 🐍 Python       | Main programming language                     |
| 🔢 NumPy        | Fourier calculations and numerical operations |
| 📊 Matplotlib   | Drawing and rendering the animation           |
| 📐 Shapely      | Geometrical processing of boundary data       |
| 🗺️ GeoJSON     | Geographical boundary representation          |
| 🎬 FFmpeg       | MP4 video encoding                            |
| 🌐 Streamlit    | Live web application                          |
| 🔗 Git & GitHub | Source control and repository hosting         |

---

## 📁 Project Structure

```text
maharashtra-fourier-epicycles/
│
├── app.py                    # Web application
├── maharashtra_fourier.py    # Fourier and animation logic
├── maharashtra.geojson       # Maharashtra boundary data
├── maharashtra_fourier.mp4   # Generated animation
├── download_map.py           # Boundary download script
├── requirements.txt          # App dependencies
└── README.md                 # Project documentation
```

---

## 💻 Run It on Your Computer

Want to explore the code locally? Follow these steps.

### ① Clone the repository

```bash
git clone https://github.com/aditya280505/maharashtra-fourier-epicycles.git
```

### ② Open the project directory

```bash
cd maharashtra-fourier-epicycles
```

### ③ Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### ④ Install dependencies

```bash
pip install -r requirements.txt
```

For local animation generation, install the scientific libraries if they are not already installed:

```bash
pip install numpy matplotlib shapely
```

FFmpeg is also required for MP4 generation and must be configured for Matplotlib.

### ⑤ Launch the application

```bash
streamlit run app.py
```

Open the local address displayed in your terminal, usually:

**http://localhost:8501**

The generated video `maharashtra_fourier.mp4` must be available at the path expected by the application.

### 🎬 Generate the animation again

To regenerate the video, run:

```bash
python maharashtra_fourier.py
```

The script processes the boundary coordinates, calculates Fourier components, renders the animation, and exports the MP4 file.

---

## 🔧 Animation Controls in the Code

The Python script includes parameters that can be adjusted to experiment with the visualization.

| Parameter      | What it changes                      |
| :------------- | :----------------------------------- |
| `NUM_CIRCLES`  | Number of Fourier components used    |
| `FRAMES`       | Number of animation frames           |
| `FPS`          | Video frame rate                     |
| `EXPORT_MP4`   | Whether to export an MP4             |
| `SHOW_CIRCLES` | Whether to show the epicycle circles |

Changing these parameters can affect the reconstruction detail, animation duration, and rendering time.

---

## 🔮 Future Possibilities

This project could be extended with:

* 🎛️ Interactive controls for epicycle count and animation speed.
* ⏯️ Playback controls for pausing and restarting.
* 🗺️ Support for other state and country boundaries.
* ✏️ Custom-shape uploads for Fourier reconstruction.
* 🔍 Side-by-side comparison of the original and reconstructed shapes.
* 📈 Visualization of individual Fourier components.

These are potential improvements, not features currently guaranteed by the application.

---

## 👨‍💻 About the Developer

<div align="center">

### Aditya Borgaonkar

Computer Science Engineering — Artificial Intelligence & Analytics
MIT ADT University, Pune

<a href="https://github.com/aditya280505">
  <img src="https://img.shields.io/badge/Explore_My_GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="Explore GitHub">
</a>

<br><br>

**[🌀 Try the Live Project](https://maharashtra-fourier-epicycles.streamlit.app/)**

*Turning mathematical concepts into visual experiences.*

</div>
