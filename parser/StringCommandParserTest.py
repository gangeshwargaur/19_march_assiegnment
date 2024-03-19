import unittest
from assiegnment.rover.parser import StringCommandParser
from assiegnment.rover.commands import MoveCommand, RotateLeftCommand, RotateRightCommand

class StringCommandParserTest(unittest.TestCase):

    def test_string_L_maps_to_RotateLeftCommand(self):

        parser = StringCommandParser("L")


        commands = parser.toCommands()


        self.assertIsInstance(commands[0], RotateLeftCommand)
        self.assertEqual(1, len(commands))

    def test_string_R_maps_to_RotateRightCommand(self):

        parser = StringCommandParser("R")


        commands = parser.toCommands()


        self.assertIsInstance(commands[0], RotateRightCommand)

    def test_string_M_maps_to_MoveCommand(self):

        parser = StringCommandParser("M")


        commands = parser.toCommands()


        self.assertIsInstance(commands[0], MoveCommand)

    def test_empty_string_results_in_empty_command_list(self):

        parser = StringCommandParser("")


        commands = parser.toCommands()


        self.assertEqual(0, len(commands))

    def test_null_string_results_in_empty_command_list(self):

        parser = StringCommandParser(None)


        commands = parser.toCommands()


        self.assertEqual(0, len(commands))

    def test_string_to_command_mapping_is_case_insensitive(self):

        parser = StringCommandParser("mM")


        commands = parser.toCommands()


        self.assertIsInstance(commands[0], MoveCommand)
        self.assertIsInstance(commands[1], MoveCommand)

    def test_multi_command_string_is_mapped_to_commands_in_same_order(self):

        parser = StringCommandParser("MRL")

        commands = parser.toCommands()


        self.assertIsInstance(commands[0], MoveCommand)
        self.assertIsInstance(commands[1], RotateRightCommand)
        self.assertIsInstance(commands[2], RotateLeftCommand)