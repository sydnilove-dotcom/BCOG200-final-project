import unittest

import game


class GameFunctionTests(unittest.TestCase):
    def setUp(self):
        game.reset_game()

    def test_move_pacman_eats_pellet_and_scores(self):
        game.move_pacman(1, 0)

        self.assertEqual(game.score, 10)
        self.assertEqual(game.find_character("P"), (7, 8))

    def test_find_next_step_toward_targets_pacman(self):
        ghost = game.ghosts[0]
        pacman_row, pacman_col = game.find_character("P")

        next_step = game.find_next_step_toward(
            ghost["row"],
            ghost["col"],
            pacman_row,
            pacman_col,
        )

        self.assertEqual(next_step, (7, 12))

    def test_pacman_can_eat_frightened_ghost(self):
        game.game_map[7][7] = " "
        game.game_map[7][12] = "P"
        game.frightened = True

        game.move_pacman(1, 0)

        self.assertEqual(game.score, game.GHOST_POINTS)
        self.assertEqual(len(game.ghosts), 2)
        self.assertEqual(len(game.eaten_ghosts), 1)
        self.assertEqual(game.find_character("P"), (7, 13))


if __name__ == "__main__":
    unittest.main()
