# 9.4 Vision Systems and Sensors

Vision systems and sensors enable robots to locate parts, verify placement, inspect quality, and adapt to position variations.

## Machine Vision Fundamentals

**Purpose**
- Part localization (X, Y, rotation)
- Presence/absence detection
- Quality inspection (defects, orientation)
- Barcode/OCR reading
- Measurement and gauging

**System Components**
- Camera (CCD or CMOS sensor)
- Lens (fixed focal length or adjustable)
- Lighting (LED ring, backlight, dome)
- Image processing computer
- Software (OpenCV, Halcon, Cognex VisionPro)

## Camera Selection

**Sensor Types**

CCD (Charge-Coupled Device):
- High image quality
- Better low-light performance
- Higher cost
- Slower frame rates

CMOS (Complementary Metal-Oxide Semiconductor):
- Lower cost
- Faster frame rates
- Lower power consumption
- Common in modern systems

**Resolution**
- VGA: 640×480 (sufficient for simple tasks)
- 1MP: 1280×1024 (general purpose)
- 5MP+: High-precision inspection

Field of view calculation:
```
FOV = (sensor_size / focal_length) × working_distance
```

**Frame Rate**
- 30 fps: Standard for pick-and-place
- 60+ fps: High-speed applications
- Triggered capture: Synchronized with motion

**Interface**
- USB 3.0: Simple, moderate speed
- GigE: Longer cables, industrial standard
- Camera Link: High bandwidth, expensive

## Lens Selection

**Focal Length**
- Short (8-16mm): Wide field of view
- Medium (25-50mm): General purpose
- Long (>50mm): Narrow field, distant objects

**Aperture (f-stop)**
- Low f-number (f/1.4-f/2.8): More light, shallow depth of field
- High f-number (f/8-f/16): Less light, greater depth of field

**Depth of Field**
Critical for 3D objects:
```
DOF ≈ (2 × N × C × d²) / f²
```
- N = f-stop number
- C = circle of confusion
- d = working distance
- f = focal length

## Lighting Techniques

**Lighting Types**

Ring Light:
- Mounts around lens
- Even illumination
- Reduces shadows
- General purpose

Backlight:
- Part silhouette
- Edge detection
- Hole/slot inspection
- High contrast

Dome Light:
- Diffuse illumination
- Eliminates reflections
- Good for shiny surfaces

Structured Light:
- Projects pattern (lines, grid)
- 3D measurement
- Height profiling

**Color**
- White: General purpose
- Red (630nm): High contrast, deep penetration
- Blue (470nm): High resolution
- IR (850nm+): See through some plastics

**Polarization**
- Reduces glare from reflective surfaces
- Polarizing filters on light and camera

## Vision Processing

**Image Acquisition**
- Triggered by robot position or external signal
- Consistent lighting critical
- Exposure time vs. motion blur trade-off

**Pre-Processing**
- Noise reduction (Gaussian blur, median filter)
- Contrast enhancement
- Color space conversion (RGB to grayscale or HSV)

**Feature Extraction**

Edge Detection:
- Sobel, Canny algorithms
- Finds part boundaries

Blob Analysis:
- Identifies connected regions
- Measures area, centroid, orientation

Template Matching:
- Correlates image with known pattern
- Returns position and rotation
- Sensitive to scale and lighting changes

**Pattern Recognition**
- Feature-based (SIFT, SURF, ORB)
- Robust to rotation, scale, partial occlusion
- Higher computational cost

**Calibration**
- Camera intrinsics (lens distortion)
- Camera-to-robot transformation
- Pixel-to-mm conversion

Calibration grid method:
```
mm_per_pixel = known_distance / pixel_distance
```

## Common Vision Tasks

**Part Localization**
1. Acquire image
2. Find part features (edges, blobs)
3. Calculate centroid and rotation
4. Transform to robot coordinates
5. Update pick position

**Presence Detection**
- Simple threshold or blob count
- Verify part before pick attempt
- Confirm placement after release

**Orientation Verification**
- Detect asymmetric features
- Ensure correct part rotation
- Reject or correct misaligned parts

**Quality Inspection**
- Measure dimensions
- Detect defects (scratches, dents)
- Color verification
- Label/marking presence

## 2D Vision System Example

**PCB Pick-and-Place**
- Camera: 1MP CMOS, USB 3.0
- Lens: 16mm, f/2.8
- Lighting: White LED ring light
- Field of view: 100×100 mm
- Resolution: 0.1 mm/pixel
- Processing: OpenCV on Raspberry Pi
- Cycle time: 200ms per image

