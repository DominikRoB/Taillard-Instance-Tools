import time

class TaillardRNG:
    def __init__(self, seed=None):
        # Constants for the linear congruential generator
        self.a = 16807
        self.b = 127773
        self.c = 2836
        self.m = 2 ** 31 - 1

        # Initial seed
        self.X = seed if seed else int(time.time())

    def next(self):
        """ Denoted as U(0,1) """
        
        # Step 1: Modification of the seed
        k = self.X // self.b
        self.X = self.a * (self.X % self.b) - k * self.c

        # Check for negative value
        if self.X < 0:
            self.X = self.X + self.m

        # Step 2: New value of the seed
        return self.X / self.m

    def next_int(self, a, b):
        """Generate random integer between a and b (inclusive)
        Denotes as U[a, b]"""

        U = self.next()
        value = int(a + U * (b - a + 1))

        # Check the condition given by Taillard to avoid 32 bit overflow
        assert self.X * (b - a + 1) / self.m + a != value / (self.m / (b - a + 1))

        return value


if __name__ == '__main__':
    rng = TaillardRNG(seed=12345)
    print(rng.next())  # Print a random float between 0 and 1 (not included)
    print(rng.next_int(10, 20))  # Print a random integer between 10 and 20 (inclusive)
