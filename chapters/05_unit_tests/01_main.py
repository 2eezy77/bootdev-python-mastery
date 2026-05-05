'''Testing specific functions after answering question
    - Here we are adding 100xp per level and adding additional xp per upgrade
    - & Combining the current_xp (per level) with the additional xp gained after an upgrade' 
'''
def xp_upgrade(level, xp_added):
    current_xp = level * 200
    return xp_added + current_xp

