import sys
import os
sys.path.append(os.path.abspath('/content/DeepLSD'))

import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt

# Import the DeepLSD class directly from deeplsd_inference
from deeplsd.models.deeplsd_inference import DeepLSD

# 1. Configuration setup and model loading (using GPU if available)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
conf = {
    'detect_lines': True,
    'line_detection_params': {
        'merge': False,
        'filtering': False,
        'grad_thresh': 3.0,
    }
}

# Initialize the model using the DeepLSD class
ckpt_path = '/content/DeepLSD/weights/deeplsd_md.tar'
net = DeepLSD(conf)

# Load the weights
state_dict = torch.load(ckpt_path, map_location=device, weights_only=False)
if 'model' in state_dict:
    net.load_state_dict(state_dict['model'])
else:
    net.load_state_dict(state_dict)

net = net.to(device).eval()

# 2. Read the test image
img_path = '/content/image_name.jpg'

# NOTE: To test your own image, upload it to Colab and update the path above. 
# Example: img_path = '/content/your_image_name.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError(f"Image not found at the specified path: {img_path}")

# 3. Run inference to detect line segments
inputs = {'image': torch.tensor(img, dtype=torch.float32, device=device)[None, None] / 255.}
with torch.no_grad():
    out = net(inputs)

# 4. Plot and display results
lines = out['lines'][0]
plt.figure(figsize=(10, 10))

# Read and display the original image in RGB format
img_rgb = cv2.imread(img_path)[:,:,::-1]
plt.imshow(img_rgb)

# Draw line segments by restructuring the coordinate indices
for line in lines:
    # Coordinate swap experiment: element 0 as X and element 1 as Y
    x1, y1 = line[0, 0], line[0, 1]
    x2, y2 = line[1, 0], line[1, 1]

    # Plot using Matplotlib
    plt.plot([x1, x2], [y1, y2], color='red', linewidth=2)

plt.axis('off')
plt.title(f"DeepLSD detected {len(lines)} line segments (Restructured coordinates)")
plt.show()