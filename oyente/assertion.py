class Assertion:
    def __init__(self, block_from):
        # Block that contains the test (assertion)
        self.block_from = block_from

        # Was the assertion violated?
        self.violated = False

        # If the assertion was violated,
        # store the counterexample
        self.model = None

        # SMT2 query to decide the assertion
        self.query = None

        # Solidity function that might contain this assertion
        self.function = None

        # Branch that led to the assertion failure
        self.path = None

        # Symbolic constraints of that path
        self.sym = None

        # Position of ASSERTFAIL instruction in source
        self.begin_line = -1
        self.begin_column = -1
        self.end_line = -1
        self.end_column = -1

    def set_position(self, position):
        self.begin_line = position['begin']['line']
        self.begin_column = position['begin']['column']
        self.end_line = position['end']['line']
        self.end_column = position['end']['column']

    def set_sym(self, sym):
        self.sym = sym

    def get_sym(self):
        return self.sym

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def set_function(self, function):
        self.function = function

    def get_function(self):
        return self.function

    def get_block_from(self):
        return self.block_from

    def is_violated(self):
        return self.violated

    def set_violated(self, violated):
        self.violated = violated

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_query(self):
        return self.query

    def set_query(self, query):
        self.query = query

    def __str__(self):
        s =  "================\n"
        s += "Assertion from block %s, line %s : column %s to line %s : column %s\n" % (str(self.block_from), str(self.begin_line), str(self.begin_column), str(self.end_line), str(self.end_column))
        #s += "SMT2 query:\n" + str(self.query) + "\n"
        s += "Violated: " + str(self.violated) + "\n"
        s += "Function: "
        if self.function == None:
            s += "?\n"
        else:
            s += self.function + "\n"
        if self.violated:
            s += "Model:\n"
            for decl in self.model.decls():
                s += str(decl.name()) + " = " + str(self.model[decl]) + ", "
        return s

    def display(self):
        print self.__str__()

    def display_on_web(self):
        s =  "================\n"
        s += "Assertion failure from function: "
        if self.function == None:
            s += "?\n"
        else:
            s += self.function + "\n"
        return s
