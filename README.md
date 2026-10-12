# Technical-Writing-Python-Circle

## Project Manager Statement

Please create `USER_GUIDE.md` for people who need to use `Circle` but are not
software engineers. Assume no Python knowledge. Explain essential terms and
provide clear instructions covering:

- Setup and creating `Circle(radius)`.
- `getRadius()`, `getDiameter()`, `getArea()`, and `getCircumference()`.
- Displaying results with `print(circleInstance)`.
- Measurement units, a worked example, and the known issue below.

Verify your instructions against the provided example.

## Project Files

- `circle.py` defines the `Circle` class.
- `example.py` demonstrates every method and prints the circle's details.
- `example_output.txt` contains the example's output.

## Run the Example

Use Python 3. No additional packages are required. From the project folder, run:

```sh
python3 example.py
```

## Known Issues

The constructor does not check that the radius is greater than zero. It accepts
zero and negative values. Users must supply a positive numeric radius.

Validation is planned but not implemented. Document the current behavior.
