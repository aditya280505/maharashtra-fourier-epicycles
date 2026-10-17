<div align="center">

# 🌀 Maharashtra Fourier Epicycles

### ✨ Turning the Map of Maharashtra into Mathematical Art

**A Python-powered visualization that reconstructs the outline of Maharashtra using Fourier transforms and rotating epicycles.**

<br>

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python\&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Fourier%20Transform-013243?style=for-the-badge\&logo=numpy\&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Animation-11557c?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

<br>

**🎬 Mathematical equations meet creative visualization.**

</div>

---

## 🌌 About the Project

What if we could draw the geographical outline of Maharashtra using nothing but rotating circles?

**Maharashtra Fourier Epicycles** is a mathematical visualization project that uses the **Discrete Fourier Transform (DFT)** to represent the state's geographical boundary as a collection of rotating vectors, known as *epicycles*.

Each circle contributes to the reconstruction of the original shape. As the vectors rotate, their combined endpoint traces the outline of Maharashtra.

The result is an animated demonstration of how complex geographical shapes can be approximated using a series of circular motions.

## 🎥 Animation Preview

The animation is generated as an MP4 video using Python and FFmpeg.

**▶️ [Watch the Animation](maharashtra_fourier.mp4)**

> 💡 Download or open the MP4 file from this repository to watch the complete animation.

## ✨ Features

* 🗺️ **Real Geographical Boundary** — Extracts Maharashtra's outer boundary from GeoJSON map data.
* 🔄 **Fourier Transform** — Converts boundary coordinates into complex Fourier coefficients.
* 🌀 **128 Epicycles** — Uses the strongest Fourier components to reconstruct the outline.
* 🎨 **Animated Visualization** — Displays rotating circles, connecting vectors and a continuously drawn trail.
* 🎬 **MP4 Export** — Renders the animation using FFmpeg.
* 📐 **Boundary Resampling** — Samples the closed boundary evenly to prepare it for Fourier analysis.
* ⚡ **Customizable Animation** — Adjusts the number of circles, frames, frame rate and visualization options.

## 🧠 How It Works

The project follows these steps:

**1. Load the Map**
Read the Maharashtra GeoJSON file and extract the geographical polygons.

**2. Extract the Boundary**
Combine district polygons into a single geometry and select its main outer boundary.

**3. Prepare the Coordinates**
Resample the boundary into evenly spaced points, center the shape and normalize its size.

**4. Apply the Fourier Transform**
Use NumPy's FFT to calculate the complex Fourier coefficients representing the boundary.

**5. Select the Dominant Frequencies**
Keep the strongest 128 Fourier components to construct the rotating epicycles.

**6. Animate the Reconstruction**
Calculate the rotating vectors frame by frame and draw their endpoint trajectory.

**7. Export the Video**
Use Matplotlib and FFmpeg to save the final animation as an MP4 file.

## 🛠️ Tech Stack

| Technology | Purpose                                      |
| ---------- | -------------------------------------------- |
| Python     | Core programming language                    |
| NumPy      | Fourier transform and numerical calculations |
| Matplotlib | Epicycle visualization and animation         |
| Shapely    | Geometric operations and polygon processing  |
| GeoJSON    | Maharashtra geographical boundary data       |
| FFmpeg     | MP4 video rendering                          |

## 📂 Project Structure

```text
maharashtra-fourier-epicycles/
│
├── maharashtra_fourier.py    # Main animation script
├── download_map.py           # Downloads geographical map data
├── maharashtra.geojson        # Maharashtra district boundaries
├── maharashtra_fourier.mp4   # Generated animation
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## ⚙️ Installation & Setup

### Prerequisites

* Python 3.10 or later
* Git
* FFmpeg

### 1. Clone the Repository

```bash
git clone https://github.com/aditya280505/maharashtra-fourier-epicycles.git
cd maharashtra-fourier-epicycles
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

Download FFmpeg from the official website:

https://ffmpeg.org/download.html

Make sure FFmpeg is installed and its executable path is configured correctly in the Python script.

### 4. Run the Project

```bash
python maharashtra_fourier.py
```

The animation will be rendered and saved as:

```text
maharashtra_fourier.mp4
```

> **Note:** The script expects `maharashtra.geojson` to exist in the project directory. If the file is missing, run `download_map.py` first and ensure the downloaded data has the expected GeoJSON structure.

## 🎛️ Customize the Animation

You can modify these settings in `maharashtra_fourier.py`:

```python
NUM_CIRCLES = 128
FRAMES = 600
FPS = 30

EXPORT_MP4 = True
SHOW_CIRCLES = True
```

| Parameter      | Description                         |
| -------------- | ----------------------------------- |
| `NUM_CIRCLES`  | Number of Fourier components used   |
| `FRAMES`       | Total animation frames              |
| `FPS`          | Video frame rate                    |
| `EXPORT_MP4`   | Enables or disables video export    |
| `SHOW_CIRCLES` | Shows or hides the epicycle circles |

Increasing the number of Fourier components can improve the reconstruction's detail, while also increasing the amount of work required per frame.

## 📚 Mathematical Concept

The project represents boundary coordinates as complex numbers:

$$
z = x + iy
$$

The Fourier coefficients are calculated using the Discrete Fourier Transform:

$$
c_k = \frac{1}{N}\sum_{n=0}^{N-1} z_n e^{-2\pi i kn/N}
$$

The boundary can then be approximated by summing rotating complex vectors:

$$
z(t) = \sum_{k \in K} c_k e^{2\pi i kt}
$$

Where:

* \(z_n\) represents a sampled boundary coordinate.
* \(c_k\) represents a Fourier coefficient.
* \(K\) is the set of selected frequencies.
* \(t\) represents animation time.

Each term contributes a rotating vector. Together, these vectors reconstruct the original boundary.

## 🚀 Future Improvements

* [ ] Add a live animation preview mode.
* [ ] Improve reconstruction accuracy by tuning the number of Fourier components.
* [ ] Support other Indian states and geographical boundaries.
* [ ] Add configurable video resolution and quality.
* [ ] Create interactive controls for Fourier frequencies and animation speed.

## 👨‍💻 Author

<div align="center">

### Aditya Pravin Borgaonkar

**AI & Analytics Undergraduate | Python Developer**

Exploring the intersection of mathematics, programming and creative visualization.

<br>

[![GitHub](https://img.shields.io/badge/GitHub-aditya280505-181717?style=for-the-badge\&logo=github)](https://github.com/aditya280505)

</div>

---

