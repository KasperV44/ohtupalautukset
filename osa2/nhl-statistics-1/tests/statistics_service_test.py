import sys
import os
import unittest

# Lisätään src-kansio Pythonin hakupolkuun
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_found(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_not_found(self):
        player = self.stats.search("Selänne")
        self.assertIsNone(player)

    def test_team(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)

    def test_top(self):
        top_players = self.stats.top(2)
        self.assertEqual(top_players[0].name, "Gretzky")
