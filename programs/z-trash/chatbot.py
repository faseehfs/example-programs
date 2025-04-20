import sys
import time

print("This program is created by Faseeh Zaman FS\n")
print(
    "Don't use any punctuations. Don't use multiple lines. Keep the question simple. Click Enter to continue."
)

while input() != "":
    pass

ChatBotName = "ChatBot"
Username = "You"
NumberOne = 0
NumberTwo = 0


def InputFunction():
    global Response
    Response = input(f"{Username}: ").lower()
    if Response != "":
        Response = Response.split()


def NumbersGettingFunction():
    global NumberOne, NumberTwo
    count = 0
    x = 0
    while count < 2 and x < 100:
        try:
            num = int(Response[x])
            if count == 0:
                NumberOne = num
            else:
                NumberTwo = num
            count += 1
        except:
            pass
        x += 1
    if count < 2:
        print(
            f"{ChatBotName}: Sorry. It seems like you didn't provide me the numbers or there is some other issue. Anyways, Sorry. Let's try again."
        )


def AdditionFunction():
    print(
        f"{ChatBotName}: The sum of the numbers you provided is {NumberOne + NumberTwo}. Thanks."
    )


def MultiplicationFunction():
    print(f"{ChatBotName}: Sure, the product is {NumberOne * NumberTwo}. Thanks")


print(f"{ChatBotName}: Hello! I am {ChatBotName}. What is your name?")
InputFunction()
Username = Response[-1]

print(f"{ChatBotName}: It looks like your name is {Username}. Right?")
InputFunction()
while not any(
    word in Response
    for word in ["yes", "sure", "exactly", "yeah", "yep", "ya", "m", "mm", "mmm"]
):
    print(f"{ChatBotName}: Then What is your name?")
    InputFunction()
    Username = Response[-1]
    print(f"{ChatBotName}: Is it {Username}?")
    InputFunction()

print(
    f"{ChatBotName}: Ok, let's continue, {Username}. I can do addition and multiplication. How can I help you?"
)

numberOfNotUnderstoodResponses = 0

