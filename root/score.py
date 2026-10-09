def lose_points(points):
    new_score = points - 10
    if points <= 0:
        return 0
    return new_score
def rank_score(points):
    if points >= 80:
        return "Excellent"
    elif points >= 50:
        return "Good"
    elif points >= 0:
        return "Keep Practicing"

if __name__ == "__main__":
    points = 100
    print(lose_points(points))