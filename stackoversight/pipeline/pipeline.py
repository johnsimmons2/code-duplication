class Pipeline(object):
    def __init__(self, steps):
        self.steps = steps
    
    def feed(self, items):
        # Feed the item into one step, get the result, feed the
        # result to the next step and so on.
        for step in self.steps:
            step.process(items)
            items = step.get()

        return items
