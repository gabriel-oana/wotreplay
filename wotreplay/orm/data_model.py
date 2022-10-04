import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, Date

Base = declarative_base()


class FileModel(Base):
    """
    Create data model for the details available in the performance part.
    """
    __tablename__ = 'wotreplay_file'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    date = Column(Date, default=datetime.datetime.utcnow)
    replay_date = Column(DateTime)
    filename = Column(String)
    is_replay_complete = Column(Boolean)
    processed = Column(Boolean)
    processing_time = Column(Integer)


class BattlePerformanceModel(Base):
    """
    Create data model for the details available in the performance part.
    """
    __tablename__ = 'wotreplay_battle_performance'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(Integer)
    file_id = Column(String)
    replay_date = Column(DateTime)
    stunned = Column(Float)
    direct_hits = Column(Integer)
    damage_assisted_radio = Column(Integer)
    stun_duration = Column(Integer)
    win_points = Column(Integer)
    damaged_while_moving = Column(Integer)
    kills = Column(Integer)
    percent_from_total_team_damage = Column(Integer)
    mark_of_mastery = Column(Integer)
    no_damage_direct_hits_received = Column(Integer)
    equipment_damage_dealt = Column(Integer)
    tkills = Column(Integer)
    shots = Column(Integer)
    team = Column(Integer)
    death_count = Column(Integer)
    stun_number = Column(Integer)
    spotted = Column(Integer)
    killer_id = Column(Integer)
    solo_flag_capture = Column(Integer)
    marks_on_gun = Column(Integer)
    killed_and_damaged_by_all_squad_mates = Column(Integer)
    rollouts_count = Column(Integer)
    health = Column(Integer)
    stop_respawn = Column(Integer)
    t_damage_dealt = Column(Integer)
    resource_absorbed = Column(Integer)
    damaged_while_enemy_moving = Column(Integer)
    damage_received = Column(Integer)
    percent_from_second_best_damage = Column(Integer)
    committed_suicide = Column(Integer)
    life_time = Column(Integer)
    damage_assisted_track = Column(Integer)
    sniper_damage_dealt = Column(Integer)
    fairplay_factor = Column(Integer)
    damage_blocked_by_armour = Column(Integer)
    damage_received_from_invisibles = Column(Integer)
    max_health = Column(Integer)
    moving_avg_damage = Column(Integer)
    flag_capture = Column(Integer)
    kills_before_team_was_damaged = Column(Integer)
    potential_damage_received = Column(Integer)
    direct_team_hits = Column(Integer)
    damage_dealt = Column(Integer)
    piercings_received = Column(Integer)
    piercings = Column(Integer)
    prev_mark_of_mastery = Column(Integer)
    dropped_capture_points = Column(Integer)
    damaged = Column(Integer)
    death_reason = Column(Integer)
    capture_points = Column(Integer)
    damage_before_team_was_damaged = Column(Integer)
    explosion_hits_received = Column(Integer)
    damage_rating = Column(Integer)
    mileage = Column(Integer)
    explosion_hits = Column(Integer)
    direct_hits_received = Column(Integer)
    is_team_killer = Column(Boolean)
    capturing_base = Column(Integer)
    damage_assisted_stun = Column(Integer)
    damage_assisted_smoke = Column(Integer)
    t_destroyed_modules = Column(Integer)
    damage_assisted_inspire = Column(Integer)


class BattleEconomyModel(Base):
    """
    Data model for data for the economy data contained in the replay.
    """
    __tablename__ = 'wotreplay_battle_economy'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(Integer)
    file_id = Column(String)
    replay_date = Column(DateTime)
    credits_to_draw = Column(Integer)
    original_prem_squad_credits = Column(Integer)
    credits_contribution_in = Column(Integer)
    event_credits = Column(Integer)
    piggy_bank = Column(Integer)
    premium_credits_factor_100 = Column(Integer)
    original_credits_contribution_in = Column(Integer)
    original_credits_penalty = Column(Integer)
    original_gold = Column(Integer)
    booster_credits = Column(Integer)
    referral_20_credits = Column(Integer)
    subtotal_event_coin = Column(Integer)
    booster_credits_factor_100 = Column(Integer)
    auto_load_cost_slot_1 = Column(Integer)
    auto_load_cost_slot_2 = Column(Integer)
    auto_load_cost_slot_3 = Column(Integer)
    credits_contribution_out = Column(Integer)
    original_credits_contribution_out = Column(Integer)
    premium_plus_credits_factor_100 = Column(Integer)
    credits = Column(Integer)
    auto_equip_cost_slot_1 = Column(Integer)
    auto_equip_cost_slot_2 = Column(Integer)
    auto_equip_cost_slot_3 = Column(Integer)
    gold_replay = Column(Integer)
    credits_penalty = Column(Integer)
    repair = Column(Integer)
    original_credits = Column(Integer)
    referral_20_credits_factor_100 = Column(Integer)
    order_credits = Column(Integer)
    order_credits_factor_100 = Column(Integer)
    original_crystal = Column(Integer)
    applied_premium_credits_factor_100 = Column(Integer)
    prem_squad_credits = Column(Integer)
    event_gold = Column(Integer)
    gold = Column(Integer)
    original_credits_contribution_in_squad = Column(Integer)
    original_event_coin = Column(Integer)
    factual_credits = Column(Integer)
    event_coin = Column(Integer)
    crystal = Column(Integer)
    crystal_replay = Column(Integer)
    original_credits_to_draw_squad = Column(Integer)
    subtotal_credits = Column(Integer)
    credits_replay = Column(Integer)
    event_event_coin = Column(Integer)
    subtotal_crystal = Column(Integer)
    achievement_credits = Column(Integer)
    subtotal_gold = Column(Integer)
    event_crystal = Column(Integer)
    event_coin_replay = Column(Integer)
    auto_repair_cost = Column(Integer)
    original_credits_penalty_squad = Column(Integer)
    original_credits_to_draw = Column(Integer)