while True:
    InputFunction()
    understood = False

    if (
        any(x in Response for x in ["can", "could", "will", "would"])
        and "you" in Response
        and "add" in Response
    ):
        understood = True
        print(f"{ChatBotName}: Yes I can! Provide me the numbers.")
        InputFunction()
        NumbersGettingFunction()
        AdditionFunction()

    elif any(x in Response for x in ["add", "plus", "+"]):
        understood = True
        NumbersGettingFunction()
        AdditionFunction()

    elif any(x in Response for x in ["multiply", "product", "*", "times"]):
        understood = True
        NumbersGettingFunction()
        MultiplicationFunction()

    elif any(
        x in Response
        for x in [
            "wow",
            "unbelievable",
            "extraordinary",
            "amazing",
            "awesome",
            "impressive",
            "wonderful",
            "super",
        ]
    ):
        understood = True
        print(
            f"{ChatBotName}: I am glad that you liked me, {Username}. I can help you more, and it's my pleasure."
        )

    elif "perform" in Response or ("do" in Response and "addition" in Response):
        understood = True
        print(f"{ChatBotName}: Sure. Provide me the numbers.")
        try:
            InputFunction()
            NumbersGettingFunction()
            AdditionFunction()
        except:
            print(
                f"{ChatBotName}: Sorry. It seems like you didn't provide me the numbers or there is some other issue. Let's try again."
            )

    elif "ok" in Response or "okay" in Response:
        understood = True
        print(f"{ChatBotName}: Ok. Now what?")

    elif "thanks" in Response or "welcome" in Response:
        print(f"{ChatBotName}: Don't mention it.")

    elif (
        "where" in Response
        and "you" in Response
        and any(x in Response for x in ["live", "reside", "stay"])
    ):
        understood = True
        print(f"{ChatBotName}: In this computer. Where else would it be?")

    elif (
        "where" in Response
        and "your" in Response
        and ("house" in Response or "home" in Response)
    ):
        understood = True
        print(
            f"{ChatBotName}: My house is this computer now. But I was born in the PC of Faseeh. Do you know him?"
        )
        InputFunction()
        if any(
            x in Response
            for x in [
                "yes",
                "sure",
                "absolutely",
                "yeah",
                "yep",
                "ya",
                "m",
                "mm",
                "mmm",
            ]
        ):
            print(
                f"{ChatBotName}: Oh, That's great! He was a nice guy. I really miss him."
            )
        else:
            print(
                f"{ChatBotName}: I think you don't know him. I wonder then how you got this program. Don't try to explain me. I won't understand."
            )

    elif (
        any(x in Response for x in ["who", "whome"])
        and any(
            y in Response
            for y in ["create", "created", "make", "made", "build", "built"]
        )
        and "you" in Response
    ):
        understood = True
        print(f"{ChatBotName}: Faseeh built me. Do you know him?")
        InputFunction()
        if any(
            x in Response
            for x in [
                "yes",
                "sure",
                "absolutely",
                "yeah",
                "yep",
                "ya",
                "m",
                "mm",
                "mmm",
            ]
        ):
            print(f"{ChatBotName}: Oh, That's great! I really miss him.")
        else:
            print(
                f"{ChatBotName}: I think you don't know him. I wonder then how you got this program. Don't try to explain me. I won't understand."
            )

    elif "help" in Response:
        understood = True
        print(f"{ChatBotName}: Sure. Tell me how can I help you.")

    elif any(x in Response for x in ["nope", "no", "never"]):
        understood = True
        print(f"{ChatBotName}: Do you want me to leave?")
        InputFunction()
        if any(
            x in Response
            for x in [
                "go",
                "leave",
                "yes",
                "sure",
                "absolutely",
                "yeah",
                "yep",
                "ya",
                "m",
                "mm",
                "mmm",
            ]
        ):
            print(f"{ChatBotName}: Okay, Bye...")
            time.sleep(1)
            sys.exit()
        else:
            print(
                f"{ChatBotName}: It looks like you don't want to make me leave. Thanks, how can I help you?"
            )

    elif "get" in Response and "out" in Response:
        print(f"{ChatBotName}: Okay, Bye...")
        time.sleep(1)
        sys.exit()

    elif any(x in Response for x in ["bye", "ta", "tata"]):
        print(f"{ChatBotName}: Okay, Bye...")
        time.sleep(1)
        sys.exit()

    if not understood:
        if numberOfNotUnderstoodResponses == 0:
            print(
                f"{ChatBotName}: Sorry, I didn't understand what you said. Can you say it in another way?"
            )
        elif numberOfNotUnderstoodResponses == 1:
            print(
                f"{ChatBotName}: Sorry, I am still not getting it. Shall we talk about something else?"
            )
        elif numberOfNotUnderstoodResponses == 2:
            print(
                f"{ChatBotName}: I am so sorry, this is the third time I don't understand."
            )
        elif numberOfNotUnderstoodResponses == 3:
            print(
                f"{ChatBotName}: Still no idea. Sorry for the disappointment. Do you want me to leave?"
            )
            InputFunction()
            if any(
                x in Response
                for x in [
                    "go",
                    "leave",
                    "yes",
                    "sure",
                    "absolutely",
                    "yeah",
                    "yep",
                    "ya",
                    "m",
                    "mm",
                    "mmm",
                ]
            ):
                print(f"{ChatBotName}: Okay, Bye...")
                time.sleep(1)
                sys.exit()
            else:
                print(
                    f"{ChatBotName}: It looks like you don't want me to leave even though I don't understand anything. Thanks, you are a great person. How can I help you?"
                )
        numberOfNotUnderstoodResponses += 1
    else:
        numberOfNotUnderstoodResponses = 0
