# This script runs the smurf.c code 

#!/bin/bash
gcc smurf.c -o smurf
./smurf $1 $2 $3 &


sleep 5
kill $!

sleep 3
