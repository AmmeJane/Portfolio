@tool
extends Node3D

@onready var MapOfGrids : GridMap = $GridMap

@export var StartGen : bool = false : set = SetStart
@export var BorderSize : int = 15 : set = SetBorderSize

func SetStart(val:bool):
	VisualiseBoarder()
	generate()
	
func SetBorderSize(val : int):
#	if val % 2 == 0:
#		val+=1
	BorderSize = val
	if Engine.is_editor_hint():
		VisualiseBoarder()
	
func VisualiseBoarder():
	MapOfGrids.clear()
	
	MakeSquare()
	MakeGrid()
	
func MakeSquare():
	for i in range(-1, BorderSize+1):
		#center is top left corner
		MapOfGrids.set_cell_item(Vector3i(i,0,-1),1) #top
		MapOfGrids.set_cell_item(Vector3i(i,0,BorderSize),1) #bottom
		MapOfGrids.set_cell_item(Vector3i(BorderSize,0,i),1) #right
		MapOfGrids.set_cell_item(Vector3i(-1,0,i),1) #left
func MakeGrid():
	for i in range(0, BorderSize):
		for j in range(0, BorderSize):
			if i % 2 == 1:
				MapOfGrids.set_cell_item(Vector3i(i,0,j),0)
			elif i % 2 == 0 and j % 2 == 1:
				MapOfGrids.set_cell_item(Vector3i(i,0,j),0)

func GenerateMaze():
	pass

func GetBlanks():
	var SpaceTable = []
	for i in range(0, BorderSize):
		for j in range(0, BorderSize):
			if MapOfGrids.get_cell_item(Vector3(i,0,j)) == -1:
				print(MapOfGrids.get_cell_item(Vector3(i,0,j)))
				SpaceTable.append(Vector3(i,0,j))
	return SpaceTable
	print("word",SpaceTable)

func generate():
	var StartingPoint = Vector3(0,0,0)
	var SpaceTable = GetBlanks()
	var CurrentPoint = StartingPoint
	var Go = true
	
	while Go:
		if GetBlanks().size() > 0:
			CurrentPoint = CheckWalls(CurrentPoint)
			if CurrentPoint in SpaceTable:
				for thing in SpaceTable:
					if thing == CurrentPoint:
						SpaceTable.remove(thing)
			else:
				print("error", SpaceTable)
		else:
			print("done",SpaceTable)
			Go = false

func CheckForGiven(val, BlockType, DirectionArray):
	for i in DirectionArray:
		if MapOfGrids.get_cell_item(val-i) == BlockType:
			MapOfGrids.set_cell_item(val-i,2)
			return val-i
func CheckWalls(val:Vector3):
	var DirectionArray = [Vector3(1,0,0),Vector3(-1,0,0),Vector3(0,0,1),Vector3(0,0,-1)]
	DirectionArray.shuffle()
	MapOfGrids.set_cell_item(val,2)
	CheckForGiven(val, -1, DirectionArray)
	CheckForGiven(val, 0, DirectionArray)
	
	
