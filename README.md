![logo](https://raw.githubusercontent.com/hh-Naram/Prism/master/Branding/Logo.png)

Designed to take an image as an input and outputs mathematical expressions, specifically bezier curves. It uses OpenCV edge detection. The main purpose of Prism is to create art with nothing but pure maths. I know a lot of people have done this and it's not a unique idea, but this is mainly for me to practice coding in my python, a language which I am not that fond of, and also cause I feel like it.

## Usage

```sh
$ gh repo clone hh-Naram/Prism && cd Prism
$ pip3 install -r requirements.txt
$ python3 Prism.py
```

## Features
Detect edges in any image with custom thresholds and output data in several formats including: `Desmos expressions`, `Latex` and `SVG`.

## References
- [Wiki: Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [Wiki: Potrace](https://en.wikipedia.org/wiki/potrace)
- [Wiki: Canny Edge Detection](https://en.wikipedia.org/wiki/Canny_edge_detector)
- [Computational approach to edge detection](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.
