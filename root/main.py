
from utils import generate_secret_number, check_user_guess
from score import lose_points , rank_score
secret_number = generate_secret_number()
score = 100

while True:
    if check_user_guess(secret_number):
        break
    else:
        score = lose_points(score)

rank_score(score)
print(rank_score(score))
print(score)