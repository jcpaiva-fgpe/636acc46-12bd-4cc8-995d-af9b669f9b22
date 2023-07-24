colors = {"Black": (0, 0, 0), "White": (255,255,255), "Red": (255, 0, 0),
          "Green": (0,255, 0), "Blue": (0, 0,255), "Yellow": (255,255, 0),
          "Cyan": (0,255,255), "Magenta": (255, 0,255)}

def calc_dist(color, r, g, b):
    dist_r = (colors[color][0] - r) ** 2
    dist_g = (colors[color][1] - g) ** 2
    dist_b = (colors[color][2] - b) ** 2
    dist = (dist_r + dist_g + dist_b) ** 0.5
    return dist    

def closest_color(r, g, b):
    best = "Black"
    best_dist = calc_dist(best, r, g, b)
    for cl in colors:
        dist = calc_dist(cl, r, g, b)
        if dist < best_dist: best = cl
    return best

print (closest_color(255, 165, 0)) # orange
print (closest_color(255,192,203)) # pink
print (closest_color(0,128,128)) # teal
