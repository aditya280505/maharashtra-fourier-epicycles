import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from matplotlib.animation import FuncAnimation, FFMpegWriter
from pathlib import Path
from shapely.geometry import shape
from shapely.ops import unary_union


# ==========================================
# FFMPEG CONFIGURATION
# ==========================================

mpl.rcParams["animation.ffmpeg_path"] = (
    r"C:\Uffmpeg-9.0.2-essentials_build"
    r"\ffmpeg-9.0.2-essentials_build\bin\ffmpeg.exe"
)


# ==========================================
# CONFIGURATION
# ==========================================

MAP_FILE = "maharashtra.geojson"
VIDEO_FILE = "maharashtra_fourier.mp4"

NUM_CIRCLES = 128

FRAMES = 860       # Increased from 600 for slower animation
FPS = 30            # Keep 30 FPS for smooth playback

EXPORT_MP4 = True
SHOW_CIRCLES = True


# ==========================================
# LOAD MAHARASHTRA GEOJSON
# ==========================================

print("Loading Maharashtra map...")

map_path = Path(MAP_FILE)

if not map_path.exists():
    raise FileNotFoundError(
        f"{MAP_FILE} not found. Run download_map.py first."
    )

with open(map_path, "r", encoding="utf-8") as file:
    geo_data = json.load(file)


# ==========================================
# EXTRACT MAHARASHTRA'S OUTER BOUNDARY
# ==========================================

print("Combining map polygons...")

geometries = []

if geo_data.get("type") == "FeatureCollection":

    for feature in geo_data.get("features", []):
        geometry = feature.get("geometry")

        if geometry:
            geometries.append(shape(geometry))

elif geo_data.get("type") == "Feature":

    geometries.append(shape(geo_data["geometry"]))

else:
    geometries.append(shape(geo_data))


if not geometries:
    raise ValueError("No valid geometries found in GeoJSON.")


# Combine district polygons into one geometry
merged = unary_union(geometries)


# Select the main landmass
if merged.geom_type == "Polygon":

    main_polygon = merged

elif merged.geom_type == "MultiPolygon":

    main_polygon = max(
        merged.geoms,
        key=lambda polygon: polygon.area
    )

else:
    raise ValueError(
        f"Unexpected geometry type: {merged.geom_type}"
    )


# Extract exterior boundary
boundary = np.asarray(
    main_polygon.exterior.coords,
    dtype=float
)

print("Maharashtra outer boundary extracted!")
print("Boundary points:", len(boundary))


# Remove repeated closing point
if np.allclose(boundary[0], boundary[-1]):
    boundary = boundary[:-1]

print(f"Map boundary loaded: {len(boundary)} points")


# ==========================================
# RESAMPLE BOUNDARY EVENLY
# ==========================================

print("Preparing boundary points...")


def resample_closed_curve(points, number_of_points=2048):
    """Sample points evenly by distance around a closed boundary."""

    points = np.asarray(points, dtype=float)

    # Close the curve
    closed = np.vstack([points, points[0]])

    distances = np.sqrt(
        np.sum(np.diff(closed, axis=0) ** 2, axis=1)
    )

    cumulative = np.concatenate([[0], np.cumsum(distances)])
    total_length = cumulative[-1]

    if total_length == 0:
        raise ValueError("Boundary has zero length.")

    sample_distances = np.linspace(
        0,
        total_length,
        number_of_points,
        endpoint=False
    )

    x = np.interp(
        sample_distances,
        cumulative,
        closed[:, 0]
    )

    y = np.interp(
        sample_distances,
        cumulative,
        closed[:, 1]
    )

    return x + 1j * y


points = resample_closed_curve(boundary, 2048)


# Center the map around the origin
points = points - np.mean(points)


# Normalize its size
max_radius = np.max(np.abs(points))
points = points / max_radius


# ==========================================
# FOURIER TRANSFORM
# ==========================================

print("Calculating Fourier coefficients...")

coefficients = np.fft.fft(points) / len(points)

frequencies = np.fft.fftfreq(
    len(points),
    d=1 / len(points)
)


# Keep the strongest Fourier components
indices = np.argsort(np.abs(coefficients))[::-1]
indices = indices[:NUM_CIRCLES]

fourier_coefficients = coefficients[indices]
fourier_frequencies = frequencies[indices]

print(f"Using {NUM_CIRCLES} Fourier circles.")


# ==========================================
# FOURIER EPICYCLES
# ==========================================

def calculate_epicycles(t):
    """Calculate the endpoint of every rotating Fourier vector."""

    x = 0j

    centers = []
    endpoints = []

    for coefficient, frequency in zip(
        fourier_coefficients,
        fourier_frequencies
    ):

        centers.append(x)

        vector = coefficient * np.exp(
            2j * np.pi * frequency * t
        )

        x += vector
        endpoints.append(x)

    return centers, endpoints


