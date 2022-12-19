#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    answer = []
    for idx in range(list_length):
        try:
            ans = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except IndexError:
            ans = 0
            print("out of range")
        except TypeError:
            ans = 0
            print("wrong type")
        except Exception:
            ans = 0
        finally:
            answer.append(ans)

    return answer

