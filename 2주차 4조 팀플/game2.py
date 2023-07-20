import random
name = "한솔"
players = ["영진", "한솔", "지현", "성민"]
def game2(players, name):
    tagger = "영진"
    num = len(players)

    # intro
    print("""
    □□□■■■■■■■■■□□□□■■□□□□■□□□□□□□□□□□□□■□■□□■■■■■■□□□■□
    □□□□□□■■■□□□□□■■■■■■□□■□□□□□□■■■■■□□■□■□□■■□□■■□□□■□
    □□□□■■■■■■■□□□■■□□■■□□■□□□□□□□□□□■□□■□■□□■□□□□■□□□■□
    □□■■■■□■□■■■□□■□□□□■□□■□□□□□□□□□■■□□■□■□□■□□□□■□□□■□
    □□□□□□□■□□□□□□■□□□□■□□■■■■□□□□□□■■■■■□■□□■■□□■■□□□■□
    □■■■■■■■■■■■■□■□□□□■□□■■■■□□□□□□■■■■■□■□□■■■■■■□□□■□
    □□□□□□□■□□□□□□■□□□□■□□■□□□□□□□□■■□□□■□■□□□□□□□□□□□■□
    □□□■■■■■■■■■□□■■□□■■□□■□□□□□□□■■■□□□■□■□□□□■■■■■■■■□
    □□□□□■■■■■□□□□■■■■■■□□■□□□□□□■■□□□□□■□■□□□□■□□□□□□■□
    □□□□■■■■■■■□□□□□□□□□□□■□□□□□□■□□□□□□■□■□□□□■□□□□□□■□
    □□□□■■□□□■■□□□□□□□□□□□■□□□□□□□□□□□□□■□■□□□□■□□□□□□■□
    □□□□■■■■■■■□□□□□□□□□□□■□□□□□□□□□□□□□■□■□□□□■■■■■■■■□""")

    #start
    refusal = 0
    lovegame_start(players, tagger, refusal, name)


def lovegame_start(players, tagger, refusal, name):
    print()
    # 컴퓨터가 플레이 하는 지 내가 하는 지 결정, 내가 선택되었는지
    my_turn = False
    selected = False
    text = name + " : "
    if tagger == name:
        my_turn = True

    # tagger가 술래
    # tagger를 제외한 나머지 사람 리스트
    others = [x for x in players if x != tagger]
    # 지목할 사람 선정
    if my_turn:
        
        next_tagger = input(text)
        next_tagger = next_tagger[:2]
    else:
        next_tagger = others[random.randint(0, len(others)-1)]
        if next_tagger == name:
            selected = True
        print(tagger, ":", next_tagger, "좋아!")
    # 지목 당한 사람의 결정. (나도 좋아(25%) 얼만큼(25%) 나는 싫어(25%) 칵 퉤(25%))
    if selected:
        answer = input(text)
        if "좋아" in answer:
            lovegame_start(players, next_tagger, 0, name)
        elif "얼만큼" in answer:
            how_much(tagger, next_tagger, name, 0, refusal)
            print()
        elif "싫어" in answer:
            print(tagger, ": 그럼 누구?")
            lovegame_start(players, next_tagger, 0, name)
        else:
            refusal += 1
            if refusal == 3:
                return tagger
            lovegame_start(players, tagger, refusal, name)

    else:
        decision = random.randint(1, 4)
        if decision == 1:
            print(next_tagger, ": 나도 좋아!")
            lovegame_start(players, next_tagger, 0, name)
        elif decision == 2:
            print(next_tagger, ": 얼만큼?")
            how_much(tagger, next_tagger, name, 0, refusal)
        elif decision == 3:
            print(next_tagger, ": 나는 싫어")
            print(tagger, ": 그럼 누구?")
            lovegame_start(players, next_tagger, 0, name)
        else:
            print(next_tagger, ": 칵 퉤")
            refusal += 1
            if refusal == 3:
                return tagger
            lovegame_start(players, tagger, refusal, name)


def how_much(tagger, next_tagger, name, lack, refusal):
    text = name + " : "
    #얼만큼 좋아하는지
    if tagger == name: #내가 물어본사람이면
        degree_of_love = input(text)
    else:
        if lack == 0:
            degree_of_love = "😌"
        elif lack == 1:
            degree_of_love = "😘"
        elif lack == 2:
            degree_of_love = "😍"
        elif lack >= 3:
            degree_of_love = "🥰" * (lack-2)

        print(f"{degree_of_love}요만큼!")
    #만족스러운지
    if next_tagger == name: #내가 판단하는 사람이면
        answer = input(text)
        if "좋아" in answer:
            lovegame_start(players, next_tagger, 0, name)
        elif "부족" in answer:
            how_much(tagger, next_tagger, name, lack+1, refusal)
        elif "싫어" in answer:
            print(tagger, ": 그럼 누구?")
            lovegame_start(players, next_tagger, 0, name)
        else: #칵 퉤
            refusal += 1
            if refusal == 3:
                return tagger
            lovegame_start(players, tagger, refusal, name)
    else:
        decision = random.randint(1, 10) #나도 좋아(20%) 부족해(50%) 나는 싫어(10%) 칵퉤(20%)
        if decision <= 2:
            print(next_tagger, ": 나도 좋아!")
            lovegame_start(players, next_tagger, 0, name)
        elif decision <= 7:
            print(next_tagger, ": 부족해")
            how_much(tagger, next_tagger, name, lack+1, refusal)
        elif decision <= 8:
            print(next_tagger, ": 나는 싫어")
            print(tagger, ": 그럼 누구?")
            lovegame_start(players, next_tagger, 0, name)
        else:
            print(next_tagger, ": 칵 퉤")
            refusal += 1
            if refusal == 3:
                return tagger
            lovegame_start(players, tagger, refusal, name)
        



game2(players, name)