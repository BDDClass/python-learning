from abc import ABC, abstractmethod
import math

PI = 3.1415926

class Shape(ABC):
	@abstractmethod
	def area(self): pass
	@abstractmethod
	def perimeter(self): pass
	def describe(self): return "This is a Shape."
	
	@staticmethod
	def validate_positive(value, name):
		if value < 0:
			print(f"{name} cannot be negative.")
			return False
		return True

class Circle(Shape):
	def __init__(self, radius):
		if not super().validate_positive(radius, "Circle"): raise ValueError("Radius must be positive.")
		self.radius = radius
	def area(self): return PI * self.radius ** 2
	def perimeter(self): return 2 * PI * self.radius

class Rectangle(Shape):
	def __init__(self, width, height):
		if not super().validate_positive(width, "Rectangle"): raise ValueError("Width must be positive.")
		if not super().validate_positive(height, "Rectangle"): raise ValueError("Height must be positive.")
		self.width = width
		self.height = height
	def area(self): return self.width * self.height
	def perimeter(self): return 2 * (self.width + self.height)

class Triangle(Shape):
	def __init__(self, side1, side2, side3):
		for side in [side1, side2, side3]:
			if not super().validate_positive(side, "Triangle"):
				raise ValueError("All sides must be positive.")
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
	def area(self):
		s = (self.side1 + self.side2 + self.side3) / 2
		return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
	def perimeter(self): return self.side1 + self.side2 + self.side3

class ShapeCollection:
	def __init__(self):
		self.shapes = []
	def add_shape(self, shape):
		self.shapes.append(shape)
	def total_area(self):
		total = 0
		for sp in self.shapes: total += sp.area()
		return total
	def total_perimeter(self):
		total = 0
		for sp in self.shapes: total += sp.perimeter()
		return total

# Test your code
if __name__ == "__main__":
	# Create shapes
	circle = Circle(5)
	rectangle = Rectangle(4, 6)
	triangle = Triangle(3, 4, 5)
	# Test individual shapes
	print("Individual Shapes:")
	for shape in [circle, rectangle, triangle]:
		print(f" {shape.describe()}")
		print(f" Area: {shape.area():.2f}")
		print(f" Perimeter: {shape.perimeter():.2f}")
	# Test collection (polymorphism!)
	collection = ShapeCollection()
	collection.add_shape(circle)
	collection.add_shape(rectangle)
	collection.add_shape(triangle)
	print(f"\nCollection Totals:")
	print(f" Total Area: {collection.total_area():.2f}")
	print(f" Total Perimeter: {collection.total_perimeter():.2f}")
	# Test validation
	print("\nTesting validation:")
	try: bad_circle = Circle(-5)
	except: print("Correctly rejected negative radius")