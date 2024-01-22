# This is a simplified example and may require adjustments based on the specific details of your FreeCAD version and your project setup.

# Create a new document or access the existing one
import FreeCAD, FreeCADGui

doc = FreeCAD.newDocument("HolesDocument")

# Define the hole parameters
hole_diameter = 3  # Example diameter

# Your coordinates list (replace with your actual coordinates)
coordinates_list_mils = [
    (-3228.00, -3359.00),
    (1515.00, -4064.00),
    (1172.00, -263.00),
    (-3228.00, 461.00),
    (-4166.00, -3695.00),
    (5265.00, 3387.50),
    (5265.00, -4512.50),
    (-635.00, 825.00),
    (-4360.00, -4512.50),
    (-4260.00, -62.50),
    (-4360.00, 3387.50),
    (-4160.00, -435.00),
    (-3995.00, 3350.00),
    (-335.00, 825.00),
    (4980.00, -4460.00),
    (5215.00, 3105.00),
]
coordinates_list_mm = [(x * 0.0254, y * 0.0254) for x, y in coordinates_list_mils]
for coordinates in coordinates_list_mm:
    App.getDocument('devkit_mount').getObject('Sketch003').addGeometry(Part.Circle(App.Vector(coordinates[0],coordinates[1],0),App.Vector(0,0,1),hole_diameter/2),False)


App.getDocument('devkit_mount').getObject('Sketch003').addGeometry(Part.Circle(App.Vector(-255.490097,-106.660263,0),App.Vector(0,0,1),2.439344),False)
