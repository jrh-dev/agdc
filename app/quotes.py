"""
A list of quotations from Aliens
"""

import random

QUOTES = (
    """
    Hey Vasquez, have you ever been mistaken for a man? <br>
    No. Have you?
    """,
    """
    Get away from her, you <strong>bitch!</strong>
    """,
    """
    They cut the power. <br>
    What do you mean <i>they</i> cut the power? How could they cut the power, man? <br>
    They're animals!
    """,
    """
    Did IQ's just drop sharply while I was away?
    """,
    """
    Well, that's great. <br>
    That's just fuckin' great, man! Now what the fuck are we supposed to do? <br>
    We're in some real pretty shit now, man!
    """,
    """
    That's it, man. <br>
    Game over, man. Game over! <br>
    What the fuck are we gonna do now? What are we gonna do?
    """,
    """
    We'd better get back 'cause it'll be dark soon and they mostly come at night. <br>
    Mostly.
    """,
    """
    I say we take off and nuke the entire site from orbit. <br>
    It's the only way to be sure.
    """,
    """
    All right sweethearts, you heard the man and you know the drill. Assholes and elbows! <br>
    Hudson, come here! Come <strong>here</strong>!
    """,
    """
    All right, sweethearts, what are you waiting for? Breakfast in bed? <br>
    Another glorious day in the Corps! <br>
    A day in the Marine Corps is like a day on the farm. <br>
    Every meal's a banquet! Every paycheck a fortune! Every formation a parade! <br>
    I <strong>love</strong> the Corps!
    """,
    """
    We're on an express elevator to hell, going down!
    """,
    """
    Hey, maybe you haven't been keeping up on current events, but we just got our asses kicked, pal!
    """,
    """
    Look, man. I only need to know one thing... <br>
    ...<strong>where<strong>...<strong>they<strong>...<strong>are<strong>.
    """,
    """
    We're in the pipe, five by five.
    """,    
)

def get_quote() -> str:
    """
    Get a random quote from the list of quotes.
    """
    return random.choice(QUOTES)