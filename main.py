from src import Rovers, Position, Plateau


def main():
    plateau = Plateau(5, 5)
    position = Position(1, 2)
    # Create rover instance
    rovers = Rovers(plateau, position, Rovers.directions.get('N'))
    instructions = input('Enter Instructions:')

    rovers.validate_instruction(instructions)
    print(rovers)
    rovers.set_position(3, 3, Rovers.directions.get('E'))
    instructions_new = input('Enter New Instructions:')
    rovers.validate_instruction(instructions_new)
    print(rovers)


if __name__ == "__main__":
    main()
