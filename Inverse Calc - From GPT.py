import math

def decimal_to_dms(decimal_deg):
    degrees = int(decimal_deg)
    minutes_full = (decimal_deg - degrees) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60
    return degrees, minutes, seconds

def inverse(p1, p2):
    # Points
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    # Z values
    z1 = p1[2] if len(p1) > 2 else None
    z2 = p2[2] if len(p2) > 2 else None

    # Deltas
    dx = x2 - x1
    dy = y2 - y1
    dz = None
    if z1 is not None and z2 is not None:
        dz = z2 - z1

    # Hz distance
    horiz_dist = math.sqrt(dx**2 + dy**2)

    # Slope distance if Z applies
    slope_dist = horiz_dist
    if dz is not None:
        slope_dist = math.sqrt(dx**2 + dy**2 + dz**2)

    # Azimuth in DD
    azimuth_rad = math.atan2(dx, dy)
    azimuth_deg = math.degrees(azimuth_rad)
    if azimuth_deg < 0:
        azimuth_deg += 360

    # Convert azimuth to DMS
    d, m, s = decimal_to_dms(azimuth_deg)

    # Inverse report
    print("----------------------------------------")
    print("       Inverse Report - Pt1 → Pt2       ")
    print("----------------------------------------")
    print(f"Delta E: {dx:+.3f} m")
    print(f"Delta N: {dy:+.3f} m")
    if dz is not None:
        print(f"Delta Elev: {dz:+.3f} m")
    print(f"Horiz Distance: {horiz_dist:.3f} m")
    if dz is not None:
        print(f"Slope Distance: {slope_dist:.3f} m")
    print(f"Azimuth: {azimuth_deg:.3f}°")
    print(f"Azimuth (DMS): {d:3d}° {m:02d}' {int(round(s)):02d}\"")
    print("----------------------------------------")

# Coordinate Input
p1 = input("Point 1 (E,N,V): ")
p2 = input("Point 2 (E,N,V): ")

inverse(p1, p2)