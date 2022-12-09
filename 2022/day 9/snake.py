class BodyPart:
    def __init__(self, pos=[0, 0]):
        self.pos = pos
        self.next = None


class Snake:
    def __init__(self):
        self.head = None


head = Snake()
Snake.head = BodyPart([0, 0])
body_1 = BodyPart([0, 0])
body_2 = BodyPart([0, 0])
body_3 = BodyPart([0, 0])
body_4 = BodyPart([0, 0])
body_5 = BodyPart([0, 0])
body_6 = BodyPart([0, 0])
body_7 = BodyPart([0, 0])
body_8 = BodyPart([0, 0])
body_9 = BodyPart([0, 0])

body_1.next = Snake.head
body_2.next = body_1
body_3.next = body_2
body_4.next = body_3
body_5.next = body_4
body_6.next = body_5
body_7.next = body_6
body_8.next = body_7
body_9.next = body_8
