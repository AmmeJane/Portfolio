class_name RandomGenMaze
extends Node3D

@onready var MapOfGrids : GridMap = $GridMap

@export var StartGen : bool = false : set = SetStart
@export var BorderSize : int = 20 : set = SetBorderSize

func SetStart(val:bool):
	generate()
	
func SetBorderSize(val : int):
	BorderSize = val
	if Engine.is_editor_hint():
		VisualiseBoarder()
	
func VisualiseBoarder():
	MapOfGrids.clear()
	for i in range(-1, BorderSize+1):
		#center is top left corner
		MapOfGrids.set_cell_item(Vector3i(i,0,-1),1) #top
		MapOfGrids.set_cell_item(Vector3i(i,0,BorderSize),1) #bottom
		MapOfGrids.set_cell_item(Vector3i(BorderSize,0,i),1) #right
		MapOfGrids.set_cell_item(Vector3i(-1,0,i),1) #left
		
	for i in range(0, BorderSize):
		for j in range(0, BorderSize):
			if i % 2 == 1:
				MapOfGrids.set_cell_item(Vector3i(i,0,j),0)
			elif i % 2 == 0 and j % 2 == 1:
				MapOfGrids.set_cell_item(Vector3i(i,0,j),0)

func generate():
	pass
