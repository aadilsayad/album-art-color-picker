# Spotify-like Color Extractor

This tool emulates the color selection behavior of the Spotify app, where two colors are extracted from an album's artwork. These colors are typically used for enhancing user interface elements such as the lyrics viewer's background and the player notification's background and text color.

## Features

- Extracts the most dominant color from an image
- Selects a contrasting color that is also prominent in the image
- Provides a list of the top 20 colors present in the image

## How It Works

The color extraction process involves several steps:

1. **Image Processing**: The image is opened and converted to RGB format using the Pillow library.

2. **Color Quantization**: The KMeans algorithm from scikit-learn is used to cluster the image pixels into a specified number of colors (default is 100).

3. **Color Sorting**: Colors are sorted based on their frequency in the image.

4. **Dominant Color Selection**: The most frequent color is selected as the dominant color.

5. **Contrast Color Selection**: A contrasting color is chosen from the top 20 most frequent colors. This selection is based on a custom contrast calculation that considers differences in hue, saturation, and value in the HSV color space.

## Dependencies

- numpy
- Pillow (PIL)
- scikit-learn
- collections (from Python standard library)
- colorsys (from Python standard library)

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/spotify-color-extractor.git
   ```

2. Install the required dependencies:
   ```
   pip install numpy Pillow scikit-learn
   ```

3. Run the script:
   ```python
   python color_extractor.py
   ```

   Note: Make sure to replace `"path/to/image.png"` in the `main()` function with the path to your image file.

## Output

The script will print:
- The dominant color (RGBA)
- A contrasting color (RGBA)
- A list of the top 20 colors in the image, along with their frequency counts

## Contributing

Contributions to improve the color extraction algorithm or add new features are welcome. Please feel free to submit a pull request or open an issue to discuss potential changes.

## License

[MIT License](LICENSE)

## Acknowledgments

This project was inspired by the color selection mechanism used in the Spotify app for enhancing user interface elements.
