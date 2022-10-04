import os
import datetime


class Extractor:

    @staticmethod
    def get_file_name(file: str) -> str:
        """
        Gets the filename of the replay without the path
        """

        filename = os.path.split(file)

        return filename[-1]

    @staticmethod
    def get_replay_date(metadata: dict):
        """
        Gets the datestamp of the replay without the path
        """

        replay_date = metadata.get('dateTime')
        d = datetime.datetime.strptime(replay_date, '%d.%m.%Y%H:%M:%S')

        return d

    @staticmethod
    def get_file_data(file: str) -> list:
        """
        Creates data for the initial file.
        """

        filename = os.path.split(file)
        data = [{
            "filename": filename[-1]
        }]

        return data

    @staticmethod
    def get_account_id(metadata: dict) -> str:
        """
        Retrieves the account id from the replay metadata.
        """

        account_id = metadata.get('playerID', 'None')

        return account_id

    @staticmethod
    def get_replay_metadata(data: dict, account_id: str, file_id: int, replay_date: str) -> list:
        """
        The metadata of the replay is contained within the first sector of the replay data.
        """

        battle_metadata = [{
            "replay_date": replay_date,
            "file_id": file_id,
            "player_vehicle": data.get('playerVehicle'),
            "nation": str(data.get('playerVehicle')).split('-')[0],
            "tank_tag": str(data.get('playerVehicle')).split('-')[1],
            "version": str(data.get('clientVersionFromXml')).split('#')[0].split('v.')[1],
            "client_version": data.get('clientVersionFromXml'),
            "client_version_executable": data.get('clientVersionFromExe'),
            "region_code": data.get('regionCode'),
            "account_id": account_id,
            "server_name": data.get('serverName'),
            "map_display_name": data.get('mapDisplayName'),
            "date_time": data.get('dateTime'),
            "map_name": data.get('mapName'),
            "gameplay_id": data.get('gameplayID'),
            "battle_type": data.get('battleType'),
            "has_mods": data.get('has_mods'),
            "player_name": data.get('playerName')
        }]

        return battle_metadata

    @staticmethod
    def get_battle_performance(data: list, account_id: str, file_id: int, replay_date: str) -> list:
        """
        Extracts all the parameters required to fill the model from the battle data.
        """

        raw_data = data[0]['personal']
        battle_id = list(raw_data.keys())[0]

        battle_data = raw_data[battle_id]

        battle_performance = [{
            "replay_date": replay_date,
            "file_id": file_id,
            "account_id": account_id,
            "stunned": battle_data.get('stunned', None),
            "direct_hits": battle_data.get('directHits', None),
            "damage_assisted_radio": battle_data.get('damageAssistedRadio', None),
            "stun_duration": battle_data.get('stunDuration', None),
            "win_points": battle_data.get('winPoints', None),
            "damaged_while_moving": battle_data.get('damagedWhileMoving', None),
            "kills": battle_data.get('kills', None),
            "percent_from_total_team_damage": battle_data.get('percentFromTotalTeamDamage', None),
            "mark_of_mastery": battle_data.get('markOfMastery', None),
            "no_damage_direct_hits_received": battle_data.get('noDamageDirectHitsReceived', None),
            "equipment_damage_dealt": battle_data.get('equipmentDamageDealt', None),
            "tkills": battle_data.get('tkills', None),
            "shots": battle_data.get('shots', None),
            "team": battle_data.get('team', None),
            "death_count": battle_data.get('deathCount', None),
            "stun_number": battle_data.get('stunNum', None),
            "spotted": battle_data.get('spotted', None),
            "killer_id": battle_data.get('killerID', None),
            "solo_flag_capture": battle_data.get('soloFlagCapture', None),
            "marks_on_gun": battle_data.get('marksOnGun', None),
            "killed_and_damaged_by_all_squad_mates": battle_data.get('killedAndDamagedByAllSquadmates', None),
            "rollouts_count": battle_data.get('rolloutsCount', None),
            "health": battle_data.get('health', None),
            "stop_respawn": battle_data.get('stopRespawn', None),
            "t_damage_dealt": battle_data.get('tdamageDealt', None),
            "resource_absorbed": battle_data.get('resourceAbsorbed', None),
            "damaged_while_enemy_moving": battle_data.get('damagedWhileEnemyMoving', None),
            "damage_received": battle_data.get('damageReceived', None),
            "percent_from_second_best_damage": battle_data.get('percentFromSecondBestDamage', None),
            "committed_suicide": battle_data.get('committedSuicide', None),
            "life_time": battle_data.get('lifeTime', None),
            "damage_assisted_track": battle_data.get('damageAssistedTrack', None),
            "sniper_damage_dealt": battle_data.get('sniperDamageDealt', None),
            "fairplay_factor": battle_data.get('fairplayFactor10', None),
            "damage_blocked_by_armour": battle_data.get('damageBlockedByArmor', None),
            "dropped_capture_points": battle_data.get('droppedCapturePoints', None),
            "damage_received_from_invisibles": battle_data.get('damageReceivedFromInvisibles', None),
            "max_health": battle_data.get('maxHealth', None),
            "moving_avg_damage": battle_data.get('movingAvgDamage', None),
            "flag_capture": battle_data.get('flagCapture', None),
            "kills_before_team_was_damaged": battle_data.get('killsBeforeTeamWasDamaged', None),
            "potential_damage_received": battle_data.get('potentialDamageReceived', None),
            "direct_team_hits": battle_data.get('directTeamHits', None),
            "damage_dealt": battle_data.get('damageDealt', None),
            "piercings_received": battle_data.get('piercingsReceived', None),
            "piercings": battle_data.get('piercings', None),
            "prev_mark_of_mastery": battle_data.get('prevMarkOfMastery', None),
            "damaged": battle_data.get('damaged', None),
            "death_reason": battle_data.get('deathReason', None),
            "capture_points": battle_data.get('capturePoints', None),
            "damage_before_team_was_damaged": battle_data.get('damageBeforeTeamWasDamaged', None),
            "explosion_hits_received": battle_data.get('explosionHitsReceived', None),
            "damage_rating": battle_data.get('damageRating', None),
            "mileage": battle_data.get('mileage', None),
            "explosion_hits": battle_data.get('explosionHits', None),
            "direct_hits_received": battle_data.get('directHitsReceived', None),
            "is_team_killer": battle_data.get('isTeamKiller', None),
            "capturing_base": battle_data.get('capturingBase', None),
            "damage_assisted_stun": battle_data.get('damageAssistedStun', None),
            "damage_assisted_smoke": battle_data.get('damageAssistedSmoke', None),
            "t_destroyed_modules": battle_data.get('tdestroyedModules', None),
            "damage_assisted_inspire": battle_data.get('damageAssistedInspire', None)
        }]

        return battle_performance

    @staticmethod
    def get_common(data: list, account_id: str, file_id: int, replay_date: str) -> list:
        """
        Extracts the common data from the battle replay.
        """

        raw_data = data[0]['common']
        response = [{
            "replay_date": replay_date,
            "file_id": file_id,
            "account_id": account_id,
            "division": raw_data.get('division', None),
            "gui_type": raw_data.get('guiType', None),
            "arena_create_time": raw_data.get('arenaCreateTime', None),
            "duration": raw_data.get('duration', None),
            "arena_type_id": raw_data.get('arenaTypeID', None),
            "gas_attack_winner_team": raw_data.get('gasAttackWinnerTeam', None),
            "winner_team": raw_data.get('winnerTeam', None),
            "veh_lock_mode": raw_data.get('vehLockMode', None),
            "bonus_type": raw_data.get('bonusType', None),
        }]

        return response

    @staticmethod
    def get_battle_frags(data: list, account_id: str, file_id: int, replay_date: str) -> list:
        """
        Extracts the players data from the battle replay
        """

        player_ids = list(data[1].keys())

        player_data = []
        for player_id in player_ids:
            raw_data = data[1][player_id]
            frags = data[2][player_id]['frags']

            player_data.append({
                "replay_date": replay_date,
                "account_id": account_id,
                "player_id": player_id,
                "file_id": file_id,
                "fake_name": raw_data.get('fakeName', 'None'),
                "team": raw_data['team'],
                "vehicle_type": raw_data['vehicleType'],
                "vehicle_tag": str(raw_data['vehicleType']).split(":")[-1],
                "vehicle_nation": str(raw_data['vehicleType']).split(":")[0],
                "is_alive": raw_data['isAlive'],
                "forbid_in_battle_invitations": raw_data['forbidInBattleInvitations'],
                "igr_type": raw_data['igrType'],
                "is_team_killer": raw_data['isTeamKiller'],
                "name": raw_data['name'],
                "frags": frags
            })

        return player_data

    @staticmethod
    def get_battle_economy(data: list, account_id: str, file_id: int, replay_date: str) -> list:
        """
        Extracts the economy data from the battle replay
        """

        raw_data = data[0]['personal']
        battle_id = list(raw_data.keys())[0]

        battle_data = raw_data[battle_id]

        battle_economy = [{
            "replay_date": replay_date,
            "file_id": file_id,
            "account_id": account_id,
            "credits_to_draw": battle_data.get('creditsToDraw', None),
            "original_prem_squad_credits": battle_data.get('originalPremSquadCredits', None),
            "credits_contribution_in": battle_data.get('creditsContributionIn', None),
            "event_credits": battle_data.get('eventCredits', None),
            "piggy_bank": battle_data.get('originalPremSquadCredits', None),
            "premium_credits_factor_100": battle_data.get('premiumCreditsFactor100', None),
            "original_credits_contribution_in": battle_data.get('originalCreditsContributionIn', None),
            "original_credits_penalty": battle_data.get('originalPremSquadCredits', None),
            "original_gold": battle_data.get('originalGold', None),
            "booster_credits": battle_data.get('boosterCredits', None),
            "referral_20_credits": battle_data.get('referral20Credits', None),
            "subtotal_event_coin": battle_data.get('subtotalEventCoin', None),
            "booster_credits_factor_100": battle_data.get('boosterCreditsFactor100', None),
            "credits_contribution_out": battle_data.get('creditsContributionOut', None),
            "premium_plus_credits_factor_100": battle_data.get('premiumPlusCreditsFactor100', None),
            "credits": battle_data.get('originalPremSquadCredits', None),
            "gold_replay": battle_data.get('goldReplay', None),
            "credits_penalty": battle_data.get('creditsPenalty', None),
            "repair": battle_data.get('repair', None),
            "original_credits": battle_data.get('originalCredits', None),
            "order_credits": battle_data.get('orderCredits', None),
            "order_credits_factor_100": battle_data.get('orderCreditsFactor100', None),
            "original_crystal": battle_data.get('originalCrystal', None),
            "applied_premium_credits_factor_100": battle_data.get('appliedPremiumCreditsFactor100', None),
            "prem_squad_credits": battle_data.get('premSquadCredits', None),
            "event_gold": battle_data.get('eventGold', None),
            "gold": battle_data.get('gold', None),
            "original_credits_contribution_in_squad": battle_data.get('originalCreditsContributionInSquad', None),
            "original_event_coin": battle_data.get('originalEventCoin', None),
            "factual_credits": battle_data.get('factualCredits', None),
            "event_coin": battle_data.get('eventCoin', None),
            "crystal": battle_data.get('crystal', None),
            "crystal_replay": battle_data.get('crystalReplay', None),
            "original_credits_to_draw_squad": battle_data.get('originalCreditsToDrawSquad', None),
            "subtotal_credits": battle_data.get('subtotalCredits', None),
            "credits_replay": battle_data.get('creditsReplay', None),
            "event_event_coin": battle_data.get('eventEventCoin', None),
            "subtotal_crystal": battle_data.get('subtotalCrystal', None),
            "achievement_credits": battle_data.get('achievementCredits', None),
            "subtotal_gold": battle_data.get('subtotalGold', None),
            "event_crystal": battle_data.get('eventCrystal', None),
            "event_coin_replay": battle_data.get('eventCoinReplay', None),
            "auto_repair_cost": battle_data.get('autoRepairCost', None),
            "original_credits_penalty_squad": battle_data.get('originalCreditsPenaltySquad', None)
        }]

        return battle_economy

    @staticmethod
    def get_battle_xp(data: list, account_id: str, file_id: int, replay_date: str) -> list:
        """
        Extracts the xp data from the battle replay
        """

        raw_data = data[0]['personal']
        battle_id = list(raw_data.keys())[0]

        battle_data = raw_data[battle_id]

        battle_xp = [{
            "replay_date": replay_date,
            "file_id": file_id,
            "account_id": account_id,
            "order_free_xp_factor_100": battle_data.get('orderFreeXPFactor100', None),
            "order_xp_factor_100": battle_data.get('orderXPFactor100', None),
            "free_xp_replay": battle_data.get('freeXPReplay', None),
            "xp_other": battle_data.get('xp/other', None),
            "premium_t_men_xp_factor_100": battle_data.get('premiumTmenXPFactor100', None),
            "achievement_xp": battle_data.get('achievementXP', None),
            "igr_xp_factor_10": battle_data.get('igrXPFactor10', None),
            "event_t_men_xp": battle_data.get('eventTMenXP', None),
            "premium_plus_xp_factor_100": battle_data.get('premiumPlusXPFactor100', None),
            "premium_plus_t_men_xp_factor_100": battle_data.get('premiumPlusTmenXPFactor100', None),
            "original_t_men_xp": battle_data.get('originalTMenXP', None),
            "referal_20_xp": battle_data.get('referral20XP', None),
            "subtotal_t_men_xp": battle_data.get('subtotalTMenXP', None),
            "premium_vehicle_xp_factor_100": battle_data.get('premiumVehicleXPFactor100', None),
            "additional_xp_factor_100": battle_data.get('additionalXPFactor10', None),
            "factual_xp": battle_data.get('factualXP', None),
            "order_free_xp": battle_data.get('orderFreeXP', None),
            "booster_t_men_xp_factor_100": battle_data.get('boosterTMenXPFactor100', None),
            "original_xp": battle_data.get('originalXP', None),
            "applied_premium_xp_factor_100": battle_data.get('appliedPremiumXPFactor100', None),
            "booster_xp": battle_data.get('boosterXP', None),
            "factual_free_xp": battle_data.get('factualFreeXP', None),
            "daily_xp_factor_10": battle_data.get('dailyXPFactor10', None),
            "event_free_xp": battle_data.get('eventFreeXP', None),
            "player_rank_xp_factor_100": battle_data.get('playerRankXPFactor100', None),
            "xp_penalty": battle_data.get('xpPenalty', None),
            "xp": battle_data.get('xp', None),
            "booster_xp_factor_100": battle_data.get('boosterXPFactor100', None),
            "order_t_men_xp": battle_data.get('orderTMenXP', None),
            "original_xp_penalty": battle_data.get('originalXPPenalty', None),
            "order_t_men_xp_factor_100": battle_data.get('orderTMenXPFactor100', None),
            "subtotal_xp": battle_data.get('subtotalXP', None),
            "squad_xp": battle_data.get('squadXP', None),
            "original_free_xp": battle_data.get('originalFreeXP', None),
            "xp_assist": battle_data.get('xp/assist', None),
            "free_xp": battle_data.get('freeXP', None),
            "premium_vehicle_xp": battle_data.get('premiumVehicleXP', None),
            "referral_20_xp_factor_100": battle_data.get('referral20XPFactor100', None),
            "event_xp": battle_data.get('eventXP', None),
            "subtotal_free_xp": battle_data.get('subtotalFreeXP', None),
            "achievement_free_xp": battle_data.get('achievementFreeXP', None),
            "player_rank_xp": battle_data.get('playerRankXP', None),
            "squad_xp_factor_100": battle_data.get('squadXPFactor100', None),
            "applied_premium_t_men_xp_factor_100": battle_data.get('appliedPremiumTmenXPFactor100', None),
            "booster_t_men_xp": battle_data.get('boosterTMenXP', None),
            "xp_attack": battle_data.get('xp/attack', None),
            "ref_system_xp_factor_10": battle_data.get('refSystemXPFactor10', None),
            "t_men_xp_replay": battle_data.get('tmenXPReplay', None),
            "premium_xp_factor_100": battle_data.get('premiumXPFactor100', None),
            "t_men_xp": battle_data.get('tmenXP', None),
            "booster_free_xp_factor_100": battle_data.get('boosterFreeXPFactor100', None),
            "booster_free_xp": battle_data.get('boosterFreeXP', None),
            "battle_num": battle_data.get('battleNum', None)

        }]

        return battle_xp
