class MetaflowException(Exception):
    headline = "Flow failed"

    def __init__(self, msg="", lineno=None):
        self.message = msg
        self.line_no = lineno
        super(MetaflowException, self).__init__()

    def __str__(self):
        prefix = "line %d: " % self.line_no if self.line_no else ""
        return "%s%s" % (prefix, self.message)
