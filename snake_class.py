from turtle import Turtle
import time

class Snake:
	def __init__(self):
		self.start_positions = [(0, 0), (-20, 0), (-40, 0)]
		self.turtles = []

	# Create segments
	######################################################

	def create_segments(self):
		for position in self.start_positions:
			self.add_segment(position)

	def add_segment(self, position):
		new_turt = Turtle("square")
		new_turt.penup()
		new_turt.color("white")
		new_turt.goto(position)
		self.turtles.append(new_turt)

	def extend(self):
		self.add_segment(self.turtles[-1].pos())


	# Control
	######################################################

	def left(self):
		if self.turtles[0].heading() != 0:
			self.turtles[0].setheading(180)

	def right(self):
		if self.turtles[0].heading() != 180:
			self.turtles[0].setheading(0)

	def up(self):
		if self.turtles[0].heading() != 270:
			self.turtles[0].setheading(90)

	def down(self):
		if self.turtles[0].heading() != 90:
			self.turtles[0].setheading(270)


	# Move action
	######################################################

	def move(self):
		for segment_nr in range(len(self.turtles) - 1, 0, -1):
			self.turtles[segment_nr].goto(self.turtles[segment_nr - 1].pos())
		self.turtles[0].forward(20)