class BattleXpModel(Base):
    """
    Create data model for the details available in the Player Personal Data.
    """
    __tablename__ = 'wotreplay_battle_xp'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(Integer)
    file_id = Column(String)
    replay_date = Column(DateTime)
    order_free_xp_factor_100 = Column(Integer)
    order_xp_factor_10 = Column(Integer)
    free_xp_replay = Column(Integer)
    xp_other = Column(Integer)
    premium_t_men_xp_factor_100 = Column(Integer)
    achievement_xp = Column(Integer)
    igr_xp_factor_100 = Column(Integer)
    event_t_men_xp = Column(Integer)
    premium_plus_xp_factor_100 = Column(Integer)
    premium_plus_t_men_xp_factor_100 = Column(Integer)
    original_t_men_xp = Column(Integer)
    referal_20_xp = Column(Integer)
    subtotal_t_men_xp = Column(Integer)
    premium_vehicle_xp_factor_100 = Column(Integer)
    additional_xp_factor_100 = Column(Integer)
    factual_xp = Column(Integer)
    order_free_xp = Column(Integer)
    booster_t_men_xp_factor_100 = Column(Integer)
    original_xp = Column(Integer)
    applied_premium_xp_factor_100 = Column(Integer)
    booster_xp = Column(Integer)
    factual_free_xp = Column(Integer)
    daily_xp_factor_10 = Column(Integer)
    event_free_xp = Column(Integer)
    player_rank_xp_factor_100 = Column(Integer)
    xp_penalty = Column(Integer)
    xp = Column(Integer)
    booster_xp_factor_100 = Column(Integer)
    order_t_men_xp = Column(Integer)
    original_xp_penalty = Column(Integer)
    order_t_men_xp_factor_100 = Column(Integer)
    subtotal_xp = Column(Integer)
    squad_xp = Column(Integer)
    original_free_xp = Column(Integer)
    xp_assist = Column(Integer)
    free_xp = Column(Integer)
    premium_vehicle_xp = Column(Integer)
    referral_20_xp_factor_100 = Column(Integer)
    event_xp = Column(Integer)
    subtotal_free_xp = Column(Integer)
    achievement_free_xp = Column(Integer)
    player_rank_xp = Column(Integer)
    squad_xp_factor_100 = Column(Integer)
    applied_premium_t_men_xp_factor_100 = Column(Integer)
    booster_t_men_xp = Column(Integer)
    xp_attack = Column(Integer)
    ref_system_xp_factor_10 = Column(Integer)
    t_men_xp_replay = Column(Integer)
    premium_xp_factor_100 = Column(Integer)
    t_men_xp = Column(Integer)
    booster_free_xp_factor_100 = Column(Integer)
    booster_free_xp = Column(Integer)
    battle_num = Column(Integer)


class CommonModel(Base):
    """
    Create data model for the details available in the Player Personal Data.
    """
    __tablename__ = 'wotreplay_common'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(String)
    file_id = Column(String)
    replay_date = Column(DateTime)
    division = Column(String)
    finish_reason = Column(Integer)
    gui_type = Column(Integer)
    arena_create_time = Column(Integer)
    duration = Column(Integer)
    arena_type_id = Column(Integer)
    gas_attack_winner_team = Column(Integer)
    winner_team = Column(Integer)
    veh_lock_mode = Column(Integer)
    bonus_type = Column(Integer)


class BattleFrags(Base):
    """
    Create data model for the details available in the Player Personal Data.
    """
    __tablename__ = 'wotreplay_battle_frags'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    file_id = Column(String)
    account_id = Column(String)
    replay_date = Column(DateTime)
    player_id = Column(String)
    fake_name = Column(String)
    team = Column(Integer)
    vehicle_type = Column(String)
    vehicle_tag = Column(String)
    vehicle_nation = Column(String)
    is_alive = Column(Boolean)
    forbid_in_battle_invitations = Column(Boolean)
    igr_type = Column(Integer)
    is_team_killer = Column(Boolean)
    name = Column(String)
    frags = Column(Integer)


class ReplayMetadataModel(Base):
    """
    Create data model for the details available in the Player Personal Data.
    """
    __tablename__ = 'wotreplay_metadata'
    __table_args__ = {'schema': 'main'}

    id = Column(Integer, primary_key=True)
    loaded_at = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(String)
    file_id = Column(String)
    replay_date = Column(DateTime)
    player_vehicle = Column(String)
    nation = Column(String)
    tank_tag = Column(String)
    version = Column(String)
    client_version = Column(String)
    client_version_executable = Column(String)
    region_code = Column(String)
    server_name = Column(String)
    map_display_name = Column(String)
    date_time = Column(String)
    map_name = Column(String)
    gameplay_id = Column(String)
    battle_type = Column(String)
    has_mods = Column(Boolean)
    player_name = Column(String)


class DataModel:

    @staticmethod
    def create_tables(engine):
        Base.metadata.create_all(engine)
















