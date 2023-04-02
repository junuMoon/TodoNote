# Chapter 1. Vectors 

## Section 1-1. Vectors and Matrices

- D1: League of legend, (x-coordinate of mouse pointer, y-coordinate of mouse pointer, which skill was used) can be be described by vectors in R3?.
	- The League of Legends example you provided could be described using a vector in R3, but not in the way you described it. Here’s why:
	- A vector in R3 consists of three components that represent a point or a direction in three-dimensional space. In the context of League of Legends, we could use a vector in R3 to describe the position of a champion on the map, or the direction in which a projectile is traveling.
	- However, the example you provided involves three pieces of information: the x-coordinate of the mouse pointer, the y-coordinate of the mouse pointer, and which skill was used. This is not a three-dimensional vector, but rather a three-tuple (or triple) of values.
	- To represent this information using vectors, we could assign each skill a unique vector in R3, and then use the x- and y-coordinates of the mouse pointer to define a point in two-dimensional space. We could then combine the skill vector and the mouse point vector to create a new vector in R3 that represents the skill being used at that particular point in the game.
- D2: Time can be expressed as both scaler and vector. **v**(date, hour, minute, …). Scaler: timestamps. And time can be said “5 minutes ago”
	- Your answer is partly correct. Time can be expressed as both a scalar and a vector, depending on the context and how it is being used.
	- When time is being used to represent a single point in time, such as a timestamp or a duration, it is considered a scalar quantity. For example, “10:30 AM” or “30 minutes” are scalar quantities of time.
	- On the other hand, when time is being used to represent a change or a displacement, such as the time it takes to travel from one location to another or the duration of a process, it can be represented as a vector quantity. For example, “2 hours east” or “30 minutes northwest” are vector quantities of time.
	- Your answer touches on some aspects of the time representation but could be improved for better clarity and accuracy.
	- Time is generally considered a scalar quantity rather than a vector. Scalars have only magnitude, while vectors have both magnitude and direction. In most physical applications, time is measured in units such as seconds, minutes, or hours and has no inherent direction associated with it. For example, when we say “5 minutes ago,” we refer to a duration, which is still a scalar quantity.
	- However, you mentioned representing time as a vector with components like date, hour, and minute. While it is possible to represent time-related information in this manner, it doesn’t make time itself a vector quantity. In this case, you are dealing with a structured data representation rather than the fundamental nature of time as a physical quantity.
	- So, in summary, time is generally considered a scalar quantity, with specific representations or data structures allowing for more complex descriptions of time-related information.
- D3. if the sum of three vectors in R^3 is zero, must they lie in the same plane? Explain.
	- A: x+y+z=0 -> y=-x-z. y should be expressed by combination of x and z. So that they must lie in the same plane
	- Your answer is on the right track, but it could be explained more clearly.
	- If the sum of three vectors in R^3 is zero, it means that vector x + vector y + vector z = 0. This can be re-written as vector y = - (vector x + vector z).
	- In this case, vector y is the negative sum of vectors x and z, meaning that it can be represented as a linear combination of vectors x and z. Since vector y can be expressed as a linear combination of the other two vectors, all three vectors must lie in the same plane.

## Section 1-2. Dot Product and Orthognoality