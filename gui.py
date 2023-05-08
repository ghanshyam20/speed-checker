from time import time

# calculate the accuracy of input prompt
def typingErrors(prompt, input_words):
    words = prompt.split()
    errors = 0

    for i in range(len(words)):
        if i in (0, len(words)-1):
            if words[i] == input_words[i]:
                continue
            else:
                errors += 1
        else:
            if words[i] == input_words[i]:
                if (words[i+1] == input_words[i+1]) and (words[i-1] == input_words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    input_words = iprompt.split()
    twords = len(input_words)
    time = etime - stime
    speed = twords / (time / 60)

    return speed

# calculate total time elapsed
def timeElapsed(stime, etime):
    time = etime - stime

    return time

if __name__ == '__main__':
    prompt = "Hi, my name is ghanshyam, I am a Python lover."
    print("Type this: '", prompt, "'")

    # listening to input ENTER
    input("Press ENTER when you are ready!")

    # recording time for input
    stime = time()
    iprompt = input()
    etime = time()

    # gather all the information returned from functions
    elapsed_time = round(timeElapsed(stime, etime), 2)
    speed = typingSpeed(iprompt, stime, etime)
    errors = typingErrors(prompt, iprompt)

    # printing all the required data
    print("Total Time elapsed: ", elapsed_time, "s")
    print("Your Average Typing Speed was: ", speed, "words / minute")
    print("With a total of: ", errors, "errors")
