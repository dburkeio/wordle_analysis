# wordle_analysis

## solver.py 
solver.py is a program to generate a Wordle answer by providing your guesses and the positions of gray, yellow, and green spaces.

## analysis1.py
analysis1.py is a program to search through all possible Wordle words and generate the top 10 best starting words. Here they are

1. [3.2786177105831533, 'soare']
2. [3.114902807775378, 'saine']
3. [3.08207343412527, 'slane']
4. [3.067818574514039, 'roate']
5. [3.0466522678185743, 'saice']
6. [3.038876889848812, 'salet']
7. [3.033693304535637, 'raile']
8. [3.002159827213823, 'orate']
9. [2.9935205183585314, 'saree']
10. [2.988768898488121, 'raine']

Wordle uses a different word list for valid guesses and possible secret words. The word scores were calculated by comparing every word combination between the valid word list and possible secret words. 

Gray letters (letter is not in the word) were assigned 0 points, yellow letters (letter is in the word but in the wrong place) were assigned 1 point, green letters (letter is in the word and in the right place) were assigned 2 points. The points are summed for each comparison and an average score is calcuated for each word.
