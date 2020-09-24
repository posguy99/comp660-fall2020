# base case example
# taken from https://www.shmoop.com/computer-science/recursion/base-case.html
# and shamelessly modified

def runAwayFromZombies():
    pass


def lookForZombies():
    pass


def escapeZombies(numberOfZombies):
    """Escape from the zombie horde

    Args:
        numberOfZombies ([int]): [number of zombies in vicinity]
    """
    # the base case is the number of zombies, the test is whether or not
    # there are still zombies around.  As long as it's > 0, the
    # recursion continues because the base case is not reached.
    if numberOfZombies > 0:
        runAwayFromZombies()
        numberOfZombies = lookForZombies()
        escapeZombies(numberOfZombies)
    else:
        # ok, we got here, so the if failed the check, there are
        # no more zombies
        return 0
