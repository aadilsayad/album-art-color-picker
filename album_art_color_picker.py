import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from collections import Counter
import colorsys

def extract_colors(image_path, num_colors=100):
    with Image.open(image_path) as img:
        img = img.convert('RGB')
        np_img = np.array(img)
        pixels = np_img.reshape(-1, 3)
        
    kmeans = KMeans(n_clusters=num_colors, random_state=42)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_
    colors = np.round(colors).astype(int)
    
    labels = kmeans.labels_
    color_counts = Counter(labels)
    
    sorted_colors = sorted([(tuple(color), color_counts[i]) for i, color in enumerate(colors)], 
                           key=lambda x: x[1], reverse=True)
    
    return sorted_colors

def calculate_contrast(color1, color2):
    # Convert to HSV for better contrast comparison
    hsv1 = colorsys.rgb_to_hsv(*[x/255.0 for x in color1[:3]])
    hsv2 = colorsys.rgb_to_hsv(*[x/255.0 for x in color2[:3]])
    
    # Calculate differences in hue, saturation, and value
    hue_diff = min(abs(hsv1[0] - hsv2[0]), 1 - abs(hsv1[0] - hsv2[0]))
    sat_diff = abs(hsv1[1] - hsv2[1])
    val_diff = abs(hsv1[2] - hsv2[2])
    
    # Weighted sum of differences (you can adjust weights if needed)
    return hue_diff * 0.5 + sat_diff * 0.25 + val_diff * 0.25

def select_colors(sorted_colors):
    dominant_color = sorted_colors[0][0]
    
    # Find the color with highest contrast among top 20
    contrast_color = max(sorted_colors[1:20], key=lambda x: calculate_contrast(dominant_color, x[0]))
    
    return dominant_color, contrast_color[0]

def main(image_path):
    sorted_colors = extract_colors(image_path)
    dominant, contrast = select_colors(sorted_colors)
    
    print(f"Dominant color: RGBA{dominant}")
    print(f"Contrasting color: RGBA{contrast}")
    
    print("\nTop 20 colors:")
    for i, (color, count) in enumerate(sorted_colors[:20], 1):
        print(f"{i}. RGBA{color} (Count: {count})")

if __name__ == "__main__":
    image_path = "path/to/image.png"
    main(image_path)