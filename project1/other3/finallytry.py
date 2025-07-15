
def maintry(): 
    try:
        a = int(input())
    except Exception as e:
        print(e)

    finally:
       pass


maintry()
# print(__name__)


if __name__ == "__main__":
    # if the code is directly runnng the code
    print('if the code is directly runnng the code')