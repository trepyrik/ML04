classDiagram
    class OrthogonalStructure {
        -int width
        -int height
        -Cell[][] grid
        +OrthogonalStructure(width, height)
        +getWidth() int
        +getHeight() int
        +getCell(x, y) Cell
        +setCell(x, y, cell) void
        +isValidPosition(x, y) boolean
        +traverse() Iterator~Cell~
    }

    class Cell {
        -int x
        -int y
        -Object value
        +Cell(x, y, value)
        +getX() int
        +getY() int
        +getValue() Object
        +setValue(value) void
    }

    class StructureOperations {
        +static findNeighbors(structure, x, y) List~Cell~
        +static findPath(start, end) List~Cell~
        +static calculateArea(structure) int
        +static validateStructure(structure) boolean
    }

    OrthogonalStructure "1" -- "*" Cell : содержит
    StructureOperations ..> OrthogonalStructure : использует
    StructureOperations ..> Cell : использует

    