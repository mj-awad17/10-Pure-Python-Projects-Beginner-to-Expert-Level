# 📊 Text-based Spreadsheet Processor - Pure Python

import re
from collections import defaultdict

class Cell:
    def __init__(self, value=""):
        self.value = value
        self.formula = value if str(value).startswith('=') else None
        self.dependencies = set()
        self.dependents = set()
        self._cached_value = None
        
    def __str__(self):
        return str(self.get_value())
    
    def get_value(self):
        if self.formula is None:
            try:
                return float(self.value)
            except ValueError:
                return self.value
        return self._cached_value

class Spreadsheet:
    def __init__(self, rows=10, cols=10):
        self.rows = rows
        self.cols = cols
        self.cells = defaultdict(Cell)
        self.col_width = defaultdict(lambda: 10)
    
    def get_cell_name(self, row, col):
        """Convert 0-based indices to A1 notation"""
        col_name = ""
        while col >= 0:
            col_name = chr(65 + (col % 26)) + col_name
            col = (col // 26) - 1
        return f"{col_name}{row + 1}"
    
    def parse_cell_name(self, name):
        """Convert A1 notation to 0-based indices"""
        match = re.match(r'([A-Z]+)([0-9]+)', name)
        if not match:
            raise ValueError(f"Invalid cell name: {name}")
        
        col_name, row = match.groups()
        col = 0
        for i, char in enumerate(reversed(col_name)):
            col += (ord(char) - 65 + 1) * (26 ** i)
        return int(row) - 1, col - 1
    
    def set_cell(self, cell_name, value):
        row, col = self.parse_cell_name(cell_name)
        cell = Cell(value)
        
        if cell.formula:
            cell.dependencies = self._get_dependencies(cell.formula)
            for dep in cell.dependencies:
                self.cells[dep].dependents.add(cell_name)
        
        self.cells[cell_name] = cell
        self._update_cell(cell_name)
    
    def _get_dependencies(self, formula):
        """Extract cell references from formula"""
        return set(re.findall(r'[A-Z]+[0-9]+', formula[1:]))
    
    def _update_cell(self, cell_name):
        """Update cell value and all dependent cells"""
        cell = self.cells[cell_name]
        if cell.formula:
            try:
                formula = cell.formula[1:]  # Remove '=' sign
                for dep in cell.dependencies:
                    dep_value = str(self.cells[dep].get_value())
                    formula = formula.replace(dep, dep_value)
                
                cell._cached_value = eval(formula)
            except Exception as e:
                cell._cached_value = f"#ERROR: {str(e)}"
        
        for dependent in cell.dependents:
            self._update_cell(dependent)
    
    def display(self):
        # Calculate column widths
        for cell_name in self.cells:
            row, col = self.parse_cell_name(cell_name)
            self.col_width[col] = max(
                self.col_width[col],
                len(str(self.cells[cell_name].get_value())) + 2
            )
        
        # Print header row
        print("    ", end="")
        for col in range(self.cols):
            col_name = self.get_cell_name(0, col)[:-1]
            print(f"{col_name:^{self.col_width[col]}}", end=" ")
        print()
        
        # Print cells
        for row in range(self.rows):
            print(f"{row + 1:3} ", end="")
            for col in range(self.cols):
                cell_name = self.get_cell_name(row, col)
                value = str(self.cells[cell_name].get_value())
                print(f"{value:^{self.col_width[col]}}", end=" ")
            print()

def main():
    sheet = Spreadsheet(5, 5)
    
    print("Welcome to the Text-Based Spreadsheet Processor!")
    print('Type "exit" to quit, "help" for commands.')
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == "exit":
            break
        elif command == "help":
            print("\nCommands:")
            print("- set A1 value : Set cell value (e.g., 'set A1 42' or 'set B1 =A1+10')")
            print("- display     : Show the spreadsheet")
            print("- exit        : Quit the program")
            print("- help        : Show this help message")
        elif command == "display":
            sheet.display()
        elif command.startswith("set "):
            try:
                _, cell, *value = command.split()
                value = " ".join(value)
                sheet.set_cell(cell.upper(), value)
                print(f"Cell {cell.upper()} set to {value}")
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Unknown command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()