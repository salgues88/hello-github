# 나도코딩 활용편 1 추억의 오락실 게임을 만들어 보자

# 나도코딩 활용편

# 8개의 실전 프로젝트 : 머신러닝, 데이터 분석, 업무 자동화, 아두이노 RC Car, 얼굴인식 등

# pip install pygame 으로 pygame 설치

import pygame

pygame.init()                                       # 초기화 (해당 코드 반드시 필요!!!)

# 화면 크기 설정 
screen_width = 480                                  # 스크린 가로 크기
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Coding")           # 게임 이름

# 여기까지 작성 후 실행 -> 밑에 아무 내용도 없어서 프로그램이 바로 꺼짐 -> 이벤트 루프 추가

# 이벤트 루프   (마우스나 키보드 동작이 오기 전까지 계속 실행시키는 기능)
running = True                                      # 게임이 진행중인가? (지금 작성하는 부분은 pygame 실행을 위해 반드시 적어야함)
while running:                                      # running이 True니 계속 돌아감
    for event in pygame.event.get():                # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:               # 창이 닫히는 이벤트가 발생했는가? (= 팝업창 X 버튼 눌렸는가?)
            running = False                         # 게임이 진행 중이 아님

# pygame 종료
pygame.quit()