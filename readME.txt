Cody Brown, 02 Dec 2022
Mug Project
CPSC 207

For stage 1, I created attributes that consisted of most of the characteristics
for a mug, such as height, radius, material, handle, color, shape, empty weight, thickness,
and capacity. The only attribute I used in stage two was capacity (mug.capacity).

For stage 2, I wanted the user to input how many cups of tea they drank in order to
simulate them "drinking" tea. I assigned the input function to 'x' so that I could use
it later in my defined function. I used the time module from the Word Game Project to
inform the user on the scenario (a mug with 4 cups of tea), and the used an int(input())
function so that what the user inputted would be an integer instead of a string. Since the
mug is not infinitely large, I set the capacity to 4 cups, which was an attribute earlier.
In my tea_drinking_simulation function, I made an if statement so that it would
only calculate how many cups were left in the mug if they drank less than or equal
to the capacity, and could not be negative. Otherwise, it would not have made sense.
So, I included the else statement to call out the user on not being able to drink more
then what was in the cup or a negative number of cups.

Note: You might notice an f' string in the function. With only the string as
'There are', tea_remaining, 'cups left', I was printing ('There are', tea_remaining, 'cups left')
which was ugly. I googled how to fix this and saw the f' string, which I also
recognized from the Word Game Project. I decided to try it, and it worked.