**Processing Steps**
1. Capture image when part enters FOV
2. Convert to grayscale
3. Threshold to binary image
4. Find largest blob (PCB outline)
5. Calculate centroid and orientation
6. Transform to robot coordinates
7. Send offset to motion controller

## 3D Vision

**Techniques**

Laser Triangulation:
- Laser line projected on part
- Camera observes line deflection
- Calculates height profile

Stereo Vision:
- Two cameras at known separation
- Matches features between images
- Calculates depth from disparity

Structured Light:
- Projects pattern (stripes, dots)
- Analyzes pattern distortion
- Generates 3D point cloud

Time-of-Flight:
- Measures light travel time
- Direct depth measurement
- Lower resolution than other methods

**Applications**
- Bin picking (random part orientation)
- Height measurement
- Volume calculation
- Complex part recognition

## Proximity Sensors

**Inductive Sensors**
- Detect ferrous and non-ferrous metals
- Sensing distance: 1-20mm
- Fast response (<1ms)
- Use: Metal part presence

**Capacitive Sensors**
- Detect any material (different sensitivity)
- Sensing distance: 5-30mm
- Use: Plastic, liquid, powder detection

**Photoelectric Sensors**

Through-Beam:
- Separate emitter and receiver
- Long range (up to 30m)
- Most reliable
- Use: Part presence, counting

Retro-Reflective:
- Reflector returns light to sensor
- Medium range (up to 5m)
- Single mounting location

Diffuse:
- Detects object reflection
- Short range (<1m)
- Simple installation

**Ultrasonic Sensors**
- Measures distance via sound echo
- Range: 50mm to 5m
- Immune to color/transparency
- Use: Level sensing, distance measurement

**Laser Distance Sensors**
- Precise distance measurement
- Range: 50mm to 300m
- High accuracy (±1mm or better)
- Use: Height profiling, positioning

## Force and Torque Sensors

**Load Cells**
- Strain gauge based
- Measure grip force
- Prevent part damage
- Verify secure grip

**6-Axis F/T Sensors**
- Measure force (Fx, Fy, Fz)
- Measure torque (Tx, Ty, Tz)
- Enable compliant assembly
- High cost ($2k-$10k+)

**Applications**
- Peg-in-hole insertion
- Contact detection
- Quality assurance (press fits)

## Sensor Integration

**Digital I/O**
- Simple presence/absence sensors
- 24V industrial standard
- Direct connection to PLC or controller

**Analog Input**
- Distance, force, pressure sensors
- 0-10V or 4-20mA signals
- Requires ADC on controller

**Network Communication**
- Vision systems via Ethernet
- Modbus TCP, EtherCAT, PROFINET
- Higher bandwidth, more data

## Vision Software

**Open Source**
- OpenCV: Comprehensive library, C++/Python
- SimpleCV: Python wrapper for OpenCV
- Scikit-image: Python image processing

**Commercial**
- Cognex VisionPro: Industry standard, expensive
- National Instruments Vision: LabVIEW integration
- Halcon: Powerful, MVTec software

**DIY Implementation**
Python + OpenCV example:
```python
import cv2
import numpy as np

# Capture image
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

# Get largest contour
largest = max(contours, key=cv2.contourArea)

# Calculate centroid
M = cv2.moments(largest)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# Send to robot controller
```

## Calibration and Accuracy

**Hand-Eye Calibration**
- Determines transformation between camera and robot
- Move robot to known positions
- Capture images of calibration target
- Solve transformation matrix

**Performance Metrics**
- Repeatability: ±0.1-0.5mm typical for 2D vision
- Accuracy: Depends on calibration quality
- Cycle time: 100-500ms per image

***

**Next**: [9.5 Motion Control and Path Planning](section-9.5-motion-control.md)

---

## References

1. **Machine Vision Software**
   - Bradski, G. & Kaehler, A. (2008). *Learning OpenCV*. O'Reilly
   - OpenCV Documentation - opencv.org
   - Halcon Machine Vision - MVTec Software GmbH

2. **Camera and Optics**
   - FLIR (Basler) Industrial Camera Selection Guide
   - Edmund Optics - Imaging Optics Technical Library
   - GigE Vision and Camera Link Standards

3. **Image Processing**
   - Gonzalez, R.C. & Woods, R.E. (2018). *Digital Image Processing*. Pearson
   - Szeliski, R. (2022). *Computer Vision: Algorithms and Applications*. Springer

4. **Calibration**
   - Zhang, Z. (2000). "Camera Calibration Technique". *IEEE Trans. PAMI*
