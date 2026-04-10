class Room():

    def __init__(self, name, height, length, width):
        self.name = name
        self.height = height
        self.length = length
        self.width = width

    @staticmethod
    def mm_to_ft(mm):
        return mm * 0.0032808399

    @staticmethod
    def sqmm_to_sqft(sqmm):
        return sqmm * 1.07639e-5

    def height_in_ft(self):
        return Room.mm_to_ft(self.height)

    @property
    def width_in_ft(self):
        return Room.mm_to_ft(self.width)

    def length_in_ft(self):
        return Room.mm_to_ft(self.length)

    def wall_area(self):
        return self.length * 2 * self.height + self.width * 2 * self.height

    def __str__(self):
        return (f"{self.name}: "
                f"height: {self.height}, "
                f"length: {self.length} "
                f"width: {self.width}"
                )


lounge = Room('Lounge', 1300, 4000, 2000)
snug = Room('Snug', 1300, 2500, 2000)
kitchen = Room('Kitchen', 2000, 3500, 1900)

print(lounge.name, "height:", lounge.height,
      "length:", lounge.length, "width:", lounge.width)
print(snug)  # uses __str__ method

# f-strings are used for formatting, the :.2f part formats decimal numbers rounded to 2 places
print(f"{lounge.name} length in feet: {lounge.height_in_ft():.2f}")  # note, () to call method
print(f"{snug.name} wall area: {snug.wall_area():.2f} in sq.mm., "
      f"{snug.sqmm_to_sqft(snug.wall_area()):.2f} in sq.ft.")
print(f"Snug width in feet: {snug.width_in_ft:.2f}")  # note, no () after method