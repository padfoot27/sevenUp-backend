class ActiveOnLinkGenerator:
    length = 17

    def __init__(self):
        self.activeOnLink = ''.join(random.SystemRandom()
                .choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(self.length))

