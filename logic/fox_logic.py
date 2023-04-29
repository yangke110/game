from actions import acttack


def do_fox_logic(m_n, x, y, ms: str):
    if len(ms) > 0:
        print('have monsters ,attack~!')
        acttack.attack()
