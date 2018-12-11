the Game class has two main methods
'run' - to play a single game
'run_loop' - which is used to play many games and save statistics to mongodb

show_stats.py shows saved data.

project now contains only two types of players - RandomPlayer that turns cards completly randomly
                                               - MemoryPlayer that has memory (dict like) of specified size