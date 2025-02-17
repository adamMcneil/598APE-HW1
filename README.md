# Peer Review Instructions
I run Ubuntu on my laptop, so I did all of the development on my personal computer.
You should be able to clone the repo on the campus machines to run the bash commands to run and compile the code.
To help you understand my optimization I made a git branch for each section in the paper.
Each section in the paper groups optimizations to the specific function or idea.
The following command will help you see the changes between your current branch and the target branch.
```bash
git diff <git-branch>
```
In the following list, the numbers are the section of the paper and the corresponding git branch to the place where those optimizations were made.
- 1 -> start
- 2 -> getLight
- 3 -> calcColor
- 4 -> getIntersection
- 5 -> solveScalers
- 6 -> calcColor2
- 7 -> macros
- 8 -> main

The testing process that I followed was pretty simple.
We used the following command to test the execution time of the program.
```bash
./main.exe -i inputs/pianoroom.ray --ppm -o output/pianoroom.ppm -H 500 -W 500
```
We would just average three runs of the program and plot that on a graph to compare execution times.
I created some make targets to help in that process but are not needed.
To verify the optimizations you could do through the branches run the program comparing execution time.
![first](https://github.com/user-attachments/assets/000ee285-125b-4878-8127-a6ab1ac63d85)
![macros](https://github.com/user-attachments/assets/2dfd1166-19af-4307-a542-2104447fab50)