# ==========================================
# MATPLOTLIB ANIMATION
# ==========================================

print("Creating animation...")

fig, ax = plt.subplots(figsize=(9, 9))

fig.patch.set_facecolor("#10131c")
ax.set_facecolor("#10131c")

ax.set_aspect("equal")

ax.set_xlim(-1.35, 1.35)
ax.set_ylim(-1.35, 1.35)

ax.axis("off")


# Title
fig.suptitle(
    "MAHARASHTRA | FOURIER EPICYCLES",
    color="white",
    fontsize=17,
    fontweight="bold",
    y=0.95,
)


# Creator branding
fig.text(
    0.5,
    0.065,
    "Powered by Aditya Borgaonkar",
    ha="center",
    va="center",
    fontsize=11,
    color="white",
    alpha=0.9,
    fontweight="medium"
)


# Faint original boundary for reference
ax.plot(
    points.real,
    points.imag,
    color="#45506b",
    linewidth=1,
    alpha=0.5,
)


# Animated drawing trail
trail_line, = ax.plot(
    [],
    [],
    color="#42e8f5",
    linewidth=2,
)


# Current endpoint
endpoint_dot, = ax.plot(
    [],
    [],
    "o",
    color="#ffffff",
    markersize=4,
)


# Draw rotating circles and connecting vectors
circles = []
vectors = []

if SHOW_CIRCLES:

    for _ in range(NUM_CIRCLES):

        circle, = ax.plot(
            [],
            [],
            color="#6575a8",
            linewidth=0.55,
            alpha=0.6,
        )

        circles.append(circle)

        vector, = ax.plot(
            [],
            [],
            color="#f4b942",
            linewidth=0.8,
            alpha=0.9,
        )

        vectors.append(vector)


trail_x = []
trail_y = []


# ==========================================
# INITIALIZE ANIMATION
# ==========================================

def init():

    trail_x.clear()
    trail_y.clear()

    trail_line.set_data([], [])
    endpoint_dot.set_data([], [])

    for circle in circles:
        circle.set_data([], [])

    for vector in vectors:
        vector.set_data([], [])

    return (
        [trail_line, endpoint_dot]
        + circles
        + vectors
    )


# ==========================================
# UPDATE ANIMATION FRAME
# ==========================================

def update(frame):

    # Complete one Fourier cycle over 860 frames
    t = frame / FRAMES

    centers, endpoints = calculate_epicycles(t)

    # Draw all epicycle circles and vectors
    if SHOW_CIRCLES:

        for i, (center, endpoint) in enumerate(
            zip(centers, endpoints)
        ):

            radius = abs(fourier_coefficients[i])

            angle = np.linspace(
                0,
                2 * np.pi,
                80
            )

            circle_x = (
                center.real + radius * np.cos(angle)
            )

            circle_y = (
                center.imag + radius * np.sin(angle)
            )

            circles[i].set_data(
                circle_x,
                circle_y
            )

            vectors[i].set_data(
                [center.real, endpoint.real],
                [center.imag, endpoint.imag],
            )


    # Endpoint of the complete Fourier chain
    endpoint = endpoints[-1]

    trail_x.append(endpoint.real)
    trail_y.append(endpoint.imag)

    trail_line.set_data(
        trail_x,
        trail_y
    )

    endpoint_dot.set_data(
        [endpoint.real],
        [endpoint.imag],
    )


    # Progress indicator
    if frame % 100 == 0:
        print(f"Animation progress: {frame}/{FRAMES}")


    return (
        [trail_line, endpoint_dot]
        + circles
        + vectors
    )


# ==========================================
# CREATE ANIMATION
# ==========================================

ani = FuncAnimation(
    fig,
    update,
    frames=FRAMES,
    init_func=init,
    interval=1000 / FPS,
    blit=True,
    repeat=True,
)


# ==========================================
# EXPORT MP4
# ==========================================

if EXPORT_MP4:

    print(f"Exporting video to {VIDEO_FILE}...")
    print("Please wait; video rendering can take some time.")

    writer = FFMpegWriter(
        fps=FPS,
        codec="libx264",
        bitrate=3000,
        metadata={
            "title": "Maharashtra Fourier Epicycles"
        },
    )

    ani.save(
        VIDEO_FILE,
        writer=writer,
        dpi=120,
    )

    print(
        f"Video saved successfully: "
        f"{Path(VIDEO_FILE).resolve()}"
    )


# ==========================================
# SHOW LIVE ANIMATION
# ==========================================

print("Opening animation window...")

plt.show()