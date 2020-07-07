import json
import math


class Agent:
	def __init__(self,position, **agent_attributes):
		self.position = position
		for attr_name, attr_value in agent_attributes.itesm():
			setatt(self,attr_name,attr_value)

class Position:
	def __init__(self,longitude_degrees, latitude_degrees):
		self.latitude_degrees = latitude_degrees
		self.longitude_degrees = longitude_degrees

	@property
	def longitude(self):
		return self.longitude_degrees * math.pi /180

class Zone:

	ZONES = []
	MIN_LONGITUDE_DEGREES = -180
	MAX_LONGITUDE_DEGREES = 180
	MIN_LATITUDE_DEGREES = -90
	MAX_LATITUDE_DEGREES = 90
	WIDTH_DEGREES = 1
	HEIGHT_DEGREES = 1

	def __init__(self,corner1, corner2):
		self.corner1 = corner1
		self.coner2 = corner2
		self.inhabitants = 0


#	@classmethod
#	def initialize_zone(self):
#		for latitude in range(self.MIN_LATITUDE_DEGREES,self.MAX_LATITUDE_DEGREES ):
#			for longitude in range(self,MIN_LONGITUDE_DEGREES,self.MAX_LONGITUDE_DEGREES, WIDTH_DEGREES):
#				bottom_left_corner = Position(longitude, latitude)
#				top_right_corner = Position(longitude + self.WIDTH_DEGREES, latitude + self.HEIGHT_DEGREES)
#				self.ZONES.append(zone)
#		print(len(cls.ZONES))


print(Zone.MIN_LONGITUDE_DEGREES)


zone.initialize_zones()




#def main()
#	for