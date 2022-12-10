from enum import Enum

class Plays(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def winner(move):
        """Next would win actual 'move'"""
        if move == Plays.ROCK:
            return Plays.PAPER
        elif move == Plays.PAPER:
            return Plays.SCISSORS    
        elif move == Plays.SCISSORS:
            return Plays.ROCK  # circular next

    @classmethod
    def get_play(cls, opponent, result):
        if result == Scores.DRAW:
            return opponent

        if result == Scores.WIN:
            return Plays.winner(opponent)
        
        return Plays.winner(Plays.winner(opponent))  # looser move


class Scores(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    @classmethod
    def get_score(cls, opponent, mine):
        if mine == opponent:
            return Scores.DRAW
        
        if Plays.winner(mine) == opponent:
            return Scores.LOSS

        return Scores.WIN


class Moves(Enum):
    A = Plays.ROCK
    B = Plays.PAPER
    C = Plays.SCISSORS
    X = Plays.ROCK
    Y = Plays.PAPER
    Z = Plays.SCISSORS


# PART 1
with open("2-input.txt") as f:
    score = 0
    for line in f.readlines():
        if not line.strip():
            break
        opponent, mine = line.split()
        opponent, mine = Moves[opponent], Moves[mine]
        result = Scores.get_score(opponent.value, mine.value)
        score += result.value + mine.value.value

print("[PART 1] Score:", score)

class Moves2(Enum):
    A = Plays.ROCK
    B = Plays.PAPER
    C = Plays.SCISSORS
    X = Scores.LOSS
    Y = Scores.DRAW
    Z = Scores.WIN

# PART 2
with open("2-input.txt") as f:
    score = 0
    for line in f.readlines():
        if not line.strip():
            break
        opponent, result = line.split()
        opponent, result = Moves2[opponent], Moves2[result]

        mine = Plays.get_play(opponent.value, result.value)
        # print(result.value.value, mine)
        score += result.value.value + mine.value

print("[PART 2] Score:", score)