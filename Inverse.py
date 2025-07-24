import math

def dd_to_dms(deg):
    d = int(deg)
    m_float = (deg - d) * 60
    m = int(m_float)
    s = (m_float - m) * 60
    return f"{d}°{m:02d}'{s:.0f}\""

def distance_2d(x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    dist = math.hypot(dx, dy)
    azimuth_dd = math.degrees(math.atan2(dx, dy))
    if azimuth_dd < 0:
        azimuth_dd += 360

    azimuth_dms = dd_to_dms(azimuth_dd)

    vd = z2 - z1
    slope_percent = (vd / dist) * 100
    math.sqrt(dx**2 + dy**2 + dz**2)

    return f"Distance:       {dist:.3f}m\nAzimuth:    {azimuth_dms}\nVertical:       {vd:.3f}m\nSlope:           {slope_percent:.2f}%"

print(distance_2d(494933.462, 6361105.375, 349.138, 494932.613, 6361106.636, 349.153))