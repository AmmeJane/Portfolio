#this script links to the player and menu, initialises the menu when level one is completed,
#or when it gets a signal from player that escape was pressed, and can reload the scene from the menu signal

extends Node

var CurrentScene = "Level One"

@onready var EndMenu : = $EndMenu
@onready var Player : = $Player

var PlayTime = 0

func _process(delta):
	PlayTime += delta
	
func _on_level_one_level_completed():
	var TotalPlayTime = PlayTime
	Player.queue_free()
	EndMenu.initialise(TotalPlayTime)

func _on_end_menu_next_level():
	pass # Replace with function body.

func _on_end_menu_try_again():
	get_tree().reload_current_scene()
	
func _on_player_pause_menu():
	Player.queue_free()
	EndMenu.initialise(0)
	
func ChangeScene(val):
	if CurrentScene == "Level One":
		CurrentScene = val
	else:
		CurrentScene == "Level Two"

