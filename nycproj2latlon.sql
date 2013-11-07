UPDATE graffiti_locations
SET the_geom = ST_Transform(
  ST_SetSRID(
    ST_MakePoint(x * 0.3048006096012192, y * 0.3048006096012192), 
    32118),
  4326
)