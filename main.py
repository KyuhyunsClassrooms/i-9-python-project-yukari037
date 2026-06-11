# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 

# ============================================================
# 사용 안내
# ------------------------------------------------------------
# 이 파일은 예시 골격입니다.
# 그대로 제출하지 말고, 반드시 자신의 주제에 맞게 수정하세요.
#
# 필수 조건
# 1. 2차원 리스트 사용
# 2. 함수 2개 이상, 가능하면 3개 이상 분리
# 3. 조건문 사용
# 4. 반복문 사용
# 5. 실행 결과 출력
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 아래 예시는 "활동 추천 프로그램"입니다.
# 자신의 주제에 맞게 data를 만드세요.
#
# 현재 열의 의미:
# 0번 열: 활동 이름
# 1번 열: 필요한 시간(분)
# 2번 열: 추천 기분
# 3번 열: 활동 유형
# ------------------------------------------------------------

import time

launch_checklist = [
    ["추력(kg)", 0, 1200, "X"],
    ["무게(kg)", 0, 1000, "X"],
    ["연료(%)", 0, 90, "X"]
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def conditions(launch_checklist):
    print("로켓 발사 조건 데이터를 입력하세요")
    launch_checklist[0][1] = int(input(f"{launch_checklist[0][0]}을 입력하세요:"))
    launch_checklist[1][1] = int(input(f"{launch_checklist[1][1]}을 입력하세요:"))
    launch_checklist[2][1] = int(input(f"{launch_checklist[2][1]}을 입력하세요:"))
    print("완료\n")
    return launch_checklist

def check(launch_checklist):
    thrust = launch_checklist[0][1]
    weight = launch_checklist[1][1]
    fuel = launch_checklist[2][1]

    all_pass = True

    if thrust >= weight * 1.2:
        launch_checklist[0][3] = "O"
    else:
        launch_checklist[0][3] = "X"
        all_pass = False

    if fuel >= 90:
        launch_checklist[2][3] = "O"
    else:
        launch_checklist[2][3] = "X"
        all_pass = False

    return all_pass


def countdown():
    print("launch starts")
    
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)

    print("발사합니다")

def result():
    if all_pass == True:
        print("SUCCESS")

    else:
        print("FAILED...")




def main():
    show_intro()
    mood, minutes = get_user_input()
    results = find_recommendations(activities, mood, minutes)
    print_result(results)


# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
main()
