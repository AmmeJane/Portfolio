@tool
extends Node3D

@onready var MapOfGrids : GridMap = $GridMap

@export var BorderSize : int = 20 : set = SetBorderSize
@export var hey : bool = false : set = hellothere

	
func SetBorderSize(val : int):
	print("hey")
	BorderSize = val
	if Engine.is_editor_hint():
		print("hey", MapOfGrids)
		MapOfGrids.clear()
		print("hey")
		for i in range(-1, BorderSize+1):
			print("hey")
			MapOfGrids.set_cell_item(Vector3i(i,0,-1),1) #top
			
func hellothere(val : bool):
	print("hey")
		
