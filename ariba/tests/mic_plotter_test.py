import unittest
import os
from ariba import mic_plotter

modules_dir = os.path.dirname(os.path.abspath(mic_plotter.__file__))
data_dir = os.path.join(modules_dir, 'tests', 'data')


class TestMicPlotter(unittest.TestCase):
    def test_mic_string_to_float(self):
        '''Test _mic_string_to_float'''
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('42.42'), 42.42)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('42'), 42.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('>42'), 84.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('> 42'), 84.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('>=42'), 42.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('>= 42'), 42.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('<42'), 21.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('< 42'), 21.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('<=42'), 42.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('<= 42'), 42.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('   <=  42.0   '), 42.0)
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('na'), 'NA')
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('NA'), 'NA')
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float('.'), 'NA')
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float(' '), 'NA')
        self.assertEqual(mic_plotter.MicPlotter._mic_string_to_float(''), 'NA')


    def test_load_mic_file(self):
        '''Test _load_mic_file'''
        infile = os.path.join(data_dir, 'mic_plotter_load_mic_file.tsv')
        got = mic_plotter.MicPlotter._load_mic_file(infile)
        expected = {
            'sample1': {'antibio1': 0.25, 'antibio2': 0.004},
            'sample2': {'antibio1': 0.125, 'antibio2': 0.004},
            'sample3': {'antibio1': 0.125, 'antibio2': 0.004},
            'sample4': {'antibio1': 512.0, 'antibio2': 256.0},
            'sample5': {'antibio1': 512.0, 'antibio2': 256.0},
            'sample6': {'antibio1': 'NA', 'antibio2': 1.0},
        }

        self.assertEqual(got, expected)


    def test_load_summary_file(self):
        '''Test _load_summary_file'''
        infile = os.path.join(data_dir, 'mic_plotter_load_summary_file.tsv')
        got = mic_plotter.MicPlotter._load_summary_file(infile)
        expected = {
            'name1': {
                'cluster1': {'assembled': 'yes', 'match': 'yes', 'ref_seq': 'ref1', 'pct_id': 100.0, 'known_var': 'no', 'novel_var': 'no', 'group1.A42T': 'no', 'group1.A42T.%': 'NA'},
                'cluster2': {'assembled': 'yes', 'match': 'yes', 'ref_seq': 'ref2', 'pct_id': 99.0, 'known_var': 'yes', 'novel_var': 'no', 'group1.A42T': 'yes', 'group1.A42T.%': 95.42},
            },
            'name2': {
                'cluster1': {'assembled': 'yes', 'match': 'yes_nonunique', 'ref_seq': 'ref3', 'pct_id': 99.0, 'known_var': 'yes', 'novel_var': 'no', 'group1.A42T': 'yes', 'group1.A42T.%': 90.90},
                'cluster2': {'assembled': 'no', 'match': 'no', 'ref_seq': 'NA', 'pct_id': 'NA', 'known_var': 'NA', 'novel_var': 'NA', 'group1.A42T': 'NA', 'group1.A42T.%': 'NA'},
            },
        }
        self.maxDiff = None
        self.assertEqual(got, expected)

