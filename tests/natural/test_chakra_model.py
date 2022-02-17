
import nlp.natural.chakras.base as nnc


def test_model_init():
    a = nnc.make_body()

    for ckey, cval in a.CHAKRAS[a.P_CHAKRA].items():
        assert cval == 0
    for ckey, cval in a.CHAKRAS[a.N_CHAKRA].items():
        assert cval == 0
    for ckey, cval in a.CHAKRAS[a.Q_CHAKRA].items():
        assert cval == 0
    for ckey, cval in a.STATES[a.P_CHAKRA].items():
        assert cval is True
    for ckey, cval in a.STATES[a.N_CHAKRA].items():
        assert cval is True
    for ckey, cval in a.STATES[a.Q_CHAKRA].items():
        assert cval is True


def test_model_infuse():
    assert nnc.infuse(20, 80) == 16
    assert nnc.infuse(20, 80, category=nnc.EXTERNAL) == 8


def test_model_reset():
    assert nnc.infuse(20, 80) == 16
    assert nnc.infuse(20, 80, category=nnc.EXTERNAL) == 8

    a = nnc.make_body()
    a.disturb(nnc.EARTH, 80)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.EARTH] == -80
    a.reset()
    assert a.CHAKRAS[a.P_CHAKRA][nnc.EARTH] == 0


def test_model_disturb():
    a = nnc.make_body()
    a.disturb(nnc.EARTH, 80)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.EARTH] == -80
    assert a.CHAKRAS[a.N_CHAKRA][nnc.EARTH] == -80
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.EARTH] == -80

    a.disturb(nnc.EARTH, 40, single=a.P_CHAKRA)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.EARTH] == -120
    assert a.CHAKRAS[a.N_CHAKRA][nnc.EARTH] == -80
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.EARTH] == -80


def test_model_recover():
    a = nnc.make_body()
    a.recover(nnc.WATER, 50)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 50

    a.recover(nnc.WATER, 400, single=a.N_CHAKRA)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 450
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 50

    a.recover(nnc.HEART, 4000)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 450
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.P_CHAKRA][nnc.HEART] == 4000
    assert a.CHAKRAS[a.N_CHAKRA][nnc.HEART] == 4000
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.HEART] == 4000


def test_model_balance():
    a = nnc.make_body()
    a.recover(nnc.WATER, 50)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 50

    a.balance(nnc.WATER, single=a.Q_CHAKRA)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 0

    a.disturb(nnc.WATER, 70)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == -20
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == -20
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == -70

    a.balance(nnc.WATER)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 0
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 0
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 0


def test_model_block_unblock():
    a = nnc.make_body()
    a.block(nnc.WATER)
    a.recover(nnc.WATER, 50)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 0
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 0
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 0

    a.block(nnc.FIRE, single=a.N_CHAKRA)
    a.disturb(nnc.FIRE, 30)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.FIRE] == -30
    assert a.CHAKRAS[a.N_CHAKRA][nnc.FIRE] == 0
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.FIRE] == -30

    a.unblock(nnc.WATER, single=a.P_CHAKRA)
    a.recover(nnc.WATER, 50)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 0
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 0

    a.unblock(nnc.WATER)
    a.recover(nnc.WATER, 50)
    assert a.CHAKRAS[a.P_CHAKRA][nnc.WATER] == 100
    assert a.CHAKRAS[a.N_CHAKRA][nnc.WATER] == 50
    assert a.CHAKRAS[a.Q_CHAKRA][nnc.WATER] == 50


def test_model_distribution_generation():
    a = nnc.make_body()

    a.recover(nnc.EARTH, 10, single=a.P_CHAKRA)
    a.recover(nnc.FIRE, -10, single=a.P_CHAKRA)
    a.recover(nnc.SOUND, -40, single=a.P_CHAKRA)
    a.recover(nnc.COSMIC, 10, single=a.P_CHAKRA)
    a.CHAKRAS[a.P_CHAKRA][nnc.WATER] = 93
    a.CHAKRAS[a.P_CHAKRA][nnc.HEART] = 100
    a.CHAKRAS[a.P_CHAKRA][nnc.LIGHT] = 50
    a.CHAKRAS[a.P_CHAKRA][nnc.CONFIDENCE] = .84

    assert a.chakraDistribution(a.P_CHAKRA) == {'earth_chakra': 42.44,
                                                'water_chakra': 75.73,
                                                'fire_chakra': 35.04,
                                                'heart_chakra': 79.61,
                                                'sound_chakra': 19.91,
                                                'light_chakra': 57.24,
                                                'thought_chakra': 42.44,
                                                'confidence_level': 84,
                                                'chakra_level': 213}
