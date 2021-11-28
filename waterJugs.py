class Jug:
    def __init__(self, name: str, maxVol: int):
        self.name = name
        self.maxVol = maxVol
        self.currentVol = 0

    def name(self):
        return self.name

    def peek(self):
        return self.currentVol

    def fill(self):
        self.currentVol = self.maxVol

    def dump(self):
        self.currentVol = 0

    def pourInto(self, jug):
        otherCurrentVol = jug.peek()
        availableVol = jug.maxVol - otherCurrentVol
        if self.currentVol > availableVol:
            jug.currentVol = jug.maxVol
            self.currentVol -= availableVol
        else:
            jug.currentVol += self.currentVol
            self.currentVol = 0


def printCurrentState(jug1: Jug, jug2: Jug, step = None):
    if step != None:
        print(f"Current volume in both after step {step}:\n\t{jug1.name}: {jug1.peek()} |----| {jug2.name}: {jug2.peek()}\n")
    else:
        print(f"Current volume in both at start:\n\t{jug1.name}: {jug1.peek()} |----| {jug2.name}: {jug2.peek()}\n")


def main():
    jug5 = Jug("Five Gal", 5)
    jug3 = Jug("Three Gal", 3)

    printCurrentState(jug5, jug3)

    print("Step 1: Fill jug3 to max.")
    jug3.fill()
    printCurrentState(jug5, jug3, 1)

    print("Step 2: Pour all of jug3 into empty jug5.")
    jug3.pourInto(jug5)
    printCurrentState(jug5, jug3, 2)

    print("Step 3: Fill jug3 to max.")
    jug3.fill()
    printCurrentState(jug5, jug3, 3)

    print("Step 4: Pour as much of jug3 that fits into jug5.")
    jug3.pourInto(jug5)
    printCurrentState(jug5, jug3, 4)

    print("Step 5: Dump all of jug5.")
    jug5.dump()
    printCurrentState(jug5, jug3, 5)

    print("Step 6: Pour all of jug3 into jug5.")
    jug3.pourInto(jug5)
    printCurrentState(jug5, jug3, 6)

    print("Step 7: Fill jug3 to max.")
    jug3.fill()
    printCurrentState(jug5, jug3, 7)

    print("Step 8: Finally, pour jug3 into jug5.")
    jug3.pourInto(jug5)
    printCurrentState(jug5, jug3, 8)

    print("SUCCESS!")


if __name__ == "__main__":
    main()
