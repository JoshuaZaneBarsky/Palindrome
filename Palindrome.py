class Palindrome:

    global INPUT, WORK, OUTPUT
    INPUT, WORK, OUTPUT = 0, 1, 2

    def __init__(self, test=False): # input tape is a string of 1s and 0s  
        self.input_tape, self.worktape, self.output_tape = [], [], []     
        self.state = 'begin' # begin, copy, check, halt
        self.runtime = 0

        self.test = test # if we are using the test case
    
    def is_palindrome(self, input_tape):
        self.create_tapes(input_tape)
        if not self.test: self.print_tapes()
        while (self.state != 'halt'):
            self.run_cases()
            self.runtime_step()
            if not self.test: self.print_tapes()
        if not self.test: self.print_result()
        return self.tapes[OUTPUT][self.head_position[OUTPUT]]

    def create_tapes(self, input_tape):
        self.input_tape = ['▷'] + input_tape + ['☐']
        self.worktape = ['▷'] + ['☐'] * (len(self.input_tape)-1)
        self.output_tape = ['▷','☐']

        self.tapes = [self.input_tape, self.worktape, self.output_tape]
        self.head_position = [0,0,0] # in, work, out

    def run_cases(self):
        match self.state:
            case 'begin':
                self.run_begin_state()
            case 'copy':
                self.run_copy_state()
            case 'check':
                self.run_check_state()
            case 'halt':
                return self.tapes[OUTPUT][self.get_head_position[OUTPUT]]
            
    def run_begin_state(self):
        self.move_right(INPUT)
        self.move_right(OUTPUT)
        self.state = 'copy'
            
    def run_copy_state(self):
        if self.tapes[INPUT][self.head_position[INPUT]] in [0, 1] and self.tapes[WORK][self.head_position[WORK]] == '▷':
            self.move_right(INPUT)
        elif self.tapes[INPUT][self.head_position[INPUT]] == '☐' and self.tapes[WORK][self.head_position[WORK]] == '▷':
            self.move_left(INPUT)
            self.move_right(WORK)
        elif self.tapes[INPUT][self.head_position[INPUT]] in [0, 1] and self.tapes[WORK][self.head_position[WORK]] == '☐':
            b = self.tapes[INPUT][self.head_position[INPUT]]
            self.write_bit(1, b)
            self.move_left(INPUT)
            self.move_right(WORK)
        elif self.tapes[INPUT][self.head_position[INPUT]] == '▷' and self.tapes[WORK][self.head_position[WORK]] == '☐':
            self.move_left(WORK)
        elif self.tapes[INPUT][self.head_position[INPUT]] == '▷' and self.tapes[WORK][self.head_position[WORK]] in [0, 1]:
            self.move_left(WORK)
        elif self.tapes[INPUT][self.head_position[INPUT]] == '▷' and self.tapes[WORK][self.head_position[WORK]] == '▷':
            self.move_right(INPUT)
            self.move_right(WORK)
            self.state = 'check'
        else:
            print("Error in run_copy_state: condition not found for (" + str(self.tapes[INPUT][self.head_position[INPUT]]) + "," + str(self.tapes[WORK][self.head_position[WORK]]) + ')')
            self.state = 'halt'

    def run_check_state(self):
        if self.tapes[INPUT][self.head_position[INPUT]] in [0, 1] and self.tapes[WORK][self.head_position[WORK]] == self.tapes[INPUT][self.head_position[INPUT]]:
            self.move_right(INPUT)
            self.move_right(WORK)
        elif self.tapes[INPUT][self.head_position[INPUT]] in [0, 1] and self.tapes[WORK][self.head_position[WORK]] == (1 - self.tapes[INPUT][self.head_position[INPUT]]):
            self.write_bit(2, 0)
            self.state = 'halt'
        elif self.tapes[INPUT][self.head_position[INPUT]] == '☐' and self.tapes[WORK][self.head_position[WORK]] == '☐':
            self.write_bit(2, 1)
            self.state = 'halt'
        else:
            print("Error in run_check_state: condition not found for (" + str(self.tapes[INPUT][self.head_position[INPUT]]) + "," + str(self.tapes[WORK][self.head_position[WORK]]) + ')')
            self.state = 'halt'

    def get_head_position(self, i):
        return self.head_position[i]
    
    def move_right(self, i):
        self.head_position[i] += 1

    def move_left(self, i):
        self.head_position[i] -= 1

    def write_bit(self, i, b):
        self.tapes[i][self.head_position[i]] = b # b can be {1, 0, ☐}
    
    def runtime_step(self):
        self.runtime += 1

    # --- For printing --- #
    def print_result(self):
        print("is_palindrome(" + str(self.input_tape) + ") = " + str(self.tapes[OUTPUT][self.head_position[OUTPUT]]))
        print("Runtime: " + str(self.runtime))

    def print_tapes(self):
        in_length = len(str(self.tapes[INPUT]))
        work_length = len(str(self.tapes[WORK]))
        out_length = len(str(self.tapes[OUTPUT]))
        longest_length = self.check_longest_string_length(in_length, work_length, out_length)

        spaces1 = longest_length - in_length
        spaces2 = longest_length - work_length
        spaces3 = longest_length - out_length

        print("--")
        print("In " + self.state + " state.")
        print("Input:  " + str(self.tapes[INPUT]) + " "*spaces1 + " Position: " + str(self.head_position[INPUT]))
        print("Work:   " + str(self.tapes[WORK]) + " "*spaces2 + " Position: " + str(self.head_position[WORK]))
        print("Output: " + str(self.tapes[OUTPUT]) + " "*spaces3 + " Position: " + str(self.head_position[OUTPUT]))

    def check_longest_string_length(self, a, b, c):
        if a>b and a>c:
            return a
        elif b>c:
            return b
        else:
            return c