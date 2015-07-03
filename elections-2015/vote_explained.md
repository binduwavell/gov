#Votes Explained

Voting was done by email as explained in voting-mechanism-2015.md.
Each vote was put into a plain text file with the following format:

- First 5 lines represent the vote ordered by priority.

- After a blank line, we added a random hexadecimal chain of 42 characters to
  differentiate two identical votes. The chain was generated with the apg tool,
version 2.2.3, using the following parameters:

    apg -a 1 -M nl -n 1 -m 42 -x 42 -c cl_seed -E ghijklmnopqrstuvwxyz

Once the vote was made unique, we computed the MD5 check sum, using md5sum,
version 8.21, and rename the file with its checksum. The value was sent to the
voting member so that it could identify its vote in the folder 'votes'. The
checksum was sent only to the voting member.

More about that procedure can be seen at the script 'register_vote.sh'.

Votes can be counted manually, but you can also use the script
'count_votes.py'.
