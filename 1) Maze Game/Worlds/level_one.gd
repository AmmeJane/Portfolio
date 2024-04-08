#This script knows when the player finds the goal and sends a signal when the goal is touched.

extends Node3D

signal LevelCompleted

func _on_goal_body_entered(body):
	if body is Player:
		emit_signal("LevelCompleted")
