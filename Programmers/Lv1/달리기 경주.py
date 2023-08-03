def solution(players, callings):
    player = {n : i for i, n in enumerate(players)}
    
    for call in callings:
        idx = player[call]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        player[players[idx]], player[players[idx - 1]] = player[players[idx - 1]], player[players[idx]]

    return players