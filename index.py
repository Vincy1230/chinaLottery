import random as rd


def welfare_double_color_ball() -> None:
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    red_ball = rd.sample(red_balls, 6)
    red_ball.sort()
    red_ball = [f"{i:02d}" for i in red_ball]
    blue_ball = rd.choice(blue_balls)
    blue_ball = f"{blue_ball:02d}"
    print(f"{' '.join(red_ball)} - {blue_ball}")


def welfare_3d_lottery(group: bool = False) -> None:
    balls = [i for i in range(0, 10)]
    lottery = [rd.choice(balls) for _ in range(3)]
    if group:
        if len(set(lottery)) == 1:
            welfare_3d_lottery(group=True)
            return
        lottery.sort()
        print(f"{' + '.join(map(str, lottery))}")
    else:
        print(f"{'   '.join(map(str, lottery))}")


def welfare_happy_8(choose: int | None = None) -> None:
    if choose is None:
        choose = rd.randint(1, 10)
    assert 1 <= choose <= 10, "Invalid choose"
    balls = [i for i in range(1, 81)]
    lottery = rd.sample(balls, choose)
    lottery.sort()
    lottery = [f"{i:02d}" for i in lottery]
    print(f"选{choose:>2} : {' '.join(map(str, lottery))}")


def welfare_seven_joy_lottery() -> None:
    balls = [i for i in range(1, 31)]
    lottery = rd.sample(balls, 7)
    red_ball = lottery[:6]
    red_ball.sort()
    red_ball = [f"{i:02d}" for i in red_ball]
    blue_ball = lottery[-1]
    blue_ball = f"{blue_ball:02d}"
    print(f"{' '.join(red_ball)} - {blue_ball}")


def sports_super_lotto() -> None:
    red_balls = [i for i in range(1, 36)]
    blue_balls = [i for i in range(1, 13)]
    red_ball = rd.sample(red_balls, 5)
    red_ball.sort()
    red_ball = [f"{i:02d}" for i in red_ball]
    blue_ball = rd.sample(blue_balls, 2)
    blue_ball.sort()
    blue_ball = [f"{i:02d}" for i in blue_ball]
    print(f"{' '.join(red_ball)} - {' '.join(blue_ball)}")


def sports_pick_3(group: bool = False) -> None:
    balls = [i for i in range(0, 10)]
    lottery = [rd.choice(balls) for _ in range(3)]
    if group:
        if len(set(lottery)) == 1:
            sports_pick_3(group=True)
            return
        lottery.sort()
        print(f"{' + '.join(map(str, lottery))}")
    else:
        print(f"{'   '.join(map(str, lottery))}")


def sports_pick_5() -> None:
    balls = [i for i in range(0, 10)]
    lottery = [rd.choice(balls) for _ in range(5)]
    print(f"{'   '.join(map(str, lottery))}")


def seven_star_lottery() -> None:
    red_balls = [i for i in range(0, 10)]
    blue_balls = [i for i in range(0, 15)]
    red_ball = [rd.choice(red_balls) for _ in range(6)]
    red_ball = [f"{i}" for i in red_ball]
    blue_ball = rd.choice(blue_balls)
    blue_ball = f"{blue_ball:02d}"
    print(f"{'  '.join(red_ball)}  -  {blue_ball}")


if __name__ == "__main__":
    welfare_double_color_ball()
    welfare_3d_lottery()
    welfare_happy_8()
    welfare_seven_joy_lottery()
    sports_super_lotto()
    sports_pick_3()
    sports_pick_5()
    seven_star_lottery()
