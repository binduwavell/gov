#How to vote for the Board elections

Here is a description about how the vote is made for the elections of the Board.

- Each vote is composed by a list of 5 candidates ordered by priority. Note that
  5 is the size of the board, according to the by-laws.

- No candidate must be listed twice in a single vote.

- Omissions are allowed.

#Closing the elections

Once the voting period is closed, candidates are sorted by two parameters in
this order:

- Number of votes

- Arithmetic mean of priority

The first 5 members are elected as the Board.

#Draws

The only important draw occurs when the Board cannot be determined. For
instance, when there is a draw between the 5th and the 6th position. In such
case, a new election needs to be run as tie-break where votes will be emitted
only for those candidates drawing.

#Example

Here is an example of an election with only 2 votes.

*Vote 1*

1. Zaphod Beeblebrox
2. Arthur Dent
3. Trillian
4. Ford Prefect
5. Marvin

*Vote 2*

1. Arthur Dent
2. Trillian
3. Slartibartfast
4. Ford Prefect
5. Zaphod Beeblebrox

That gives us the following ranking ordered by number of votes, and then by
average priority:

R = Ranking
V = Number of votes
P = Arithmetic mean priority

<pre>
R  V   P   Candidate
-  -  ---  -------------------
1  2  1.5  Arthur Dent
2  2  2.5  Trillian
3  2  3.0  Zaphod Beeblebrox
4  2  4.0  Ford Prefect 
5  1  3.0  Slartibartfast
6  1  5.0  Marvin
</pre>

Which means that Marvin is out of the Board. He has the same amount of votes as
Slartibartfast, but Slartibartfast has a better average priority. Marvin, the
paranoid android, probably does not even care. You know, brain the size of a
planet and they ask him to be in a Board.
