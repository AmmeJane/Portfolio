#This script makes a menu when it is called from the game script. 
#It emits a signal when try again is pressed and also quits when leave is pressed

extends Control

signal TryAgain
signal NextLevel

@onready var TheTime : = $CenterContainer/Column/Time
@onready var TheTitle : = $CenterContainer/Column/Title


func initialise(TotalPlayTime : float):
	Input.mouse_mode = Input.MOUSE_MODE_VISIBLE
	if TotalPlayTime != 0:
		var Minutes : String = str(int(TotalPlayTime / 60))
		var Seconds : String = str(int(fmod(TotalPlayTime, 60)))
		var TimeText = "Your time was %s minutes and %s seconds." % [Minutes, Seconds]
		TheTime.text = TimeText
	else:
		var TitleText = "You failed"
		TheTitle.text = TitleText
		var TimeText = "You pressed Escape"
		TheTime.text = TimeText
	
	show()
	
func _on_next_level_pressed():
	emit_signal("NextLevel")

func _on_try_again_pressed():
	emit_signal("TryAgain")


func _on_main_menu_pressed():
	get_tree().quit()


