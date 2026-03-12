controls: up key, down key, right key, left key

instead of storing the snake as a list of coordinates and shifting them each frame each tail segment is its own object with a reference to the next segment like a linked list when the snake moves the head passes its old position down the chain recursively, so each segment follows the one ahead of it naturally
adding a new segment is just calling new tail to the head and it will pass down until it finds the end appending new tail object there
