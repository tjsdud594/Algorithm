### 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/42579

###############################
#           풀이완료           #
###############################



def solution(genres, plays):
    from collections import defaultdict
    answer = []
    sings_dict = {}
    genres_dict = defaultdict(int)
    genre_cnt_dict = defaultdict(int)

    for i, z in enumerate(zip(genres, plays)):
        sings_dict[i] = list(z)
        genres_dict[z[0]]+=z[1]

    # 각 노래별로 장르, 노래 재생 횟수, 장르 총 재생 횟수 넣기
    for k in sings_dict:
        sings_dict[k].append(genres_dict[sings_dict[k][0]])

    sorted_sings = sorted(sings_dict.items(), key=lambda x : (-x[1][2], -x[1][1], x[0]))

    for sing in sorted_sings:
        genre_cnt_dict[sing[1][0]]+=1
        if genre_cnt_dict[sing[1][0]]<=2:
            answer.append(sing[0])

    return answer





if __name__ == "__main__":
    import time
    import random

    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]

    start = time.time()
    print(solution(genres, plays))
    end = time.time()

    print(f"{end - start:.5f} sec")