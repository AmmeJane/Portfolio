#This script controls player movement and any key presses the player makes, like pressing escape for the menu

extends CharacterBody3D

class_name Player

signal PauseMenu

@export var MoveSpeed : float = 10
@export var Sensitivity : float = 0.005

@onready var Camera : = $Camera3D
@onready var Ray : = $Camera3D/RayCast3D
var RayOrigin = Vector3()
var RayEnd = Vector3()

func _ready():
	Input.mouse_mode = Input.MOUSE_MODE_CAPTURED
	
func _unhandled_input(event):
	#moves the camera based on mouse position and clamps it so it cant look up or down infinitely/behind the character
	if event is InputEventMouseMotion:
		rotate_y(event.relative.x*-Sensitivity)
		Camera.rotate_x(event.relative.y*-Sensitivity)
		Camera.rotation_degrees.x = clamp(Camera.rotation_degrees.x,-70,90)

func _physics_process(delta):
	
	#click events
	if Input.is_action_pressed("PauseMenu"):
		emit_signal("PauseMenu")
		
	var MovingUD : float = Input.get_action_strength("Backwards") - Input.get_action_strength("Forward")
	var MovingLR : float = Input.get_action_strength("Right") - Input.get_action_strength("Left")
	
	var DirectionUD : Vector3 = Vector3(0,0,1).rotated(Vector3(0,1,0), rotation.y)
	var MotionUD : Vector3 = DirectionUD * MovingUD * MoveSpeed
	
	var DirectionLR : Vector3 = Vector3(1,0,0).rotated(Vector3(0,1,0), rotation.y)
	var MotionLR : Vector3 = DirectionLR * MovingLR * MoveSpeed
	
	velocity = MotionUD + MotionLR
	move_and_slide()

	

	
