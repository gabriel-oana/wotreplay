import unittest
import datetime
from wotreplay.wotreplay import ReplayData


class TestReplayData(unittest.TestCase):

    replay = ReplayData(file_path='replay_data/test.wotreplay', db_name='', db_path='', load=False)

    def test_battle_metadata(self):
        battle_metadata = self.replay.battle_metadata
        expected = [{'replay_date': datetime.datetime(2020, 4, 29, 17, 57, 18), 'file_id': 0,
                     'player_vehicle': 'italy-It13_Progetto_M35_mod_46', 'nation': 'italy',
                     'tank_tag': 'It13_Progetto_M35_mod_46', 'version': '1.9.0.1',
                     'client_version': 'World\xa0of\xa0Tanksv.1.9.0.1#287', 'client_version_executable': '1.9.0.0',
                     'region_code': 'EU', 'account_id': 508670392, 'server_name': 'WOTEU2',
                     'map_display_name': 'Lakeville', 'date_time': '29.04.202017:57:18', 'map_name': '07_lakeville',
                     'gameplay_id': 'ctf', 'battle_type': 1, 'has_mods': None, 'player_name': 'Gabezzone'}]

        self.assertListEqual(battle_metadata, expected)

    def test_battle_performance(self):
        battle_performance = self.replay.battle_performance
        expected = [{'replay_date': datetime.datetime(2020, 4, 29, 17, 57, 18), 'file_id': 0, 'account_id': 508670392,
                     'stunned': 0, 'direct_hits': 5, 'damage_assisted_radio': 0, 'stun_duration': 0.0, 'win_points': 0,
                     'damaged_while_moving': 1, 'kills': 1, 'percent_from_total_team_damage': 2.498714652956298,
                     'mark_of_mastery': 0, 'no_damage_direct_hits_received': 0, 'equipment_damage_dealt': 0,
                     'tkills': 0, 'shots': 9, 'team': 1, 'death_count': 1, 'stun_number': 0, 'spotted': 0,
                     'killer_id': 19784876, 'solo_flag_capture': 0, 'marks_on_gun': 0,
                     'killed_and_damaged_by_all_squad_mates': 0, 'rollouts_count': 1, 'health': -3,
                     'stop_respawn': False, 't_damage_dealt': 0, 'resource_absorbed': 0,
                     'damaged_while_enemy_moving': 1, 'damage_received': 1400, 'percent_from_second_best_damage': 0.0,
                     'committed_suicide': False, 'life_time': 135, 'damage_assisted_track': 713,
                     'sniper_damage_dealt': 97, 'fairplay_factor': 0, 'damage_blocked_by_armour': 0,
                     'dropped_capture_points': 0, 'damage_received_from_invisibles': 311, 'max_health': 1400,
                     'moving_avg_damage': 1808, 'flag_capture': 0, 'kills_before_team_was_damaged': 0,
                     'potential_damage_received': 1270, 'direct_team_hits': 1, 'damage_dealt': 486,
                     'piercings_received': 3, 'piercings': 2, 'prev_mark_of_mastery': 3, 'damaged': 2,
                     'death_reason': 0, 'capture_points': 0, 'damage_before_team_was_damaged': 0,
                     'explosion_hits_received': 0, 'damage_rating': 63, 'mileage': 797, 'explosion_hits': 0,
                     'direct_hits_received': 3, 'is_team_killer': False, 'capturing_base': None,
                     'damage_assisted_stun': 0, 'damage_assisted_smoke': 0, 't_destroyed_modules': 0,
                     'damage_assisted_inspire': 0}]

        self.assertListEqual(battle_performance, expected)