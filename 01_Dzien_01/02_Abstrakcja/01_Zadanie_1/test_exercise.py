import unittest
from unittest.mock import patch, call

import exercise


class TraderTestCase(unittest.TestCase):
    def test_wallet_does_not_change_if_waiting_using_w_or_wait_or_empty(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'wait', '', '', '']
            exercise.main([5, 5, 5, 5, 5])

    def test_wallet_buying_using_buy(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'w', 'buy', '', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 60.0 PLN!')

    def test_wallet_buying_using_b(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['', '', 'b', '', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 60.0 PLN!')

    def test_wallet_selling_using_sell(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'w', 's', 'sell', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 40.0 PLN!')

    def test_wallet_selling_using_s(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'w', 'b', 's', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Your result: 40.0 PLN!')

    def test_asking_again_for_correct_command(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'w', 'Počkejte', 'w', 'b', 's']
            exercise.main([2, 2, 2, 4, 8])
        prt.assert_has_calls(
            [call('Invalid choice: Počkejte'), call('Your result: 200.0 PLN!')],
            any_order=True
        )

    def test_selling_with_no_usd_does_not_change_wallet(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'w', 's', 's', '']
            exercise.main([2, 3, 4, 5, 6])
        prt.assert_called_with('Your result: 100.0 PLN!')

    def test_buying_with_no_pln_does_not_change_wallet(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['w', 'b', 'b', 'b', 's']
            exercise.main([3, 4, 5, 6, 7])
        prt.assert_called_with('Your result: 175.0 PLN!')
