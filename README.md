# Final State Machine of a Dog Race

This program simulates a simple dog race with a Finite State Machine (FSM) to control the dog's movement.

## States:

start: The initial state where the dog is at the starting line.

State start: "Dog at start"<br>
Actions: The dog is positioned at the starting line, waiting for user input to begin the race.<br>
moving: The state where the dog is running towards the finish line.

State running: "Dog running..."<br>
Actions: The dog moves forward at a constant pace until it reaches the finish line or is manually stopped by the user.<br>
stopped: The state where the dog is temporarily stopped during the race.

State stopped: "Dog stopped"<br>
Actions: The dog pauses its movement. The user can resume the race by starting the movement again.<br>
finish: The state where the dog has completed the race and reached the finish line.

State finished: "Dog finished the race!"<br>
Actions: Once the dog reaches the finish line, it stops moving, and this state is final unless the race is reset.

## Controls:

space: Starts or resumes the dog's movement.<br>
s: Stops the dog's movement.<br>
e: Resets the dog to the starting position.<br>
