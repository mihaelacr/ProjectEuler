def find_n_tilings_loopy(canvas_height, canvas_width):
    n_tilings = 0

    for h in range(1, canvas_height + 1):
        vertical_tiling = canvas_height - h + 1
        
        for w in range(1, canvas_width + 1):
            horizontal_tiling = canvas_width - w + 1

            complete_tiling = vertical_tiling * horizontal_tiling

            n_tilings += complete_tiling

    return n_tilings

def find_n_tilings(H, W):
    # By rearranging the above loops (ie summations)
    # algebraically we get:
    # (W**2 - W**2/2 - W/2 + W) * (H**2 - H**2/2 - H/2 + H)
    # and simplifying further:
    return (W**2+W) * (H**2+H) // 4


target = 2_000_000
best = 0
best_hw = None

for H in range(20,100):
    for W in range(20, 100):

        if H < W:
            # avoid symmetric duplicates
            continue

        nrects = find_n_tilings(H, W)

        if abs(target - nrects) < abs(target - best):
            best = nrects
            best_hw = (H, W)
            print(f"New best {H}x{W} {nrects}")

print(best_hw[0] * best_hw[1])
