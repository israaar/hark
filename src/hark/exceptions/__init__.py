class NotImplemented(Exception):
    pass


class InvalidImagePath(Exception):
    pass


class ModelInvalidException(Exception):
    def __init__(self, instance, reason):
        self.model = instance
        name = instance.__class__.__name__
        msg = "%s invalid: %s" % (name, reason)
        Exception.__init__(self, msg)


class InvalidMachineException(Exception):
    pass


class InvalidQueryConstraint(Exception):
    pass


class DuplicateModelException(Exception):
    def __init__(self, instance, e=None):
        self.model = instance
        name = instance.__class__.__name__
        if e is not None:
            msg = "A %s with the same field values already exists." \
                "The original error: %s" % (name, str(e))
        else:
            msg = "A %s with the same field values already exists" % name
        Exception.__init__(self, msg)


class UnknownPlatformException(Exception):
    def __init__(self, platform):
        msg = 'Hark does not understand this value for sys.platform: ' \
            + platform
        Exception.__init__(self, msg)


class UnknownGuestException(Exception):
    pass


class UnknownDriverException(Exception):
    pass


class UnsupportedDriverException(Exception):
    def __init__(self, platform, driver):
        msg = "Your platform - '%s' - does not support the driver '%s'" \
            % (platform, driver)
        Exception.__init__(self, msg)


class CommandFailed(Exception):
    def __init__(self, command, result):
        self.command = command
        self.result = result
        msg = "Command '%s' had exit_status %d and stderr: '%s'" % (
            command.cmd, result.exit_status, result.stderr)
        Exception.__init__(self, msg)


class MachineNotFound(Exception):
    pass


class ImageNotFound(Exception):
    pass


class UnrecognisedMachineState(Exception):
    pass


class InvalidStatus(Exception):
    """
    Exception used when the user tries to make an invalid status change to a
    machine, e.g. removing it while it's still running, or starting it, while
    it's started, etc.
    """
    pass


class BadHarkEnvironment(Exception):
    def __init__(self, *complaints):
        msg = "hark found %d issues with your environment; they were:\n%s" % (
            len(complaints), "\n ".join(complaints)
        )
        Exception.__init__(self, msg)


class NetworkFull(Exception):
    def __init__(self, max_avail):
        msg = 'No available addresses remaining - ' \
            'the hark network can only support %d hosts; ' \
            'try removing some hosts first.'
        Exception.__init__(self, msg)
