from Exceptions_for_ques import InvalidAnsError
import math,random,datetime

def is_convertible_to_int(val):
    try:
        int(val)
        return True
    except (ValueError, TypeError):
        return False


def sqaureFunc(score):
        try:
            obj = {}
            num = random.randint(1,100)
            obj["type"] = "square of number"
            print(f"Give square of {num}:")
            prev = datetime.datetime.now()
            ans = input()
            cur = datetime.datetime.now()
            time_taken = cur - prev
            obj["time_to_ans"] = time_taken.total_seconds()
            print(f"Time taken to answer: {time_taken.total_seconds()} seconds")
            if is_convertible_to_int(ans)==False:
                raise InvalidAnsError(ans)
            ans = int(ans)
            if(ans==(num**2)):
                print("correct answer!!")
                score += 10
                obj["output"] = "correct" 
            else:
                score -= 5
                print("Oops.. Wrong answer")
                obj["output"] = "wrong" 
            obj["num"] = num
            obj["user_input"] = ans
            obj["cur_score"] = score
        except InvalidAnsError as e:
             print(e)
        finally:
            return score,obj

        
             
       

def sqaureRootFunc(score):
        try:
            obj = {}
            num = random.randint(1,10000)
            obj["type"] = "square root of number"
            while(math.sqrt(num) != int(math.sqrt(num))):
                num = random.randint(1,10000)
            print(f"Give square root of {num}:")
            prev = datetime.datetime.now()
            ans = input()
            cur = datetime.datetime.now()
            time_taken = cur - prev
            obj["time_to_ans"] = time_taken.total_seconds()
            print(f"Time taken to answer: {time_taken.total_seconds()} seconds")
            if is_convertible_to_int(ans)==False:
                raise InvalidAnsError(ans)
            ans = int(ans)
            if(ans**2==num):
                print("correct answer!!")
                score += 10
                obj["output"] = "correct" 
            else:
                score -= 5
                print("Oops.. Wrong answer")
                obj["output"] = "wrong" 
            obj["num"] = num
            obj["user_input"] = ans
            obj["cur_score"] = score
        except InvalidAnsError as e:
            print(e)
        finally:
            return score,obj