import sys
import random
import re

class MPP_Interpreter:
    def __init__(self, filename):
        self.memory = [0] * 1000000   # 1 million memory cells
        self.stack = []
        self.output = []
        self.labels = {}
        self.program = []
        self.pc = 0
        self.running = True
        self.loop_stack = []
        self.call_stack = []
        self.current_color = "\033[0m"  # Default terminal color
        self.variables = {}  # store all typed variables
        self.load_program(filename)

    # ---------------- Load Program & Labels ----------------
    def load_program(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip() and not l.strip().startswith('//')]
        self.program = lines
        for i, l in enumerate(self.program):
            if l.endswith(':'):
                self.labels[l[:-1]] = i

    # ---------------- Stack / Memory ----------------
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop() if self.stack else 0

    def set_mem(self, addr, val):
        if 0 <= addr < len(self.memory):
            self.memory[addr] = val
        else:
            print(f"Memory address {addr} out of range!")

    def get_mem(self, addr):
        if 0 <= addr < len(self.memory):
            return self.memory[addr]
        else:
            print(f"Memory address {addr} out of range!")
            return 0

    def rand(self, limit=256):
        return random.randint(0, limit - 1)

    # ---------------- Run Program ----------------
    def run(self):
        while self.pc < len(self.program) and self.running:
            line = self.program[self.pc]
            self.execute(line)
            self.pc += 1

    # ---------------- Execute Single Line ----------------
    def execute(self, line):
        parts = line.split()
        if not parts: 
            return
        cmd = parts[0]

        # -------- Output --------
        if cmd == '#':   # print
            text = ' '.join(parts[1:])
            text = re.sub(r'\$(\w+)', lambda m: str(self.get_var(m.group(1))), text)
            print(self.current_color + text + "\033[0m")
            self.output.append(text)

        elif cmd == 'Q': 
            self.running = False

        # -------- Colors --------
        elif cmd == 'COLOR':
            if len(parts) > 1:
                color_name = parts[1].upper()
                colors = {
                    "RED": "\033[31m",
                    "GREEN": "\033[32m",
                    "YELLOW": "\033[33m",
                    "BLUE": "\033[34m",
                    "MAGENTA": "\033[35m",
                    "CYAN": "\033[36m",
                    "WHITE": "\033[37m",
                    "RESET": "\033[0m"
                }
                self.current_color = colors.get(color_name, "\033[0m")

        # -------- Stack / Memory --------
        elif cmd == 'P':
            if len(parts) == 1:
                print()
                return
            val = parts[1]
            if val.startswith('$'):
                val = self.get_var(val[1:])
            else:
                try:
                    val = int(val)
                except ValueError:
                    val = val
            self.push(val)

        elif cmd == 'O':
            val = self.pop()
            print(val)

        elif cmd == 'MSET':
            self.set_mem(int(parts[1]), int(parts[2]))

        elif cmd == 'MGET':
            self.push(self.get_mem(int(parts[1])))

        # -------- Random --------
        elif cmd == '~':
            self.push(self.rand(int(parts[1]) if len(parts) > 1 else 256))

        # -------- Arithmetic --------
        elif cmd == '+':
            b, a = self.pop(), self.pop()
            self.push(a + b)

        elif cmd == '-':
            b, a = self.pop(), self.pop()
            self.push(a - b)

        elif cmd == '*':
            b, a = self.pop(), self.pop()
            self.push(a * b)

        elif cmd == '/':
            b, a = self.pop(), self.pop()
            self.push(a // b if b != 0 else 0)

        elif cmd == '%':
            b, a = self.pop(), self.pop()
            self.push(a % b if b != 0 else 0)

        # -------- Logic --------
        elif cmd == '&':
            b, a = self.pop(), self.pop()
            self.push(a & b)

        elif cmd == '|':
            b, a = self.pop(), self.pop()
            self.push(a | b)

        elif cmd == '!':
            a = self.pop()
            self.push(~a)

        elif cmd == 'XX':  # XOR
            a, b = self.pop(), self.pop()
            self.push(a ^ b)

        # -------- Comparison --------
        elif cmd == '>':
            b, a = self.pop(), self.pop()
            self.push(1 if a > b else 0)

        elif cmd == '<':
            b, a = self.pop(), self.pop()
            self.push(1 if a < b else 0)

        elif cmd == '=':
            b, a = self.pop(), self.pop()
            self.push(1 if a == b else 0)

        # -------- Control Flow --------
        elif cmd == '?':
            val = self.pop() if self.stack else 0
            if len(parts) > 1:
                label = parts[1]
                if val == 0 and label in self.labels:
                    self.pc = self.labels[label]

        elif cmd == '[':
            self.loop_stack.append(self.pc)

        elif cmd == ']':
            if self.loop_stack:
                self.pc = self.loop_stack[-1] - 1

        elif cmd == 'CJ':
            val = self.pop()
            if val != 0 and len(parts) > 1:
                label = parts[1]
                if label in self.labels:
                    self.pc = self.labels[label]

        # -------- Functions --------
        elif cmd == '{':
            self.call_stack.append(self.pc)

        elif cmd == '}':
            if self.call_stack:
                self.pc = self.call_stack.pop()

        # -------- Stack Magic --------
        elif cmd == 'DU':
            val = self.pop()
            self.push(val)
            self.push(val)

        elif cmd == '@':
            a, b = self.pop(), self.pop()
            self.push(a)
            self.push(b)

        elif cmd == 'RS':
            self.stack.reverse()

        elif cmd == 'RM':
            for i in range(16):
                self.set_mem(i, self.rand(256))

        elif cmd == 'XY':
            self.push(self.get_mem(0) + self.get_mem(1))

        elif cmd == '!!':
            print(''.join(chr(s % 256) for s in self.stack))

        # -------- Input --------
        elif cmd == 'INPUT':
            var = parts[1] if len(parts) > 1 else "in"
            user_in = input("> ")
            if user_in.isdigit():
                self.push(int(user_in))
                self.set_var(var, int(user_in))
            else:
                for c in user_in:
                    self.push(ord(c))
                self.push(10)
                self.set_var(var, user_in)

        # -------- Variable Types --------
        elif cmd == 'NU':  # number
            name = parts[1]
            val = int(parts[2]) if len(parts) > 2 else 0
            self.variables[name] = val

        elif cmd == 'FL':  # float
            name = parts[1]
            val = float(parts[2]) if len(parts) > 2 else 0.0
            self.variables[name] = val

        elif cmd == 'ST':  # string
            name = parts[1]
            val = ' '.join(parts[2:]) if len(parts) > 2 else ""
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            self.variables[name] = val

        elif cmd == 'BO':  # boolean
            name = parts[1]
            val = parts[2].lower() == "true" if len(parts) > 2 else False
            self.variables[name] = val

        # -------- Labels --------
        elif cmd.endswith(':'):
            pass

        # -------- Unknown --------
        else:
            print(f"Unknown symbol: {cmd}")

    # ---------------- Variables ----------------
    def set_var(self, name, value):
        self.variables[name] = value
        self.memory[hash(name) % len(self.memory)] = value

    def get_var(self, name):
        if name in self.variables:
            return self.variables[name]
        return self.memory[hash(name) % len(self.memory)]


# -------------------- Run from command line --------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mpp_interpreter.py program.m++")
        sys.exit(1)
    interp = MPP_Interpreter(sys.argv[1])
    interp.run()
