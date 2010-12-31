import re

from util import hook

@hook.input
def ignore(inp):
    """
    This input hook demonstrates how to ignore requests from a certain user
    """
    return None if inp.nick in ('avidal_', 'badguy') else inp


@hook.output
def uppercase_output(inp, method, msg):
    """
    This function is called with two arguments, the method and the message
    The method is one of the speaking methods of the Input object: say,
        reply, pm, me, or notice
    msg is the actual message that is going to be sent

    this function can return a string, in which case that string is sent
    using the same method that was passed in here, or it can return None
    in which case the message will not be sent at all
    """

    return msg.upper()


@hook.output
def censor_words(inp, method, msg):
    """
    This hook can be used to filter certained censored words which may result
    in the bot being banned from a network if they are mentioned
    """

    # note, these would normally be in the config file
    censored = [
        'DCC SEND',
        '1nj3ct',
        'startkeylogger',
        '!coz',
    ]

    censored = map(re.escape, censored)

    replacement = '[censored]'

    # bad words are fine in PMs, but nowhere else
    if method == 'pm': return msg

    rx = re.compile('(%s)' % '|'.join(censored), re.IGNORECASE)
    msg = rx.sub(replacement, msg)

    return msg
