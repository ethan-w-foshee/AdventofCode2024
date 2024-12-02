[Advent of Code](https://adventofcode.com/) is a yearly challenge where everyday, for 25 days, you are giving a task, or puzzle to solve using whatever language and methods you want.

For the year of 2024, I decided to challenge myself in using a coding language I have not used in years: Python.

In this readme, I will be covering how I tackled the different challenges.
### I will be assuming that you know what the challenge is for each individual day. Also, spoilers ahead.
[Day 1](#day1)

<a name="day1"></a>
# Day 1:
## Part 1
The main challenge I ran into was forgetting how to manuver through Python. Once stuff started to click, and translate over from JavaScript, I looked up a few things, and did some brainstorming. 
<Details>
  <Summary>Part 1 Solution</Summary>
  To put the entire list in a text file, open that file up and read it line by line in a for loop. Each line, I would grab the first 5   characters, and store that in it's own list, then grab the last 5 characters, and store that in a separate list. Once that was done, I ran the basic `.sort` function, that is built into Python, on both of the lists.

  Next was to run another loop, this time, iterating through my first list of numbers. I took the index and got the respective number in the second list. I took the absolute value of the difference of numbers, and added that difference into a total sum. That ended day 1, part 1!
</Details>

## Part 2
<Details>
  <Summary>Part 2 Solution</Summary>
  The second part was a lot easier. My solution was just having a nested for loop that would compare the first number in my first list to every number in the second list, then move on. As it went through, if it had the correct number, it would add to a counter, then after each completion of the second list, multiply that counter by the first number. Once again, at the end, add all of the numbers together, and that gave me my solution!
</Details>
